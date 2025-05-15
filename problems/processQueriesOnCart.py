'''
Process Queries on Cart
FULLTIME
Build a prototype for a cart management service.

An array of integers, items, represents the item ids in the cart initially.

Given another array of q integers, query, your service must perform as follows.

Each integer is an item id to be added to or removed from the cart.
If the query integer is positive, add the integer representing an item id to the back of the cart.
If the query integer is negative, remove the first occurrence of the integer from the cart.
List the final items present in the cart after all the queries are completed.
It is safe to assume that the cart will not end up empty. The queries only ask for removal of items that are present in the cart. There is no 0 in array query.

Function Description

Complete the function processQueriesOnCart in the editor below.

processQueriesOnCart has the following parameters:

int items[n] : items initially in the cart
int query[q] : items to add or remove

Example 1 :

Input: items = [1, 2, 1, 2, 1], query = [-1, -1, 3, 4, -3]
Output: [2, 2, 1, 4]
Explanation:
Initially, there are n = 5 items in the cart represented as cart = [1,2,1,2,1] and queries = [-1,-1,3,4,-3]

Query	Task	Cart
-1	Delete first 1 from cart	[2,1,2,1]
-1	Delete first 1 from cart	[2,2,1]
3	Append 3 to cart	[2,2,1,3]
4	Append 4 to cart	[2,2,1,3,4]
-3	Delete first 3 from cart	[2,2,1,4]
Report [2,2,1,4] as the final cart.


Example 2 :

Input: items = [5, 1, 2, 2, 4, 6], query = [1, -2, -1, -1]
Output: [5, 2, 4, 6]
Explanation:
items = [5, 1, 2, 2, 4, 6]
queries = [1, -2, -1, -1]

Query	Task	Cart
1	Append 1 to cart	[5, 1, 2, 2, 4, 6, 1]
-2	Delete first 2 from cart	[5, 1, 2, 4, 6, 1]
-1	Delete first 1 from cart	[5, 2, 4, 6, 1]
-1	Delete first 1 from cart	[5, 2, 4, 6]
Report [5, 2, 4, 6] as the final cart.


Constraints:

1 <= n, q <= 2 * 10^5
1 <= items[i] <= 10^9
-10^9 <= query[i] <= 10^9
It is guaranteed that query[i] != 0`
'''
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