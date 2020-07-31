#! python3
# characterPictureGrid.py - Say you have a list of lists where each value in 
# the inner lists is a one-character string, like grid. You can think of 
# grid[x][y] as being the character at the x- and y-coordinates of a “picture” 
# drawn with text characters. The (0, 0) origin will be in the upper-left 
# corner, the x-coordinates increase going right, and w the y-coordinates 
# increase going down. Copy the previous grid value, and write code that uses 
# it to print the image.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()