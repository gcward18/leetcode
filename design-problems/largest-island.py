'''
🔍 Problem: Largest Island in a Grid (Graph / DFS / Union-Find)
Scenario:
You are given an m x n binary grid where 1 represents land and 0 represents water. An island is a group of 1s connected horizontally or vertically (not diagonally).

Question:
Return the size (number of cells) of the largest island in the grid.

🧾 Example:
Input:

python
Copy
Edit
grid = [
  [0, 0, 1, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 0, 0, 1]
]
Output:

python
Copy
Edit
5
Explanation:
The central island (connected 1s) has a size of 5, which is the largest.

✅ Constraints:
1 <= m, n <= 1000

You can mutate the input grid or use a visited set

Expected time complexity: O(m * n)

'''

def max_island_size(matrix: list[list[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    count = 0
    
    def dfs(row: int, col: int, ):
        # check if we can look at this spot
        if 0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] == 1:
            # flip bit so we don't visit again
            matrix[row][col] = 0
            
            # check 4 cardinal directions
            return dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1) + 1
        
        return 0
            
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == 1:
                count = max(count, dfs(row, col))
    
    return count
          
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]
    ]
    assert max_island_size(grid) == 5
