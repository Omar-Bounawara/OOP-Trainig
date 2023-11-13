"""
Author: Omar-Bounawara


Problem:(modified version of a problem from hackerRank)
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
Neo reads the column from top to bottom and starts reading from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them
with a single space '' for better readability.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Example:
Initialized Script:

This$#is% Matrix#  %!

Decoded Output:
This is Matrix#  %!
"""



# Importing the necessary module for generating random numbers
from random import randrange

# Class definition for the Neo Matrix
class neo_matrix:
    # Constructor to initialize the matrix with specified dimensions
    def __init__(self, row_size: int, column_size: int):
        # Initializing the matrix with empty strings
        self.matrix = [['' for _ in range(column_size)] for _ in range(row_size)]
        # Storing the dimensions of the matrix
        self.row_size = row_size
        self.column_size = column_size

    # String representation of the matrix for printing
    def __repr__(self):
        res = ""
        for row in self.matrix:
            ch = ""
            for element in row:
                ch += element + " "
            res += ch + "\n"
        return res

    # Iterator initialization for matrix traversal
    def __iter__(self):
        # Initializing the current row and column for iteration
        self.current_row = 0
        self.current_column = 0
        return self

    # Iterator method for obtaining the next element during iteration
    def __next__(self):
        if self.current_column < self.column_size:
            element = self.matrix[self.current_row][self.current_column]

            if self.current_row == self.row_size - 1:
                self.current_row = 0
                self.current_column += 1
            else:
                self.current_row += 1

            return element
        else:
            # StopIteration is raised when the end of iteration is reached
            raise StopIteration

    # Method to retrieve a specific element in the matrix
    def element(self, row, column):
        return self.matrix[row][column]

    # Method to initialize the matrix with a given script
    def init_script(self, script):
        pointer = 0
        for column in range(self.column_size):
            for row in range(self.row_size):
                self.matrix[row][column] = script[pointer]
                pointer += 1

    # Method to initialize the matrix with random alphanumeric characters
    def random_script(self):
        for row in range(self.row_size):
            for column in range(self.column_size):
                self.matrix[row][column] = chr(randrange(65, 130))

    # Method to find the position of a target character in the matrix
    def find(self, target):
        for element in self:
            if element == target:
                return self.current_row, self.current_column

    # Method to decode the matrix script as per Neo's instructions
    def decode(self):
        script = ""
        for character in self:
            if character.isalnum():
                script += character
            else:
                sub_script = character

                while not character.isalnum():
                    try:
                        character = self.__next__()
                        sub_script += character

                    except StopIteration:
                        script += sub_script
                        break
                if character.isalnum():
                    script += " " + character

        return script

# Example usage of the neo_matrix class
m = neo_matrix(7, 3)
# Initializing the matrix with a specific script
m.init_script("This$#is% Matrix#  %!")
# Printing the matrix
print(m)

# Decoding and printing the script
print(m.decode())
