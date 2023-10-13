import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder.appName("Spark Ramsey").getOrCreate()
    WithSpark(spark).possiblePathsParallel(8, 8)
    spark.stop
  }
}
case class WithSpark(spark: SparkSession) {
  val sc = spark
  import spark.implicits._
  def possiblePathsParallel(modulo: Long, partitions: Int = 12) = sc
    .range(partitions)
    .map(_.toLong)
    .repartition(partitions)
    .mapPartitions(F.possiblePaths(modulo))
}

object F {
  def otherNodes(modulo: Long): IndexedSeq[Long] = otherNodes(modulo.toInt)
    .map(_.toLong)

  def otherNodes(modulo: Int) = Range(1, modulo)

  case class Partition(i: Long, of: Long) {
    def values(modulo: Long) = otherNodes(modulo)
      .filter( _ % of == i)
  }

  def possiblePaths(modulo: Long)(values: Iterator[Long]): Iterator[Seq[Long]] = values
    .flatMap(possiblePaths(modulo, _))

  def possiblePaths(modulo: Long, first: Long): Iterator[Seq[Long]] = otherNodes(modulo)
    .filterNot( _ == first)
    .permutations
    .map(first +: _ :+ 0)
}
