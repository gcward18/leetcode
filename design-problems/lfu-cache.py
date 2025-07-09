'''
🔁 Problem 1: LFU Cache (Least Frequently Used Cache)
Design a data structure that supports the following operations in O(1) average time:

get(key): return the value of the key if it exists, else return -1.

put(key, value): update the value of the key if it exists; otherwise, insert the key-value pair.
If the cache reaches capacity, evict the least frequently used key.
If there’s a tie in frequency, remove the least recently used one.

🧾 Example:
python
Copy
Edit
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
lfu.get(1)       # returns 1
lfu.put(3, 3)    # evicts key 2 (freq=1, LRU)
lfu.get(2)       # returns -1
lfu.get(3)       # returns 3
lfu.get(1)       # returns 1
lfu.put(4, 4)    # evicts key 3 (freq=1, LRU)
lfu.get(3)       # returns -1
lfu.get(4)       # returns 4
✅ Constraints:
0 <= key, value <= 10^4

Total operations ≤ 10^5

Capacity ≥ 0


'''
from collections import defaultdict

class ListNode:    
    def __init__(self, key: int, value: int, prev: 'ListNode'=None, next: 'ListNode'=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1, self.head)
        self.head.next = self.tail
        self.size = 0
        
    def _insert(self, node: ListNode, prev: ListNode, next: ListNode) -> None:
        node.prev, node.next = prev, next
        prev.next, next.prev = node, node
        self.size += 1
        
    def _remove(self, node: ListNode) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.size -= 1
    
    def length(self) -> int:
        return self.size
    
    def push_head(self, key: int, value: int):
        self._insert(ListNode(key, value), self.head, self.head.next)
        
    def push_tail(self, key: int, value: int):
        self._insert(ListNode(key, value), self.tail.prev, self.tail)
        
    def push_node_tail(self, node: ListNode):
        self._insert(node, self.tail.prev, self.tail)
    
    def pop_tail(self):
        if self.size > 0:
            node = self.tail.prev
            self._remove(node)
            return node
    
    def pop_head(self):
        if self.size > 0:
            node = self.head.next 
            self._remove(node)
            return node
        return None
        
class LFUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._node_freq = {}
        self._freq_cache = defaultdict(LinkedList)
        self._min_frequency = 0
    
    def _update(self, key: int, value: int):
        frequency, node = self._node_freq[key]
        
        # update node
        if value is not None:
            node.value = value
        
        # get the frequency and update the frequency list we are tracking it on
        self._freq_cache[frequency]._remove(node)
        
        if self._freq_cache[frequency].length() == 0:   
            del self._freq_cache[frequency]
            if self._min_frequency == frequency:
                self._min_frequency += 1
    
        # we have to increment the frequency
        frequency += 1
        self._freq_cache[frequency].push_node_tail(node)
        self._node_freq[key] = (frequency, node)
        
    def _remove(self, key):
        frequency, node = self._node_freq[key]
        linked_list = self._freq_cache[frequency]
        linked_list._remove(node)
        
        if linked_list.length() == 0:
            del self._freq_cache[frequency]
            del self._node_freq[key]
        
    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        
        if key in self._node_freq:
            self._update(key, value)
            return
        
        if len(self._node_freq) > self._capacity:
            node_to_evict = self._freq_cache[self._min_frequency].pop_head()
            del self._node_freq[node_to_evict.key]
        
        node = ListNode(key, value)
        self._freq_cache[1].push_node_tail(node)
        self._node_freq[key] = (1, node)
        self._min_frequency = 1
            
    def get(self, key:int) -> int:
        if key not in self._node_freq:
            return -1
        
        self._update(key, None)
        _, node = self._node_freq[key]
        
        return node.value
        
if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    lfu.get(1)       # returns 1
    lfu.put(3, 3)    # evicts key 2 (freq=1, LRU)
    lfu.get(2)       # returns -1
    lfu.get(3)       # returns 3
    lfu.get(1)       # returns 1
    lfu.put(4, 4)    # evicts key 3 (freq=1, LRU)
    lfu.get(3)       # returns -1
    lfu.get(4)       # returns 4
