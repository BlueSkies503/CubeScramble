# Create a Rubik's Cube Scramble Generator
# Scramble should be 25 moves long
# Scramble should not have moves that make previous moves redundant
# Example: R, Ri or R2


from random import randint

# all possible moves on a Rubik's Cube

list = ['U', 'Ui', 'U2', 'F', 'Fi', 'F2', 'R', 'Ri', 'R2', 'B', 'Bi', 'B2',
    'L', 'Li', 'L2', 'D', 'Di', 'D2']

# shuffle those moves


def generate_random_moves(num_moves):
    moves = []
    for move in xrange(num_moves):
        moves.append(list[randint(0, len(list)) - 1])
    return moves


# print shuffled list
print generate_random_moves(4)
