# Create a Rubik's Cube Scramble Generator
# Scramble should be 25 moves long
# Scramble should not have moves that make previous moves redundant
# ^Example: R, Ri or R2, Ri (R2 + Ri = R)
# Here is what end result should look like:
# B2  D  R'  U'  F'  R  U'  B  R  B'  R2  L  D2  U2  B  R'  U'  R  B2  F  D'  F  D  F2  U'

from random import choice

# all possible moves on a Rubik's Cube
CUBE_TURNS = ['U', 'Ui', 'U2', 'F', 'Fi', 'F2', 'R', 'Ri', 'R2', 'B',
              'Bi', 'B2', 'L', 'Li', 'L2', 'D', 'Di', 'D2']

# shuffle those moves


def generate_random_moves(num_moves):
    moves = []
    for move in xrange(num_moves):
        moves.append(choice(CUBE_TURNS))
    return moves


# print shuffled list
print generate_random_moves(4)
