'''
Min Cost To Add New Roads
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2together. (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together. The cost is the sum of the connection costs used. If the task is impossible, return -1.

Example 1:

Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation:
Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:

Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation:
There is no way to connect all cities even if all edges are used.
Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]


'''

import time
class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        self.size = size
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.root[rootY] = rootX
            self.size -= 1
            return True
        return False

class Solution:
    from heapq import heappop, heappush

    def minCostConnectNodes(self, N, connections):
        uf = UnionFind(N + 1)
        cost = 0
        connections_made = 0
        for u, v, w in sorted(connections, key=lambda x:x[2]):
            if uf.union(u,v):
                cost += w
                connections_made += 1
                
                
        if connections_made != N-1:
            return -1
        
        return cost

if __name__ == "__main__":
    solution = Solution()
    input, answer = [[[0, 1, 12], [0, 2, 100], [0, 3, 100], [0, 4, 100], [0, 5, 100],
                      [0, 6, 100], [0, 7, 100], [0, 8, 25], [1, 2, 10], [1, 3, 100],
                      [1, 4, 100], [1, 5, 100], [1, 6, 100], [1, 7, 40], [1, 8, 8],
                      [2, 3, 18], [2, 4, 100], [2, 5, 100], [2, 6, 55], [2, 7, 100],
                      [2, 8, 100], [3, 4, 44], [3, 5, 100], [3, 6, 100], [3, 7, 100], 
                      [3, 8, 100], [4, 5, 60], [4, 6, 38], [4, 7, 100], [4, 8, 100], 
                      [5, 6, 100], [5, 7, 100], [5, 8, 100], [6, 7, 35], [6, 8, 100], 
                      [7, 8, 35]] , 9], 216 
    start = time.time()
    result = solution.minCostConnectNodes(input[1], input[0])
    end = time.time()
    print(f"Elapsed time for minCostConnectNodes to run was : {end - start:.10f} seconds")
    assert result == answer