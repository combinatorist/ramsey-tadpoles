import org.apache.spark.sql.{SparkSession, Dataset, Row}

object Main {
  def session() =
    SparkSession.builder.appName("Spark Ramsey").getOrCreate()

  def main(args: Array[String]): Unit = {
    val modulo = args(0).toLong
    val df = process(modulo)
    df.sparkSession.stop()
  }

  def process(modulo: Long): Dataset[Row] = {
    val spark = session
    val df = WithSpark(spark).fromScratch(modulo, modulo.toInt - 1)
    df.cache.show(false)
    // likely need sudo access for second disk. :(
    df.write.mode("overwrite").save(s"/data/ramsey/spark/df-overwritten-mod-$modulo")
    df.toDF
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
