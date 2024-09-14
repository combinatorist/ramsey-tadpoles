package pure
import scala.util.Random

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
    assert(F.toCanonical(modulo)(Seq(2, 3, 1)) == Seq(1, 2, 3))
  }
}

object F {
  def factorial(n: Int): Int = n match {
    case 1 => 1
    case x => x * factorial(x - 1)
  }

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

  def toCanonical(modulo: Int)(chordSeq: Seq[Int]) =
    Iterator
      .continually(chordSeq)
      .flatten
      .sliding(modulo)
      .drop(1)
      .takeWhile(_ != chordSeq)
      // .take(modulo) //safety against infite loops (depending what's fed in)
      .fold(chordSeq)((a, b) => if (lessThanSeq(a, b)) a else b)

  def shuffleN(modulo: Int)(n: Int, seed: Int) = {
    Random.setSeed(seed)
    val nodeSeq = Range(0, modulo)
    (0 until n)
      .map { i =>
        Record(
          seed,
          i,
          {
            val shuffled = Random.shuffle(nodeSeq)
            val chordSeq = toChordSeq(modulo)(shuffled :+ shuffled.head)
            toCanonical(modulo)(chordSeq)
           }
        )
      }
  }
}
final case class Record(partitionSeed: Int, i: Int, chordSeq: Seq[Int])
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
