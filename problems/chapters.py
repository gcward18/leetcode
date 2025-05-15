'''
There are list of chapters where chapters[i] represents the number of pages in that chapter.
We can read upto k consecutive chapters per day. Additionally, we can only read p pages per chapter a day.
Find the minimum number of days required to complete reading all the chapters.

input #1
chapters = [10,20,30,40]
k = 2
p = 10

result: 6

chapters: [5,1,4,3,2,7,1]
k = 3
p = 2

result: 7
'''

class Solution:
    def minimumNumDays(self, chapters: list[int], k: int, p: int) -> int:
        '''
        some comments about code
        '''
        return 0

if __name__ == "__main__":
    solution = Solution()
    input = [[10,20,30,40], 2, 10]
    answer = [7]
    assert solution.minimumNumDays(input[0]) == 0