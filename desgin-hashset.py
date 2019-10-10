# Problem #705
# https://leetcode.com/problems/design-hashset
# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Example:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)

# Note:

# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.

class LLNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        

class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None for _ in range(1000)]
        
    def h(self, key):
        return ((key*103) % 2029) % 1000
        
    def add(self, key: int) -> None:
        hKey = self.h(key)
        
        node = self.map[hKey]
        if node == None:
            self.map[hKey] = LLNode(key)
        else:
            while node != None and node.key != key:
                node = node.next
            if node == None:
                newNode = LLNode(key)
                newNode.next = self.map[hKey]
                self.map[hKey] = newNode
                
        """
        value will always be non-negative.
        """
        
    def contains(self, key: int) -> int:
        hKey = self.h(key)
        node = self.map[hKey]
        while node != None and node.key != key:
            node = node.next
        if node == None:
            return False
        else:
            return True
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
    def remove(self, key: int) -> None:
        hKey = self.h(key)
        if self.map[hKey] == None:
            return -1
        else:
            prior = None
            node = self.map[hKey]
            while node != None and node.key != key:
                prior = node
                node = node.next
                
            if node == None:
                pass
            else:
                if prior == None:
                    self.map[hKey] = node.next
                else:
                    prior.next = node.next
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)