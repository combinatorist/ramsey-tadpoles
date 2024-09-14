package pure

object Main {
  def main(args: Array[String]): Unit = {
    val modulo = 3
    val nodeSeq = Seq(0, 1, 2, 0).map(_.toInt)
    val chordSeq = F.toChordSeq(modulo)(nodeSeq)
    assert(chordSeq == Seq(1, 1, 1))
    assert(F.lessThanSeq(Seq(1, 2, 3), Seq(2, 3, 1)))
    assert(!F.lessThanSeq(Seq(1, 2, 3), Seq(1, 2, 3)))
    assert(!F.lessThanSeq(Seq(2, 3, 1), Seq(1, 2, 3)))
    assert(!F.isCanonical(modulo)(Seq(2, 3, 1)))
    assert(F.isCanonical(modulo)(Seq(1, 2, 3)))
  }
}

object F {
  def otherNodes(modulo: Int): IndexedSeq[Int] = Range(1, modulo).map(_.toInt)

  case class Partition(i: Int, of: Int) {
    def values(modulo: Int) =
      otherNodes(modulo)
        .filter(_ % of == i)
  }

  def possiblePaths(modulo: Int)(values: Iterator[Int]): Iterator[Seq[Int]] =
    values
      .flatMap(possiblePaths(modulo, _))

  def possiblePaths(modulo: Int, first: Int): Iterator[Seq[Int]] =
    otherNodes(modulo)
      .filterNot(_ == first)
      .permutations
      // rotating one position avoids partition skew later in isCanonical
      .map(first +: _ :+ 0 :+ first)

  def toChordSeq(modulo: Int)(wrappedCycle: Seq[Int]) =
    wrappedCycle
      .sliding(2)
      .map(x => (modulo + x.last - x.head) % modulo)
      .toSeq

  // assumes same length
  def lessThanSeq(a: Seq[Int], b: Seq[Int]) =
    a
      .lazyZip(b)
      .dropWhile(x => x._1 == x._2)
      .headOption
      .exists { case (c: Int, d: Int) => c < d }

  def isCanonical(modulo: Int)(chordSeq: Seq[Int]) =
    !Iterator
      .continually(chordSeq)
      .flatten
      .drop(1) // don't start with the current chordSeq!
      .sliding(modulo)
      .takeWhile(_ != chordSeq)
      // .take(modulo) //safety against infite loops (depending what's fed in)
      .exists(lessThanSeq(_, chordSeq))

}

/*
object SeqOrdering extends Ordering[Seq[Int]] {
  // assumes same length
  def compare(a: Seq[Int], b: Seq[Int]) = {
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
