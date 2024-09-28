import org.apache.spark.sql.{SparkSession, Dataset, Row, functions => F}
import scala.sys.process._
import java.util.UUID
import util.Random

object Main {
  def session() =
    SparkSession.builder().appName("Spark Ramsey").getOrCreate()

  def main(args: Array[String]): Unit = {
    val modulo = args(0).toInt
    val mainSeed = args.lift(1).fold(Random.nextInt())(_.toInt)
    val df = process(modulo, mainSeed)
    df.sparkSession.stop()
  }

  def gitBranch = Process("git branch --show-current").lazyLines.head
  def gitSha = Process("git rev-parse --short HEAD").lazyLines.head
  def gitAuthorDate =
    Process(
      """git log -n1 --format="%ad" --date=iso-strict"""
    ).lazyLines.head
  def gitIsDirty = Process("git status --short").lazyLines.nonEmpty

  def process(modulo: Int, mainSeed: Int): Dataset[Row] = {
    val runId = UUID.randomUUID().toString
    val spark = session()
    import spark.sqlContext.implicits._
    val logDf =
      List(runId)
        .toDF()
        .withColumn("modulo", F.lit(modulo))
        .withColumn("mainSeed", F.lit(mainSeed))
        .withColumn("git_branch", F.lit(gitBranch))
        .withColumn("git_sha", F.lit(gitSha))
        .withColumn("git_author_date", F.lit(gitAuthorDate))
        .withColumn("git_is_dirty", F.lit(gitIsDirty))

    val sharedPath = "/data/ramsey/spark/random_sample"
    def log(logEnd: Boolean) =
      logDf
        .withColumn("run_id", F.lit(runId))
        .withColumn("log_type", F.lit(if (logEnd) "end" else "start"))
        .withColumn("log_time", F.current_timestamp())
        .write
        .mode("append")
        .save(s"$sharedPath/run_log/storage_version=6.0")

    log(logEnd = false)

    val df =
      WithSpark(spark, modulo, mainSeed).fromScratch
        .withColumn("modulo", F.lit(modulo))
        .withColumn("storage_version", F.lit("v4.1"))
        .withColumn("run_id", F.lit(runId))

    df.write
      .mode("append")
      .partitionBy("modulo", "run_id", "partitionSeed")
      .save(s"$sharedPath/hamiltonian_chord_sequences/storage_version=6.0")

    log(logEnd = true)

    df.toDF()
  }
}

final case class WithSpark(spark: SparkSession, modulo: Int, mainSeed: Int) {
  val threads = 15
  val rounds = 1
  val partitions = threads * rounds
  val N = pure.F.factorial(9)
  import spark.implicits._

  def fromScratch =
    spark
      .range(partitions)
      .repartition(partitions)
      .mapPartitions(
        _.flatMap(i =>
          pure.F.shuffleN(modulo)(N, mainSeed + i.toInt)
        )
      )

}
