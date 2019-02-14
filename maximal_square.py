#! usr/bin/env python 3

# imports:
import random

# Definitions:
class MaximumSquare(object):

    def __init__(self, ArrSize = 10):
        """
        This initializes the random square and its transposon.
        ArrSize = the size of the random array (default 10)
        self.Arr = the random array
        self.transposeArr = the transposed random array
        self.LargestArr = the initial largest square in the array
        """
        self.Arr = ["".join(random.choice("01") for i in range(0,ArrSize)) for y in range(0,ArrSize)]
        #["1111","1110","1111","0000"]
        
        self.transposeArr = list("".join(i) for i in zip(*self.Arr))
        self.LargestArr = 0

        
    def FindMaximum(self):
        """
        Finds the largest square in the random matrix. This works by utilizing the random array and its transposon. If there is a "1" in the random array the "square" becomes true. The square can be found using the transposed array, in which the coordinates for i and e are reversed (i=e and e=i). 
        square = false/true
        maxArr = largest possible array in one square run
        square_x = integer for some random found square in square run
        squares = list that stores largest squares
        """
        square = False
        maxArr = 0
        square_x = 0
        squares = []
        for i in range(len(self.Arr)):
            for e in range(len(self.Arr[i])):
                if self.Arr[i][e] == "1":
                    square = True
                if square:
                    try:
                        for y in range(len(self.Arr)):
                            if self.Arr[i][e+y] == "1":
                                square_x += 1
                                if self.Arr[i+y][e:e+square_x] == "1" * square_x and self.transposeArr[e+y][i:i+square_x] == "1" * square_x:
                                    maxArr += 1
                                    squares.append(maxArr**2)
                            else:
                                maxArr = 0
                                square_x = 0
                                square = False
                                                             
                    except IndexError:
                        square = False
                        maxArr = 0
                        square_x = 0
        self.LargestArr = max(squares)
                        
    def PrintResults(self):
        """
        Prints the results
        """
        print("\n")
        for item in self.Arr:
            print("{}".format(item))
        print("the transposed matrix is:")
        print("The size of the array is: {}".format(len(self.Arr)))
        print("The largest square in the array is: {}".format(self.LargestArr))

if __name__ == "__main__":
    ByteArr = MaximumSquare(20)
    ByteArr.FindMaximum()
    ByteArr.PrintResults()
