'''
🔍 Problem: Word Ladder (Graph / BFS)
Scenario:
You are given two words, a beginWord and an endWord, and a dictionary wordList.
Each transformation must change exactly one letter and result in a word from the list.

Question:
Return the length of the shortest transformation sequence from beginWord to endWord.
If no such transformation is possible, return 0.

🧾 Example:
Input:

python
Copy
Edit
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output:

python
Copy
Edit
5
Explanation:
The shortest path is:
"hit" → "hot" → "dot" → "dog" → "cog"

✅ Constraints:
All words are of same length.

You may assume endWord is in wordList.

Only one letter can be changed at a time.

Each intermediate word must exist in wordList.

Expected time complexity: O(N * M) where:

N = number of words in wordList

M = length of each word

'''
from collections import deque

def word_ladder(begin_word: str, end_word: str, word_list: list[str]) -> int:
    queue = deque([(begin_word, 1)])
    update_count = float("inf")
    word_list = set(word_list)
    visited = set()
    
    while queue:
        word, count = queue.popleft()
        
        if word == end_word:
            return count
        
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i + 1:]
                if new_word in word_list and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, count + 1))    

    return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    assert word_ladder(beginWord, endWord, wordList) == 5