import org.apache.spark.sql.{SparkSession, Dataset, Row}

object Main {
  def session() =
    SparkSession.builder.appName("Spark Ramsey").getOrCreate()

  def main(args: Array[String]): Unit = {
    val df = process
    df.sparkSession.stop()
  }

  def process(): Dataset[Row] = {
    val spark = session
    val df = WithSpark(spark).fromScratch(8, 8)
    df.show(false)
    df.write.mode("overwrite").save("df-overwritten")
    df.toDF
  }
}

case class WithSpark(spark: SparkSession) {
  val sc = spark
  import spark.implicits._

  def possiblePathsParallel(modulo: Long, partitions: Int) = sc
    .range(partitions)
    .map(_.toLong)
    .repartition(partitions)
    .mapPartitions(F.possiblePaths(modulo))

  def fromScratch(modulo: Long, partitions: Int = 12) =
    possiblePathsParallel(modulo, partitions)
      .map(F.chordSeq _)
      .filter(F.isCanonical(modulo.toInt) _)

}
