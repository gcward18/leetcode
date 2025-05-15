'''
Distribute Parcels
Minimize Maximum Parcels
Distribute parcels among delivery agents in a way that minimizes the maximum number of parcels any single agent has to deliver. You're given:

An integer array parcels[i], where parcels[i] is the number of parcels currently assigned to the i-th agent.

An integer extra_parcels, which is the number of parcels that need to be distributed among the agents.

The goal is to find the minimum possible value of the maximum number of parcels any agent has after distributing the extra_parcels.


Example 1 :

Input: parcels = [6, 6, 5, 5], extra_parcels = 3
Output: 7


Example 2 :

Input: parcels = [7, 5, 1, 9, 1], extra_parcels = 25
Output: 10


Example 3 :

Input: parcels = [1], extra_parcels = 9
Output: 10
'''

import time, math
class Solution:
    def minimize_maximum_parcels(self, parcels: list[int], extra_parcels: int) -> int:
        max_parcel = max(parcels)
        for parcel in parcels:
            diff = max_parcel - parcel
            extra_parcels = extra_parcels - diff
            if extra_parcels <= 0:
                return max_parcel
        
        return max_parcel + math.ceil(extra_parcels / len(parcels))

if __name__ == "__main__":
    solution = Solution()
    input, answer = [ [6, 6, 5, 5], 3], 7
    start = time.time()
    result = solution.minimize_maximum_parcels(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for minimize_maximum_parcels to run was : {end - start:.10f} seconds")
    assert result == answer