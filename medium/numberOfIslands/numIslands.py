
def numIslands( grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0 
    def mybfs(i,j):
        nonlocal grid

        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0"):
            return 
        #mark as visited 
        grid[i][j] = "0"
        #adjacent island
        mybfs(i-1,j) #up
        mybfs(i+1,j) #down
        mybfs(i,j-1) #left
        mybfs(i,j+1) #right
        
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                print(grid[i],grid[i][j])
                count += 1
                mybfs(i,j)
    print(count)
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(grid)
print(numIslands(grid))
    
    
    