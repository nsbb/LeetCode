class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result=0
        len_i=len(grid); len_j=len(grid[0])
        for i in range(len_i):
            for j in range(len_j):
                if i==0 and j==0:                   #top left edge
                    if grid[i][j] == 1:
                        result+=2
                    if grid[i][j] != grid[i][j+1]:
                        result+=1
                    if grid[i][j] != grid[i+1][j]:
                        result+=1
                elif i==0 and j!=0:                 #top edge
                    if grid[i][j] == 1:
                        result+=1
                    if grid[i][j] != grid[i][j+1]:
                        result+=1
                    if grid[i][j] != grid[i+1][j]:
                        result+=1
                elif i==0 and j==(len_j-1):         #top rirght edge
                    if grid[i][j] == 1:
                        result+=2
                    if grid[i][j] != grid[i+1][j]:
                        result+=1
                elif j==0:                         #left edge
                    if grid[i][j] == 1:
                        result+=1
                    if grid[i][j] != grid[i][j+1]:
                        result+=1
                    if grid[i][j] != grid[i+1][j]:
                        result+=1
                elif i==(len_i-1) and j==0:         #bottom left edge
                    if grid[i][j] == 1:
                        result+=2
                    if grid[i][j] != grid[i][j+1]:
                        result+=1
                elif i==(len_i-1):                 #bottome edge                
                    if grid[i][j] == 1:
                        result+=1
                    if grid[i][j] != grid[i][j+1]:
                        result+=1
                elif i==(len_i-1) and j==(len_j-1): #bottom right edge
                    if grid[i][j] == 1:
                        reseult += 2
                elif j==(len_j-1):                 #right edge
                    if grid[i][j] == 1:
                        result+=1
                    if grid[i][j] != grid[i+1][j]:
                        result+=1                    
                else:
                    if grid[i][j] != grid[i][j+1]:
                        result+=1
                    if grid[i][j] != grid[i+1][j]:
                        result+=1
            return result
