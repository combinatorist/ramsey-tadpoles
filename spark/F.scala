package pure

object Main {
  def main(args: Array[String]): Unit = {
    val modulo = 3
    val nodeSeq = Seq(0,1,2,0).map(_.toLong)
    val chordSeq = F.toChordSeq(modulo)(nodeSeq)
    assert(chordSeq == Seq(1,1,1))
    assert(F.lessThanSeq(Seq(1,2,3), Seq(2,3,1)))
    assert(!F.lessThanSeq(Seq(1,2,3), Seq(1,2,3)))
    assert(!F.lessThanSeq(Seq(2,3,1), Seq(1,2,3)))

    assert(!F.isCanonical(modulo)(Seq(2,3,1)))
    assert(F.isCanonical(modulo)(Seq(1,2,3)))

    // only full Canonical should catch the wrap-around case
    assert(!F.isCanonical(modulo)(Seq(1,2,1)))
    assert( F.possiblyCanonical(  Seq(1,2,1)))

    // otherwise, possibly should match
    assert(!F.possiblyCanonical(Seq(2,3,1)))
    assert(F.possiblyCanonical(Seq(1,2,3)))
  }
}

object F {
  def otherNodes(modulo: Long): IndexedSeq[Long] = otherNodes(modulo.toInt)
    .map(_.toLong)

  def otherNodes(modulo: Int) = Range(1, modulo)

  case class Partition(i: Long, of: Long) {
    def values(modulo: Long) = otherNodes(modulo)
      .filter(_ % of == i)
  }

  def possiblePaths(modulo: Long)(values: Iterator[Long]): Iterator[Seq[Long]] = values
    .flatMap(possiblePaths(modulo, _))

  def possiblePaths(modulo: Long, first: Long): Iterator[Seq[Long]] = otherNodes(modulo)
    .filterNot(_ == first)
    .permutations
    // rotating one position avoids partition skew later in isCanonical
    .map(first +: _ :+ 0L :+ first)

  def toChordSeq(modulo: Long)(wrappedCycle: Seq[Long]) = wrappedCycle
    .sliding(2)
    .map(x => (modulo + x.last - x.head) % modulo)
    .toSeq

  // assumes same length
  def lessThanSeq(a: Seq[Long], b: Seq[Long]) = a.lazyZip(b)
    .dropWhile(x => x._1 == x._2)
    .headOption
    .exists{ case(c: Long, d: Long) => c < d}

  def isCanonical(modulo: Int)(chordSeq: Seq[Long]) = !Iterator
    .continually(chordSeq)
    .flatten
    .drop(1) //don't start with the current chordSeq!
    .sliding(modulo)
    .takeWhile(_ != chordSeq)
    //.take(modulo) //safety against infite loops (depending what's fed in)
    .exists(lessThanSeq(_, chordSeq))

  def possiblyCanonical(chordPartSeq: Seq[Long]) =
    !chordPartSeq
      .tails
      .drop(1) // don't start with the current chordPartSeq!
      .exists(x => lessThanSeq(x, chordPartSeq.take(x.size)))

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
