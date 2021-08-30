#  File: WordSearch.py

#  Description: A program that finds the first position of the first letter of a word in a word search. The word
# can either be horizontal, vertical, or diagonal in either the left or right direction.

#  Student Name: Phillip Gavino

#  Student UT EID: pag2529

#  Partner Name: Jack Qiao

#  Partner UT EID: jq3838

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 8/28/2021

#  Date Last Modified: 8/29/2021

import sys


# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
    number_index = 0
    lines = sys.stdin.readlines()
    n = int(lines[0])
    grid = [[" " for k in range(n)] for l in range(n)]  # creates matrix

    for x in range(len(lines)):
        lines[x] = lines[x].replace("\n", "")
        if (lines[x].isnumeric()):
            number_index = x

    word_list = lines[number_index + 1:]
    chars = lines[2:number_index - 1]

    for y in range(len(chars)):
        chars[y] = chars[y].replace(" ", "")

    for i in range(n):
        for j in range(n):
            grid[i][j] = chars[i][j]
    return grid, word_list


def horizontal_right(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c += 1
        if (c >= len(grid) and i != len(word) - 1):
            return False
    return True


def horizontal_left(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c -= 1
        if (c == -1 and i != len(word) - 1):
            return False
    return True


def vertical_up(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        r -= 1
        if (c == -1 and i != len(word) - 1):
            return False
    return True


def vertical_down(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        r += 1
        if (r >= len(grid) and i != len(word) - 1):
            return False
    return True


def diagonal_up_right(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c += 1
        r -= 1
        if ((c >= len(grid) or r == -1) and i != len(word) - 1):
            return False
    return True


def diagonal_up_left(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c -= 1
        r -= 1
        if ((c == -1 or r == -1) and i != len(word) - 1):
            return False
    return True


def diagonal_down_right(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c += 1
        r += 1
        if ((c >= len(grid) or r >= len(grid)) and i != len(word) - 1):
            return False
    return True


def diagonal_down_left(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c -= 1
        r += 1
        if ((c == -1 or r >= len(grid)) and i != len(word) - 1):
            return False
    return True


def find_word(grid, word):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == word[0]):
                if (horizontal_right(grid, i, j, word)
                        or horizontal_left(grid, i, j, word)
                        or vertical_up(grid, i, j, word)
                        or vertical_down(grid, i, j, word)
                        or diagonal_down_left(grid, i, j, word)
                        or diagonal_up_left(grid, i, j, word)
                        or diagonal_up_right(grid, i, j, word)
                        or diagonal_down_right(grid, i, j, word)):
                    return (i+1, j+1)
    return(0, 0)


def main():
    # read the input file from stdin
    # find each word and print its location
    word_grid, word_list = read_input()
    for word in word_list:
        location = find_word(word_grid, word)
        print(word + ": " + str(location))


if __name__ == "__main__":
    main()
