import scala.collection.mutable.ListBuffer

def residues(modulo: Int)(generator: Int) = {
  var residues = ListBuffer(generator)

  Seq(1).toIterator
    .++(Iterator.continually(generator))
    .map(residues.head * _ % modulo)
    .takeWhile(!residues.tail.contains(_))
    .map { x => x +=: residues; x }
    .toSet

}

def coprimes(modulo: Int) = {
  val divisors = Range(2, modulo)
    .filter(modulo % _ == 0)
  Range(1, modulo)
    .filterNot(x => divisors.exists(x % _ == 0))
}

def areCoprime(s: Set[Int]) = ???

def sets(modulo: Int) = Range(1, modulo).toSet.subsets

def generatedSets(modulo: Int) = coprimes(modulo).map(residues(modulo)).toSet

var filters: Seq[(Set[Int], Int) => Boolean] = Seq()
filters :+ ((x: Set[Int], y: Int) => x != Set())

def combinedChords(modulo: Int, generator: Int)(chordCycle: Seq[Long]) = {
  Iterator
    .continually(chordCycle)
    .flatten
    .sliding(generator)
    .take(modulo)
    .map(_.reduce(_ + _) % modulo)
    .toSet
}

def coveredGenerators(generatedSets: Set[Set[Int]], modulo: Int)(
    s: Seq[Long]
) = {
  generatedSets
    .filterNot(g => s.exists(s => !g.exists(_ == s)))
    .map(g => (g -> combinedChords(modulo, g.head)(s)))
    .toMap
}

def cg(modulo: Int) = (() => coveredGenerators(generatedSets(modulo), modulo))

def modDf(modulo: Int) =
  spark.read.load(s"data/df-overwritten-mod-$modulo").cache

def summary(modulo: Int) = modDf(modulo)
  .as[Seq[Long]]
  .flatMap(cg(modulo)(_).toSeq)
  .groupByKey(_._1)
  .mapValues(_._2)
  .reduceGroups(_ union _)
  .show(false)
