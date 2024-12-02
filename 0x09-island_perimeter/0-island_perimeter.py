#!/usr/bin/python3
'''Island perimeter'''


def island_perimeter(grid):
    '''Computes the perimeter of an island with no lakes'''
    
    total_perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                cell_perimeter = 4

                if row > 0 and grid[row - 1][col] == 1:
                    cell_perimeter -= 2

                if col > 0 and grid[row][col - 1] == 1:
                    cell_perimeter -= 2

                total_perimeter += cell_perimeter

    return total_perimeter