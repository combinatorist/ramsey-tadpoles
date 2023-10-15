package pure
object Main {
  def main(args: Array[String]): Unit = {
    val modulo = 3
    val chordSeq = Seq(0,1,2).map(_.toLong)
    assert(F.isCanonical(modulo)(chordSeq))
  }
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
    .take(modulo)
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
