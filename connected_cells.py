"""
Code challenge: find the winning player
By: Koen van den Berg

The problem that is presented in this script is as follows: an N amount of
players is positioned in a field of X columns and Y rows. Given such a random
field, can you find the player that occupies the most consecutive cells in
that field?

Rules:
1- a cell is considered a neighbor only if the cell is above, below,
right or left from the player. No diagonal neighbors are allowed.
2- the winner is the player with the most consecutive occupied cells.
3- in case of a tie, the player that started the game is the winner. In our
case that is player A.

+-----+-----+-----+-----+
|A    |A    |A    |B    |
+-----+-----+-----+-----+
|A    |A    |A    |B    |
+-----+-----+-----+-----+
|B    |A    |B    |B    |
+-----+-----+-----+-----+

Result:
A: 7
B: 4

The winner is player A with 7 cells
"""
import random

PLAYERS = 2
ROWSIZE = 3
COLSIZE = 4
TOTALCELLS = ROWSIZE * COLSIZE


def neighbors(pos: int) -> list:
    """
    retrieves the neighbors at position pos
    """
    # below and above:
    result = [pos - ROWSIZE, pos + ROWSIZE]
    if pos % ROWSIZE != 0:  # left
        result.append(pos - 1)
    if (pos + 1) % ROWSIZE != 0:  # right
        result.append(pos + 1)
    result = [i for i in result
              if 0 <= i < TOTALCELLS]
    return result


def get_values(positions: list, field: list) -> list:
    """
    gets the values at certain positions
    """
    values = [field[l] for l in positions]
    return values


def walk(start_pos: int, start_val: int, field: list,
         traversed: list = [], acc: int = 0):
    """
    steps through the grid from starting position
    """
    surrounding = neighbors(start_pos)
    vals = get_values(surrounding, field)
    for v, i in zip(vals, surrounding):
        if v == start_val and i not in traversed:
            traversed.append(i)
            acc = walk(start_pos=i, start_val=start_val, field=field,
                       traversed=traversed, acc=acc + 1)
    return acc


def get_player_name(player: int) -> str:
    """
    retrieves the name of the player in alphabetical representation
    """
    return chr(97 + player)


def final_score(field: list) -> dict:
    """
    retrieves the final score for a playing field
    """
    scores = {i: 0 for i in range(0, PLAYERS)}
    for i in range(0, TOTALCELLS):
        player = get_values([i], field)[0]
        score = walk(i, player, field)
        if score > scores[player]:
            scores[player] = score
    return scores


def determine_winner(scores: dict) -> str:
    """
    determines the winner of the game
    """
    totals = list(scores.values())
    players = list(scores.keys())
    winner = players[totals.index(max(totals))]
    return f'The winner is {get_player_name(winner)} with {scores[winner]} ' \
           f'cells'


def generate_field():
    """
    generates a random playing field and prints to standard out
    """
    random_field = [random.choice([i for i in range(PLAYERS)])
                    for i in range(TOTALCELLS)]
    for i in range(0, len(random_field), ROWSIZE):
        print([get_player_name(x) for x in random_field[i: i + ROWSIZE]])
    return random_field


if __name__ == '__main__':
    playing_field = generate_field()
    final_scores = final_score(field=playing_field)
    print(determine_winner(final_scores))
