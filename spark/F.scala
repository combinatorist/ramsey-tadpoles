package pure

object Main {
  def main(args: Array[String]): Unit = {
    val modulo = 3
    val nodeSeq = Seq(0,1,2,0).map(_.toLong)
    val chordSeq = F.toChordSeq(modulo)(nodeSeq)
    println(chordSeq)
    assert(chordSeq == Seq(1,1,1))
    /*
    assert(F.lessThanSeq(Seq(0,1,2), Seq(1,2,0)))
    assert(!F.lessThanSeq(Seq(0,1,2), Seq(0,1,2)))
    assert(!F.lessThanSeq(Seq(1,2,0), Seq(0,1,2)))
    */
    assert(!F.isCanonical(modulo)(Seq(1,2,0)))
    assert(F.isCanonical(modulo)(Seq(0,1,2)))
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
    .map(0L +: first +: _ :+ 0)

  def toChordSeq(modulo: Long)(wrappedCycle: Seq[Long]) = wrappedCycle
    .sliding(2)
    .map(x => (modulo + x.last - x.head) % modulo)
    .toSeq

  // assumes same length
  def lessThanSeq(a: Seq[Long], b: Seq[Long]) = {
    println(a, b)
    val soFar = a.lazyZip(b)
    .dropWhile(x => x._1 == x._2)
    println(soFar.toSeq)
    soFar
    .toIterator
    .nextOption
    .exists{ case(c: Long,d: Long) => println(c,d); c < d}
  }

  def isCanonical(modulo: Int)(chordSeq: Seq[Long]) = {
   val soFar = Iterator
    .continually(chordSeq)
    .flatten
    .drop(1) //don't start with the current chordSeq!
    .sliding(modulo)
    .map(_.toSeq)
    .takeWhile(_ != chordSeq)
    .take(modulo)
    .toSeq

  println(soFar)

   !soFar
    .exists(lessThanSeq(_, chordSeq))

  }
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
