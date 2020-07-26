

# Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string
#  provided.
#
# Letter Value
# A, E, I, O, U, L, N, R, S, T 1
# D, G 2
# B, C, M, P 3
# F, H, V, W, Y 4
# K 5
# J, X 8
# Q, Z 10

one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
two_point = ["D", "G"]
three_point = ["B", "C", "M", "P"]
four_point = ["F", "H", "V", "W", "Y"]
five_point = ["K"]
eight_point = ["J", "X"]
ten_point = ["Q", "Z"]


def scrabble_count(word):

    score = 0

    for letter in word:

        if letter in one_point:
            score += 1
        elif letter in two_point:
            score += 2
        elif letter in three_point:
            score += 3
        elif letter in four_point:
            score += 4
        elif letter in five_point:
            score += 5
        elif letter in eight_point:
            score += 8
        elif letter in ten_point:
            score += 10
    return score

print(scrabble_count("DANIEL"))

# Note that this scrabble calculator will only take uppercase letters use LOWER to allow for lower case letters




