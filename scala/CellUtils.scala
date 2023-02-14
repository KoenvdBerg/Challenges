package connected.cells

import scala.collection.mutable.ListBuffer
import scala.collection.mutable.ArrayBuffer
import scala.collection.mutable.Map
import scala.util.Random

object CellUtils:
  val players = 2
  val rowsize = 5
  val colsize = 5
  val totalcells = rowsize * colsize

  /**
   * find the neighbors for a position in a field
   * @param pos an index in the field
   * @return
   */
  private def neighbors(pos: Int): List[Int] =
    val nbr = new ListBuffer[Int]
    nbr += pos - colsize
    nbr += pos + colsize
    if pos % colsize != 0 then
      nbr += pos - 1
    if (pos + 1) % colsize != 0 then
      nbr += pos + 1
    nbr.toList.filter(x => 0 <= x).filter(x => x < totalcells)

  /**
   * walks over the playing field
   * @param startPos = start position to walk from
   * @param player = player to walk for
   * @param field = the field to walk over
   * @param traversed = indices that have been walked over already
   * @return
   */
  def walk(startPos: Int, player: Int, field: IndexedSeq[Int], traversed: ArrayBuffer[Int]): ArrayBuffer[Int] =
    val nbrs = neighbors(startPos)
    for
      pos <- nbrs
    do
      if player == field(pos) & !traversed.contains(pos) then
        traversed += pos
        walk(pos, player, field, traversed)
    traversed

  /**
   * computes the final score based on a playing field
   * @param field = the playing field
   * @return
   */
  def finalScore(field: IndexedSeq[Int]): ArrayBuffer[Int] =
    val scores = (for i <- 0 until players yield 0).to(ArrayBuffer)
    val seen = new ArrayBuffer[Int]
    for
      i <- field.indices
    do
      if !seen.contains(i) then
        val player = field(i)
        val connected = walk(i, player, field, new ArrayBuffer[Int])
        for i <- connected do seen += i
        val score = connected.length
        if score > scores(player) then
          scores(player) = score
    scores

  /**
   * determines the winner based on the scores
   * @param scores
   */
  def determineWinner(scores: ArrayBuffer[Int]): Unit =
    val winner = scores.indexOf(scores.max)
    println(s"The winner is ${getPlayerName(winner)} with a total score of ${scores(winner)}")

  /**
   * generates a playing field
   */
  def generatePlayingField(r: Random): IndexedSeq[Int] =
    for i <- 0 until totalcells yield r.nextInt(players)

  /**
   * obtains the player name in alphabetical representation
   */
  def getPlayerName(player: Int): Character =
    val playerchar = 97 + player
    playerchar.toChar

  /**
   * prints the playing field to the console
   */
  def printPlayingfield(field: IndexedSeq[Int]): Unit =
    println("\n === PLAYING FIELD ===")
    for i <- 0 until totalcells by colsize do
      for v <- field.slice(i, i + colsize) do
        print(s"${getPlayerName(v)} ")
      print("\n")

