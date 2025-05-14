class Solution:
    def integerToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tenths = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[(num % 1000)//100] + tenths[(num % 100)//10] + ones[(num % 10)] 

if __name__ == "__main__":
    solution = Solution()
    
    print(solution.integerToRoman(3749), ' == ', 'MMMDCCXLIX')