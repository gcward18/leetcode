import time
from collections import defaultdict

class Solution:
    def processQueriesOnCart(self, items: list[int], query: list[int]) -> int:
        counter = defaultdict(lambda: 0)
        for q in query:
            counter[-q] += 1
        
        result = []
        for item in items:
            if counter[item] > 0:
                counter[item] -= 1
            else:
                result.append(item)
                
        for item in query:
            if item > 0:
                if counter[item] > 0:
                    counter[item] -= 1
                else:
                    result.append(item)
        
        return result

if __name__ == "__main__":
    solution = Solution()
    input, answer = [ [5, 1, 2, 2, 4, 6],  [1, -2, -1, -1]],  [5, 2, 4, 6]
    start = time.time()
    result = solution.processQueriesOnCart(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for processQueriesOnCart to run was : {end - start:.10f} seconds")
    assert result == answer