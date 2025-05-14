class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        '''
        use a two pointer approach, where we take the sum of the curr i, j, kth index and compare it to the target
        if the diff between the target and the sum is smaller than any previous diff, then we store that diff and return
        the target - diff
        '''
        min_diff = float("inf")
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            low, high = i + 1, n - 1
            
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                
                if abs(target - sum) < abs(min_diff):
                    min_diff = target-sum
                
                if sum < target:
                    low += 1
                else: 
                    high -= 1
            
            if min_diff == 0:
                break
            
        return target - min_diff  

if __name__ == "__main__":
    solution = Solution()
    input0 = [[-1,2,1,-4], 1]
    input1 = [[0,0,0], 1]
    assert solution.threeSumClosest(input0[0], input0[1]) == 2
    assert solution.threeSumClosest(input1[0], input1[1]) == 0
    
    