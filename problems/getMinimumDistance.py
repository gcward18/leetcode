'''
Get Minimum Total Distance
FULLTIME
There are n distribution centers, all built along a straight line. 
They plan to build two warehouses to serve the distribution centers.
A distribution center has its demands met by the warehouse that is 
closest to it. Position the warehouses optimally, such that the sum
of distances from the distribution centers to their closest warehouse is minimized.

Given an array dist_centers, that represent the positions of the distribution
centers, return the minimum sum of distances to their closest warehouses 
if the warehouses are positioned optimally.


Function Description

Complete the function getMinTotalDistance in the editor.

getMinTotalDistance has the following parameter:

int dist_centers[n] : the locations of the distribution centers

Returns

int: the minimum sum of distances


Example 1 :

Input: dist_centers = [4, 1, 5, 99, 100]
Output: 5
Explanation: One optimal solution is to position warehouse at w1 = 4, w2 = 99.

[1, 4, 5, 99, 100]

dists:
[0,  3,  4, 98, 99]
[3,  0,  1, 95, 96]
[4,  1,  0, 95, 95]
[98, 95, 94, 0,  1]
[99, 96, 95, 1,  0]


curr_min_dist = 6
min_dist = 5
Example 2 :

Input: dist_centers = [1, 2, 3]
Output: 1
Explanation: One optimal solution is to position the warehouses at w1 = 1 and w2 = 2.

The minimum sum of the distances between distribution centers and the warehouses closest to them is 0 + 0 + 1 = 1.
'''

import time
class Solution:
    def getMinPlacements(self, dist_centers: list[int]) -> int:
        dist_centers.sort()
        min_dist =2**31
        n = len(dist_centers)
        
        for p in range(1, n):
            idx1 = (p - 1) // 2
            idx2 = (p + n - 1) // 2 
            
            curr_dist = 0
            
            for i in range(p):
                curr_dist += abs(dist_centers[idx1] - dist_centers[i]) 
            for i in range(p, n):
                curr_dist += abs(dist_centers[idx2] - dist_centers[i])
            min_dist = min(min_dist, curr_dist)
        
        return min_dist

if __name__ == "__main__":
    solution = Solution()
    input, answer = [1, 4, 5, 99, 100], 5
    start = time.time()
    result = solution.getMinPlacements(input)
    end = time.time()
    print(f"Elapsed time for getMinPlacements to run was : {end - start:.10f} seconds")
    assert result == answer