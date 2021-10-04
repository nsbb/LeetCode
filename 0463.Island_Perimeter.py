class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result=0
        len_i=len(grid); len_j=len(grid[0])
        
        # add 0 on the border around.
        zeros=[0]*(len_j+2)
        grid.insert(0,zeros)   # top
        grid.append(zeros)     # bottom
        for row in grid:
            row.insert(0,0)    # left
            row.append(0)      # right
            
        # calculate the perimeter.
        for i in range(len_i+1):
            for j in range(len_j+1):
                if grid[i][j] != grid[i][j+1]:
                    result+=1
                if grid[i][j] != grid[i+1][j]:
                    result+=1
        return result
