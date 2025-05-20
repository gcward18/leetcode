'''
Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes already connected by an edge.
newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
Example 1:

6
1 -> 4 -> 5 
2 -> 3

6
1 -> 4 -> 5
| 5
2 -> 3

1 -> 4 -> 5
\
 \
  \ 10
   \
2 -> 3

  6
 / 2
1 -> 4 -> 5
2 -> 3

            5
1 -> 4 -> 5 -> 6
2 -> 3





Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.6

greedily take the choice of the minimum weight, and try to add that to our graph, if a union was successful then we can count towards our total weight, once all the components are connected return the sum of the weights


'''

from collections import Counter, defaultdict
import time
import heapq

class UnionFind:
    def __init__(self, size):
        self.root = list(range(size + 1))
        self.size = size
    
    def find(self, x:int):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x:int, y:int) -> bool:
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if xRoot != yRoot:
            self.root[y] = xRoot
            self.size -= 1
            return True
        return False
    
    
class Solution:
    def minCost(self, n: int, edges: list[int], new_edges: list[int]) -> int:
        uf = UnionFind(n) # wait for this
        minHeap = [] # going to track all the new_edges to add
        minCost = 0
        
        # build initial graph with all the connections
        for u, v in edges:
            uf.union(u,v)
        
        print('union was successful: ', uf.size == 3)
        
        for u, v, w in new_edges:
            heapq.heappush(minHeap, (w, u, v)) # weight, source, target
        
        print('heap has smallest on top: ', minHeap[0] == (2, 1, 6))
        
        while minHeap and uf.size != 1:
            weight, u, v = heapq.heappop(minHeap)
            
            if uf.union(u, v):
                minCost += weight
        
        return minCost

if __name__ == "__main__":
    solution = Solution()
    input, answer = [6, [[1, 4], [4, 5], [2, 3]],  [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]], 7
    start = time.time()
    result = solution.minCost(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for minCost to run was : {end - start:.10f} seconds")
    assert result == answer