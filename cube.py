"""
Author: Koen van den Berg
Description: Creates a cube of N size and finds subcubes of n size
"""

# Imports
import random


# Definitions
class Cube():
    """A cube is a NxN matrice with random 0 and 1 values
    """
    
    def __init__(self, N):
        """Initialization function
        """
        self.cube = self._createCubeData(N)
        self.cubeSize = N
        self.transposed_cube = self._transposeCube()
        self.largestSubCube = {}
    
    def _createCubeData(self, N):
        """Creates the cube of size N
        N: int, height and width of cube
        """
        cube = []
        for x in range(N):
            cube_row = []
            for y in range(N):
                randnumber = random.randint(0,1)
                cube_row.append(randnumber)
            cube.append(cube_row)
        return(cube)

    def _transposeCube(self):
        """Transposes the cube
        """
        t_cube = []
        for x in range(len(self.cube)):
            cube_row = []
            for y in range(len(self.cube)):
                t_value = self.cube[y][x]
                cube_row.append(t_value)
            t_cube.append(cube_row)
        return(t_cube)

    def printCube(self):
        """Prints the cube nicely
        """
        print('This is the cube\n------------------------------')
        for row in self.cube:
            for j in row:
                print(f'{j}', end='')
            print()
        print('\nThis is the transposed cube\n------------------------------')
        for row in self.transposed_cube:
            for j in row:
                print(f'{j}', end='')
            print()
        
    def findSubCube(self):
        """Finds largest subcube of 1s in the cube
        """
        subCubeLoc = []
        subCubeSize = 0
        isSearching = False

        for x in range(len(self.cube)):
            for y in range(len(self.cube[x])):
                if self.cube[x][y] == 1:
                    this_size = 1
                    isSearching = True
                    while isSearching == True:
                        try:
                            next_part = self.cube[x+this_size][y:y+this_size+1]
                            next_part_transpose = self.transposed_cube[y+this_size][x:x+this_size+1]
                            if next_part == [1 for i in range(this_size+1)] and next_part_transpose == [1 for i in range(this_size+1)]:
                                this_size += 1
                                isSearching = True
                                if this_size > subCubeSize:
                                    subCubeSize = this_size
                                    subCubeLoc = [x,y]
                            else:
                                isSearching = False
                        except(IndexError):
                            isSearching = False
        self.largestSubCube["Size"] = subCubeSize
        self.largestSubCube["Loc"] = subCubeLoc

if __name__=="__main__":
    test = Cube(50)
    test.printCube()
    test.findSubCube()
    print(test.largestSubCube)
