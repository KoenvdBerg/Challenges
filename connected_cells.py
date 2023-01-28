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

# GLOBAL PARAMETERS:
PLAYERS = 2
ROWSIZE = 3
COLSIZE = 4
TOTALCELLS = ROWSIZE * COLSIZE


# FUNCTIONAL PARADIGM FUNCTIONS:
def neighbors(pos: int) -> list:
    """
    retrieves the neighbors at position pos
    """
    # below and above:
    result = [pos - COLSIZE, pos + COLSIZE]
    if pos % COLSIZE != 0:  # left
        result.append(pos - 1)
    if (pos + 1) % COLSIZE != 0:  # right
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


def walk(start_pos: int, player: int, field: list, traversed: list):
    """
    walks through the playing field from starting position
    """
    surrounding = neighbors(start_pos)
    vals = get_values(surrounding, field)
    for v, i in zip(vals, surrounding):
        if v == player and i not in traversed:
            traversed.append(i)
            walk(start_pos=i, player=player, field=field,
                 traversed=traversed)
    return traversed


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
    seen = []
    for i, player in enumerate(field):
        if i not in seen:
            traversed = walk(i, player, field, [])
            seen += traversed
            score = len(traversed)
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


# IMPERATIVE PARADIGM FUNCTIONS:
def generate_playing_field():
    """
    generates a random playing field and prints to standard out
    """
    choices = list(range(PLAYERS))
    random_field = random.choices(population=choices,
                                  k=TOTALCELLS)
    return random_field


def print_playing_field(field: list) -> None:
    """
    prints the playing field to standard out
    """
    for i in range(0, TOTALCELLS, COLSIZE):
        print([get_player_name(x) for x in field[i: i + COLSIZE]])


if __name__ == '__main__':
    playing_field = generate_playing_field()
    print_playing_field(playing_field)
    final_scores = final_score(field=playing_field)
    print(determine_winner(final_scores))
