import org.apache.spark.sql.{SparkSession, Dataset, Row, functions => F}
import scala.sys.process._
import java.util.UUID

object Main {
  def session() =
    SparkSession.builder().appName("Spark Ramsey").getOrCreate()

  def main(args: Array[String]): Unit = {
    val modulo = args(0).toLong
    val df = process(modulo)
    df.sparkSession.stop()
  }

  def gitBranch = Process("git branch --show-current").lazyLines.head
  def gitSha = Process("git rev-parse --short HEAD").lazyLines.head
  def gitAuthorDate = Process("""git log -n1 --format="%ad" --date=iso-strict""")
    .lazyLines
     .head
  def gitIsDirty = Process("git status --short").lazyLines.nonEmpty

  def process(modulo: Long): Dataset[Row] = {
    val runId = UUID.randomUUID().toString
    val spark = session()
    import spark.sqlContext.implicits._
    val logDf = List(runId).toDF()
      .withColumn("storage_version", F.lit("v2.0"))
      .withColumn("git_branch", F.lit(gitBranch))
      .withColumn("git_sha", F.lit(gitSha))
      .withColumn("git_author_date", F.lit(gitAuthorDate))
      .withColumn("git_is_dirty", F.lit(gitIsDirty))

    def log(logEnd: Boolean) = logDf
      .withColumn("log_type", F.lit(if (logEnd) "end" else "start"))
      .withColumn("log_time", F.current_timestamp())
      .write
      .mode("append")
      .partitionBy(
        "storage_version",
        "log_time",
        "git_branch",
        "git_sha",
        "git_author_date",
        "git_is_dirty"
      )
      .save("/data/ramsey/spark/run_log")

    log(logEnd=false)

    val df = WithSpark(spark).fromScratch(modulo, modulo.toInt - 1)
      .withColumn("modulo", F.lit(modulo))
      .withColumn("storage_version", F.lit("v3.0"))
      .withColumn("run_id", F.lit(runId))
    df.write.mode("append")
      .partitionBy("storage_version", "modulo", "run_id")
      .save(s"/data/ramsey/spark/hamiltonian_chord_sequences/")


    log(logEnd=true)

    df.toDF()
  }
}

case class WithSpark(spark: SparkSession) {
  import spark.implicits._

  def possiblePathsParallel(modulo: Long, partitions: Int) = spark
    .range(partitions)
    .map(_ + 1L) //no 0 -> 0 self loop
    .repartition(partitions)
    .mapPartitions(pure.F.possiblePaths(modulo))

  def fromScratch(modulo: Long, partitions: Int) = {
    possiblePathsParallel(modulo, partitions)
      .map(pure.F.toChordSeq(modulo))
      .filter(pure.F.isCanonical(modulo.toInt) _)
  }

}
