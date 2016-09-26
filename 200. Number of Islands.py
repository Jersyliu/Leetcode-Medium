class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == [] or len(grid[0]) == 0:
            return 0
        length = len(grid)
        width = len(grid[0])
        number = 0
        for i in xrange(length):
            for j in xrange(width):
                if grid[i][j] == "1":
                    self.explore(grid,length,width,i,j)
                    number += 1
        return number
        
    def explore(self,grid,length,width,i,j):
        if i < 0 or i == length or j < 0 or j == width:
            return
        if grid[i][j] == "0" or grid[i][j] == "2":
            return
        grid[i][j] = "2"
        self.explore(grid,length,width,i,j-1)
        self.explore(grid,length,width,i,j+1)
        self.explore(grid,length,width,i-1,j)
        self.explore(grid,length,width,i+1,j)
        
        
        