#  File: WordSearch.py

#  Description: A program that finds the first position of the first letter of a word in a word search. The word
# can either be horizontal, vertical, or diagonal in either the left or right direction, up or down directions.

#  Student Name: Phillip Gavino

#  Student UT EID: pag2529

#  Partner Name: Jack Qiao

#  Partner UT EID: jq3838

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 8/28/2021

#  Date Last Modified: 8/30/2021

import sys


# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
    number_index = 0
    lines = sys.stdin.readlines()
    n = int(lines[0])
    grid = [[" " for k in range(n)] for l in range(n)]  # creates matrix

    # goes through read lines and replaces \n with blank and then checks where the second number's index is
    for x in range(len(lines)):
        lines[x] = lines[x].replace("\n", "")
        if (lines[x].isnumeric()):
            number_index = x

    word_list = lines[number_index + 1:]  # slices the read lines list from the number index + 1 to make the word_list
    chars = lines[2:number_index - 1]  # slices the read lines list from the third index to the number index minus
    # 1

    for y in range(len(chars)):  # replaces the spaces in the characters list to blank
        chars[y] = chars[y].replace(" ", "")

    # creates a grid from the characters characters list
    for i in range(n):
        for j in range(n):
            grid[i][j] = chars[i][j]
    return grid, word_list


# the right horizontal direction check method
def horizontal_right(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):  # if the grid cell is not equal to one of the word's characters then return false
            return False
        c += 1  # else add 1 to column
        if (c >= len(grid) and i != len(word) - 1):  # if the integer is greater than the grid's number of columns, and
            # the ith value of word is not equal to the last index of word, then return false
            return False
    return True  # if it doesn't return false at either checks, return true


# the left horizontal direction check method
def horizontal_left(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c -= 1  # subtract column by 1
        if (c == -1 and i != len(word) - 1):  # if column is equal to -1 and other boolean expression then return false
            return False
    return True


# vertical up direction check method
def vertical_up(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        r -= 1  # subtract row by 1
        if (r == -1 and i != len(word) - 1):
            return False
    return True


def vertical_down(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        r += 1  # add 1 to row
        if (r >= len(grid) and i != len(word) - 1):
            return False
    return True


def diagonal_up_right(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c += 1  # add 1 to column
        r -= 1  # subtract 1 from row
        if ((c >= len(grid) or r == -1) and i != len(word) - 1):
            return False
    return True


def diagonal_up_left(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c -= 1  # subtract 1 from column
        r -= 1  # subtract 1 from row
        if ((c == -1 or r == -1) and i != len(word) - 1):
            return False
    return True


def diagonal_down_right(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c += 1  # add 1 to column
        r += 1  # add 1 to row
        if ((c >= len(grid) or r >= len(grid)) and i != len(word) - 1):
            return False
    return True


def diagonal_down_left(grid, r, c, word):
    for i in range(len(word)):
        if (grid[r][c] != word[i]):
            return False
        c -= 1  # subtract 1 from column
        r += 1  # add 1 to row
        if ((c == -1 or r >= len(grid)) and i != len(word) - 1):
            return False
    return True


def find_word(grid, word):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == word[0]):  # if the grid cell is equal to the first character in the word
                if (horizontal_right(grid, i, j, word)  # then goes through a boolean statement to check if the word 
                        # goes in a straight line in one of the directions
                        or horizontal_left(grid, i, j, word)
                        or vertical_up(grid, i, j, word)
                        or vertical_down(grid, i, j, word)
                        or diagonal_down_left(grid, i, j, word)
                        or diagonal_up_left(grid, i, j, word)
                        or diagonal_up_right(grid, i, j, word)
                        or diagonal_down_right(grid, i, j, word)):
                    return (i + 1, j + 1)  # if true return the coordinate position
    return (0, 0)  # else return (0, 0)


def main():
    # read the input file from stdin
    # find each word and print its location
    word_grid, word_list = read_input()
    for word in word_list:
        location = find_word(word_grid, word)
        print(word + ": " + str(location))


if __name__ == "__main__":
    main()

