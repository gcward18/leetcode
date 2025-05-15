'''
Similar DNA Pairs
FULLTIME
A DNA sequence is represented by a string of lowercase letters. Given a pair of DNA sequences,
if the scientist is able to remove any number of a letter in sequence1 and any number of a letter
in sequence2 to make the strings anagrams, then the sequences are similar.

Given n pairs of DNA sequences, for each pair, attempt to find if they are similar. Return 
a list of boolean values where boolean[i] indicates for the i'th pair.


Function Description

Complete the function getSequence in the editor below.

getSequence has the following parameter(s):

String dna[n][2] : the pairs of DNA sequences.

Returns

boolean[n] : 'true' if the pair is special, and 'false' otherwise


Example 1 :

Input: dna = [["safddadfs", "famafmss"]]
Output: [true]
Explanation:
The strings are anagrams after removing all the occurrences of character 'd' from s and character 'm' from t. Return [True].
Note: It is not required that all instances of a character be removed. For example, given 'aab' and 'ba', one 'a' 
can be removed from 'aab' to leave 'ab'.


Example 2 :

Input: dna = [["abcee", "acdeedb"], ["sljffsajej", "sljsje"]]
Output: [true, false]
Explanation:
For pair 1, remove 'b' from the second string and leave the first string untouched.
For pair 2, dna1 contains 'f' and 'a' which are not in dna2. They cannot be anagrams after removing only a character from dna1.


Constraints:

1 <= n <= 10
1 <= length of dna[i][0], dna[i][1] <= 10000.
The strings in dna1 and dna2 consist of lowercase English letters only.
'''
from collections import Counter
from collections import Counter

class Solution:   
    
    def isAnagramByLetterRemoval(self, s, t) -> bool:
        extraInT = None
        sCount = Counter(s)
        
        for c in t:
            if c in sCount:
                if sCount[c] == 1:
                    del sCount[c]
                else:
                    sCount[c] -= 1
            elif extraInT and c != extraInT:
                return False
            else:
                extraInT = c
        
        return len(sCount) <= 1
                
    def dnaSequence(self, dna):
        return [self.isAnagramByLetterRemoval(s1, s2) for s1, s2 in dna]

# Test function to verify results
def test_solution():
    solution = Solution()
    
    # Original test cases
    test_cases = [
        ['aonecode', 'aonecode'],    # Should be True (identical)
        ['xxxyyyz', 'xxyzzxyyy'],    # Should be True
        ['aaaaaa', 'aakkaakk'],      # Should be True
        ['aaabbaa', 'bbaabab']       # Should be True
    ]
    
    print("Original test cases:")
    for i, (s1, s2) in enumerate(test_cases):
        result = solution.isAnagramByLetterRemoval(s1, s2)
        print(f"Test {i}: '{s1}' and '{s2}' => {result}")
    
    # Problem examples
    examples = [
        ["safddadfs", "famafmss"],    # Should be True
        ["abcee", "acdeedb"],         # Should be True
        ["sljffsajej", "sljsje"]      # Should be False
    ]
    
    print("\nProblem examples:")
    for i, (s1, s2) in enumerate(examples):
        result = solution.isAnagramByLetterRemoval(s1, s2)
        print(f"Example {i+1}: '{s1}' and '{s2}' => {result}")
    
    # Run the full test suite from the original test
    input_data = [['aonecode', 'aonecode'], ['xxxyyyz', 'xxxyyyyzz'], 
                  ['aaaaaa', 'aaaakkkk'], ['aaaaabb', 'bbaabab']]
    expected = [True, False, True, True]
    result = solution.dnaSequence(input_data)
    
    print("\nFull test suite:")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print(f"Pass: {result == expected}")

    # Example test from problem statement
    test1 = [["safddadfs", "famafmss"]]
    expected1 = [True]
    result1 = solution.dnaSequence(test1)
    print(f"\nTest from problem statement 1:")
    print(f"Expected: {expected1}")
    print(f"Got:      {result1}")
    
    test2 = [["abcee", "acdeedb"], ["sljffsajej", "sljsje"]]
    expected2 = [True, False]
    result2 = solution.dnaSequence(test2)
    print(f"\nTest from problem statement 2:")
    print(f"Expected: {expected2}")
    print(f"Got:      {result2}")

# Run the test
if __name__ == "__main__":
    test_solution()