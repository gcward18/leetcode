class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        '''
        digits are in the range of 2 - 9 and are passed as strings
        convert the digits to return all possible letter combinations
        
        look at backtracking:
            "23"
             i
           / | \            
          a  b  c
         /|\
        d e f
        
        start with first letter and then go through all subsequent letters and if current i == len(string) append to result and return
        only go through the available letters on each character 
        
                dfs(index, curr)
                i= 0, []
                
                "2"    curr = ["ad", "ae", "af", "b", "c"]
                /|\
               a b c  i = 1
               
               "3"
              /|\
             d e f
        '''
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        def dfs(index: int, curr: list[int]) -> None:
            if index == len(digits):
                result.append(''.join(curr[:]))
                return
            
            for char in mappings[digits[index]]:
                curr.append(char)
                dfs(index + 1, curr)
                curr.pop()
                
            return
        
        dfs(0, [])
        return result

if __name__ == "__main__":
    solution = Solution()
    input = ["23"]
    assert all(combination in ["ad","ae","af","bd","be","bf","cd","ce","cf"] for combination in solution.letterCombinations(input[0])) == True