# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:37:35 2023

@author: Chelsea Apawti
"""

import numpy as np

# Translates the list of generator matrices (3d array) from numbers to text
def genToText(genString):
    num = 0
    # Obtain the shape of the array
    [length, size, s] = np.shape(genString)
    for n in range(length):
        # Count how many generator matrices there are in the list (count nonzero matrices)
        if (genString[n][:][:] == np.zeros((size,size))).any() == True:
            num = n
            print("Number of generators:",n)
            break
    
    # Create a new list with "num" matrices (so no zero padding, which was done in the original list)
    textString = np.chararray((num, size, size))
    
    # For each matrix, translate each variable to the corresponding generator symbol
    for n in range(num):
        for i in range(size):
            for j in range(size):
                if genString[n][i][j] == 1:
                    textString[n][i][j] = 'I'
                elif genString[n][i][j] == 2:
                    textString[n][i][j] = 'X'
                elif genString[n][i][j] == 3:
                    textString[n][i][j] = 'Y'
                elif genString[n][i][j] == 4:
                    textString[n][i][j] = 'Z'
                else:
                    textString[n][i][j] = '-'
    # Print the generators
    print(textString.decode())


def main():
    matrix = np.array([[[2,1],[1,2]], [[3,1],[1,2]], [[0,0],[0,0]], [[0,0],[0,0]]])
    genToText(matrix)

if __name__ == "__main__":
    main()
    