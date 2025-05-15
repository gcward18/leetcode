'''
There are n nodes in amazon shipping centre, where each node should conect to the nearest hub, the last node is always a hub. There will be list of k queries provided, each of them having a list of additional nodes which could also act as hubs, we need to find the min cost of having this setup for each query.
The cost is defined as the difference between node and the nearest hub. all the nodes are 1 indexed.
Note: a node can connect to a hub whose index is equal or greater than that.

nodes = [10,20,30,40,50]
queries = [[2,4], [1,3]]

result = [20, 20]

explanation: for query 1,
node 1 nearest hub 20, 20-10 = 10
node 2 nearest hub is itself: 20-20 = 0
node 3 nearest hub is 40, 40-30 = 10
node 4, nearest hub is itself: 40-40 = 0
node 5, nearest hub is itself: 50-50 = 0

similarly for query 2
'''

class Solution:
    def shippingCalc(self, nodes: list[int], queries: list[list[int]]) -> list[int]:
        '''
        some comments about code
        '''
        return []

if __name__ == "__main__":
    solution = Solution()
    input = [[10,20,30,40,50],  [[2,4], [1,3]]]
    answer = [20, 20]
    assert solution.shippingCalc(input[0], input[1]) == answer