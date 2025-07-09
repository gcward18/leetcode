'''
🔄 Follow-Up Problem: Flip One Water Cell to Land
Scenario Extension:
Given the same m x n grid of 0s and 1s (water and land), you are now allowed to flip at most one 0 to 1.

Question:
What is the maximum possible island size you can obtain after flipping exactly one water cell to land?

🧾 Example:
Input:

python
Copy
Edit
grid = [
  [0, 0, 1, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 0, 1, 1]
]
Output:

python
Copy
Edit
3
Explanation:
Flipping the 0 at (0,1) connects two separate 1s diagonally adjacent. The resulting island size is 3.
'''

def largest_island(grid: list[list[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    largest_count = 0
    island_id = 2
    island_sizes = {}
    
    def dfs(row, col, id):
        if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
            grid[row][col] = id
            
            count = dfs(row + 1, col, id) + dfs(row - 1, col, id) + dfs(row, col + 1, id) + dfs(row, col - 1, id) + 1
            return count
        return 0
    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                island_sizes[island_id] = dfs(row, col, island_id)
                island_id += 1
                
    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                up = grid[row - 1][col] if row - 1 >= 0 and grid[row - 1][col] in island_sizes else 0
                down = grid[row + 1][col] if row + 1 < ROWS and grid[row + 1][col] in island_sizes else 0
                left = grid[row][col - 1] if col - 1 >= 0 and grid[row][col - 1]  in island_sizes else 0
                right = grid[row][col + 1] if col + 1 < COLS and grid[row][col + 1]  in island_sizes else 0
                
                directions = set([up, down, left, right])
                curr_count = 0
                
                for direction in directions:
                    if direction in island_sizes:
                        curr_count += island_sizes[direction]
                        
                largest_count = max(largest_count, curr_count + 1)
    
    return largest_count

if __name__ == "__main__":
    grid = [
        [1, 0],
        [0, 1]
    ]
    
    # assert largest_island(grid) == 3
    
    grid = [
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 1]
    ]
    
    assert largest_island(grid) == 9
    
