# Problem #146
# https://leetcode.com/problems/lru-cache
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4



class LLNode:
    
    def __init__(self, key, prior = None):
        self.key = key
        self.prior = prior
        if self.prior != None:
            self.prior.next = self
        self.next = None




class LRUCache:

    def __init__(self, capacity: int):
        #print("Capacity is: ", capacity)
        self.k = capacity
        self.d = {}
        # d structure: {key:[node[key,prior,next],val]}
        self.h = None
        self.t = None
        self.size = 0
        
    def stringOrder(self):
        s = 'Forward: '
        last = None
        node = self.h
        while node != None:
            s += (" ("+str(node.key)+") <->")
            last = node
            node = node.next
        s = s[:-4]
        s+= "\nBackward: "
        while last != None:
            s += (" ("+str(last.key)+") <->")
            last = last.prior
        s = s[:-4]
        print(s)
        return s
    
    def get(self, key: int) -> int:
        #print("\n\n")
        #print("Getting: ", key)
        if key in self.d:
            #print('got key')
            node = self.d[key][0]
            if self.size == 1:
                pass
            else:
                if self.h.key == key:
                    #print("node is head")
                    self.h.next.prior = None
                    self.h = node.next
                    node.prior = self.t
                    node.next = None
                    self.t.next = node
                    self.t = self.t.next
                elif key != self.t.key:
                    #print("node is not head, not tail")
                    node.prior.next = node.next
                    node.next.prior = node.prior
                    node.prior = self.t
                    node.next = None
                    self.t.next = node
                    self.t = self.t.next




            
            #print("new head is: ", self.h.key)
            #print("new tail is: ", self.t.key)
            return self.d[key][1]
        else:
            #print("Key not found")
            return -1
        

    def put(self, key: int, value: int) -> None:
        #print("\n\nPutting: ", key)
        #print("size:", self.size, "/", self.k)
        ##add key : node/val pair to cache
        if self.size == 0:
            node = LLNode(key)
            self.d[key] = [node,value]
            #print("Adding first element: ", key,":", value)
            self.h = node
            self.t = node
            self.size += 1
        elif key in self.d:
            #print("Replacing: ", key,":", value)
            self.d[key][1] = value
            node = self.d[key][0]
            if self.size == 1:
                #print("size = 1")
                pass
            else:
                if self.h.key == key:
                    #print("node is head")
                    self.h.next.prior = None
                    self.h = self.h.next
                    node.prior = self.t
                    node.next = None
                    self.t.next = node
                    self.t = self.t.next
                elif key != self.t.key:
                    #print("node is not head, not tail")
                    node.prior.next = node.next
                    node.next.prior = node.prior
                    node.prior = self.t
                    node.next = None
                    self.t.next = node
                    self.t = self.t.next
        else:
            #print("Adding element:", key, ":", value)
            node = LLNode(key, self.t)
            self.d[key] = [node,value]
            #print("tail is:", self.t.key)
            self.t.next = node
            self.t = self.t.next
            self.size += 1
            if self.size == self.k+1:
                #print("At capacity, deleting head")
                self.d.pop(self.h.key, None)
                self.h = self.h.next
                self.h.prior = None
                self.size -= 1
        #print("new tail is: ", self.t.key)