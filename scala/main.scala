/**
 * Code challenge: find the winning player
 * By: Koen van den Berg
 *
 * The article that describes the code in this script can be found here:
 * https://medium.com/@k.vandenberg/learn-functional-programming-in-python-with-this-coding-challenge-e3d4fb5d4978
 *
 * The problem that is presented in this script is as follows: an N amount of
 * players is positioned in a field of X columns and Y rows. Given such a random
 * field, can you find the player that occupies the most consecutive cells in that field?
 *
 * Rules:
 * 1- a cell is considered a neighbor only if the cell is above, below,
 * right or left from the player. No diagonal neighbors are allowed.
 * 2- the winner is the player with the most consecutive occupied cells.
 * 3- in case of a tie, the player that started the game is the winner. In our
 * case that is player A.
 *
 * +-----+-----+-----+-----+
 * |A    |A    |A    |B    |
 * +-----+-----+-----+-----+
 * |A    |A    |A    |B    |
 * +-----+-----+-----+-----+
 * |B    |A    |B    |B    |
 * +-----+-----+-----+-----+
 *
 * Result:
 * A: 7
 * B: 4
 * The winner is player A with 7 cells
 */
package connected.cells

import scala.util.Random
import CellUtils.*

import scala.collection.mutable.ArrayBuffer


@main def run(): Unit =
  val r = new Random()
  val field = generatePlayingField(r)
  printPlayingfield(field)

  val playerscores = finalScore(field)
  print(determineWinner(playerscores))
