'''
Get Operations
There are n processes. The i-th process has resource[i] number of resources. All the resource[i] are distinct. The CPU wants the processes to be arranged in increasing order of their resource[i] . The CPU does several operations to make this.

In each operation, the CPU selects an integer x and a process with number of resources x . It then places all processes with resource values less than x before the processes with resource values greater than or equal to x , maintaining their original order i.e. the relative order between processes having resource value less than x should be maintained and the same applies for processes having resource value greater than or equal to x .

Find the lexicographically smallest sequence of Xs that the CPU chooses, such that it takes the minimum number of operations to complete the task.

Note: If the minimum number of operations = 0, then return a sequence only containing the integer -1.


Function Description

Complete the function getOperations in the editor below. getOperations has the following parameter(s):

int resource[n] : Contains the number of resources of each process
Returns

int[] : Lexicographically smallest sequence of Xs such that it takes the minimum number of operations to complete the task.


Example 1 :

Input: resource = [6, 4, 3, 5, 2, 1]
Output: [2, 3, 4, 6]
Explanation:
CPU can achieve the minimum number of operations in the following way:

Choose x=2: [6, 4, 3, 5, 2, 1] -> [1, 6, 4, 3, 5, 2]

Choose x=3: [1, 6, 4, 3, 5, 2] -> [1, 2, 6, 4, 3, 5]

Choose x=4: [1, 2, 6, 4, 3, 5] -> [1, 2, 3, 6, 4, 5]

Choose x=6: [1, 2, 3, 6, 4, 5] -> [1, 2, 3, 4, 5, 6]

Minimum number of operations = 4, and the answer is [2, 3, 4, 6].


Example 2 :

Input: resource = [10, 15, 14, 12, 13]
Output: [14, 15]
Explanation:
The optimal way is:
Choose x = 14: [15, 10, 14, 12, 13] -> [10, 12, 13, 15, 14]

Choose x = 15: [10, 12, 13, 15, 14] -> [10, 12, 13, 14, 15]

So, the answer is [14, 15].


Example 3 :

Input: resource = [2, 4, 14, 10, 5, 3]
Output: [4, 10, 14]
Explanation:
The optimal way is:

Choose x = 4: [2, 4, 14, 10, 5, 3] -> [2, 3, 4, 14, 10, 5]

Choose x = 10: [2, 3, 4, 14, 10, 5] -> [2, 3, 4, 5, 14, 10]

Choose x = 14: [2, 3, 4, 5, 14, 10] -> [2, 3, 4, 5, 10, 14]

So, the answer is [4, 10, 14].


Constraints:

1 ≤ n ≤ 50
1 ≤ resource[i] ≤ 10^9
All resource[i] are distinct
'''

import time
class Solution:
    def getOperations(self, **params) -> int:
        '''
        some comments about code
        '''
        return 0

if __name__ == "__main__":
    solution = Solution()
    input, answer = [6, 4, 3, 5, 2, 1],  [2, 3, 4, 6]
    start = time.time()
    result = solution.getOperations(input)
    end = time.time()
    print(f"Elapsed time for getOperations to run was : {end - start:.10f} seconds")
    assert result == answer