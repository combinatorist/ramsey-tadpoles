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

  def chordSeq(wrappedCycle: Seq[Long]) = wrappedCycle
    .sliding(2, 10)
    .map(x => x.last - x.head)
    .toSeq

  // assumes same length
  def lessThanSeq(a: Seq[Long], b: Seq[Long]) = a.lazyZip(b).exists(_ < _)

  def isCanonical(modulo: Int)(chordSeq: Seq[Long]) = !Iterator
    .continually(chordSeq)
    .flatten
    .drop(1) //don't start with the current chordSeq!
    .sliding(modulo)
    .takeWhile(_ != chordSeq)
    .exists(lessThanSeq(_, chordSeq))

}

/*
object SeqOrdering extends Ordering[Seq[Long]] {
  // assumes same length
  def compare(a: Seq[Long], b: Seq[Long]) = {
    val toCompare = a.zip(b)
      .toIterator
      .dropWhile{ case (a, b) => a == b }
    toCompare.nextOption match {
      case None => 0
      case Some((x, y)) => x compare y
    }
  }
}
*/
