import time
class Solution:
    def findNextLargest(self, nums: list[int]) -> list[int]:
        stack = []
        result = [-1] * len(nums)
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            stack.append(i)
            
        return result
    
    def findNextSmallest(self, nums: list[int]) -> list[int]:
        stack = []
        result = [-1] * len(nums)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        return result
            
        

if __name__ == "__main__":
    solution = Solution()
    input, answer = [1,2,3,6,4,5,7], [-1,-1,-1,4,-1,-1,-1]
    start = time.time()
    result = solution.findNextSmallest(input)
    end = time.time()
    print(f"Elapsed time for findNextLargest to run was : {end - start:.10f} seconds")
    assert result == answer