class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        '''
        need to keep track of the 4 numbers that are closest to the target, lets try three sum with another starting number
        [0, 0, 2, 3, 4]
         i  j  k     l
         ^ 
         call this until we hit a length of k = 3
         
         maybe we do a k sum and set k = 4
         that seems good,
         once we process a number we need to skip all of the same values are we will get the same result multiple times
         
        '''
        result = []
        curr = []
        nums.sort()
        def kSum(start, target, k):
            nonlocal result
            if k == 2:
                low, high = start, len(nums) -1
                
                while low < high:
                    sum = nums[low] + nums[high]
                    
                    if sum < target:
                        low += 1
                    elif sum > target:
                        high -= 1
                    else:
                        result.append(curr[:] + [nums[low], nums[high]])
                        while low + 1 < len(nums) and nums[low] == nums[low + 1]:
                            low += 1
                        low += 1
                            
            else:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    else:
                        curr.append(nums[i])
                        kSum(i + 1, target - nums[i], k - 1)
                        curr.pop()
        
        kSum(0, target, 4)
        return result

if __name__ == "__main__":
    solution = Solution()
    input = [[1,0,-1,0,-2,2], 0]
    result = solution.fourSum(input[0], input[1])
    answer = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    assert all( res in answer for res in result) == True