# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# Example:

# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 

# Note:

# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000]

class LLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        

class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None for _ in range(1000)]
        
        
        
        
    def h(self, key):
        return ((key*103) % 2029) % 1000
        
        
        
    def put(self, key: int, value: int) -> None:
        hKey = self.h(key)
        
        node = self.map[hKey]
        if node == None:
            self.map[hKey] = LLNode(key, value)
        else:
            while node != None and node.key != key:
                node = node.next
            if node == None:
                newNode = LLNode(key, value)
                newNode.next = self.map[hKey]
                self.map[hKey] = newNode
            else:
                node.val = value
                
        """
        value will always be non-negative.
        """
        

    def get(self, key: int) -> int:
        hKey = self.h(key)
        if self.map[hKey] == None:
            return -1
        else:
            node = self.map[hKey]
            while node != None and node.key != key:
                node = node.next
            if node == None:
                return -1
            else:
                return node.val
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

