"""number_of_islands"""
#######################
## 1. Initial: set grid, num of rows, num of cols, visit list.
## 2. checkBoundry function: return True or False.
## 3. dfs function: set visit list with recusion.
## 4. num of islands: return number of islands.
#######################

import sys

class Solution(object):

	def __init__(self, grid):
		self.grid = grid
		self.num_row = len(grid)
		print "len(grid) is %d" %self.num_row
		
		if self.num_row == 0:
			return None
		
		self.num_column = len(grid[0])
		print "len(grid[0]) is %d" %self.num_column
		
		self.visit = [[False for i in range(self.num_row)] for j in range(self.num_column)]


	def checkBoundry(self, x, y):
		if x >= 0 and x < self.num_row and y >= 0 and y < self.num_column and self.grid[x][y] and self.visit[x][y] == False:
			return True
		return False


	# Key
	def dfs(self,x,y):
		nbrow = [1,0,-1,0]
		nbcol = [0,1,0,-1]
		for k in range(4):
			new_x = x + nbrow[k]
			new_y = y + nbcol[k]
			if self.checkBoundry(new_x,new_y):
				self.visit[new_x][new_y] = True
				self.dfs(new_x,new_y)


	def numIslands(self):
		grid = self.grid
		m = self.num_row
		n = self.num_column
		
		count = 0
		
		for row in range(m):
			for col in range(n):
				if self.checkBoundry(row, col):
					self.visit[row][col] = True
					self.dfs(row,col)
					count += 1
		
		return count


if __name__ == "__main__":
	grid_1 = [[1,1,1,0,1],[0,1,0,0,0],[1,0,0,1,1],[0,0,1,0,1],[0,1,0,0,0]]
	
	grid_2 = [[1,1,1,0,1],[0,1,0,0,1],[1,0,0,1,1],[0,0,1,0,0],[0,1,0,0,1]]
	
	island = Solution(grid_1)
	print "Number of islands is: %d" %island.numIslands()
	
	sys.exit()