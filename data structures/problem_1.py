class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.tail = None
        self.length = 0

    def insert(self, data: Node):
        new_node = data
        if self.start is not None:
            self.start.prev = new_node
            new_node.next = self.start
        else:
            self.tail = new_node
        self.start = new_node
        self.length += 1

    def pop_to_start(self, node: Node):
        if self.length == 1: return
        if node.val == self.start.val: return
        #TODO: think about removing from tail and adding to the start or if there's only one element in the DLL
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev.next = node.next
        self.length -= 1
        self.insert(Node(node.val))

    def pop_tail(self):
        old = self.tail
        if self.tail.prev != None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        return old
        

class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity <= 0: 
            print('capacity choice cannot be less than 1')
            capacity = 1
        self.cache = dict()
        self.capacity = capacity
        self.dll = DoublyLinkedList()

    def set(self, key, value):
        added = Node(value)
        if self.capacity == self.dll.length:
            if key in self.cache:
                print(key)
                self.dll.pop_to_start(self.cache[key])
                self.cache[key] = added
            else:
                old_index = self.dll.pop_tail()
                del self.cache[old_index.val]
                self.cache[key] = added
                self.dll.insert(added)
        else:
            self.cache[key] = added
            self.dll.insert(added)

    def get(self, key):
        if key in self.cache:
            res = self.cache[key]
            return res.val
        else:
            return -1


# TEST 1: normal functioning
C = LRU_Cache(5)
C.set(1, 1)
C.set(2, 2)
C.set(3, 3)
C.set(4, 4)
C.get(1)
C.get(2)
C.get(9)
C.set(5, 5) 
C.set(6, 6)
C.get(3)
print(C.cache[5].val) #return 5

# TEST 2: normal functioning with a deletion from the cache
C2 = LRU_Cache(2)
C2.set(1, 1)
C2.set(2, 2)
C2.set(3, 3)
C2.set(4, 4)
C2.set(2, 2)
print(C2.get(2))     # returns 2
print(C2.get(3))      # returns -1 because was deleted from the cache


# TEST 3: if 0 or less the capacity is forced into 1
C3 = LRU_Cache(0)
C3.set(4, 4)
C3.set(3, 3)
C3.set(2, 2)
print(C3.get(2)) #returns 2

# TEST 4: test if it breaks with strings
C4 = LRU_Cache(10)
C4.set(2, 2)
print(C3.get('2')) # returns -1 because it's a string
C4.set('2', 2)
print(C4.get('2')) # now that the key '2' is set it returned 2
