object Main {
  case class Partition(subModulo: Int)(value: Int)
  case class Path(stops: Seq[Int], chords: Seq[Int])
  def possiblePaths(modulo: Int): IndexedSeq[Seq[Int]] = {
    val otherNodes = Range(1, modulo)
    otherNodes.flatMap(possiblePaths(modulo, _))
  }

  def possiblePaths(modulo: Int, partition: Partition): Iterator[Seq[Int]] =
    ???

  def possiblePaths(modulo: Int, first: Int): Iterator[Seq[Int]] = {
    val otherNodes = Range(1, modulo).filterNot( _ == first)
    Range(1, modulo).permutations.map(first +: _ :+ 0)
  }
}
