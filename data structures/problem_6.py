
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    res = LinkedList()
    inserted = dict()
    A, B = llist_1.head, llist_2.head
    while A != None or B != None:
        if A:
            if A.value not in inserted:
                res.append(A.value)
                inserted[A.value] = True
            A = A.next
        if B:
            if B.value not in inserted:
                res.append(B.value)
                inserted[B.value] = True
            B = B.next
    return res

def intersection(llist_1, llist_2):
    res = LinkedList()
    inserted = dict()
    A, B = llist_1.head, llist_2.head
    while A != None or B != None:
        if A:
            if A.value not in inserted:
                inserted[A.value] = 'A'
            elif inserted[A.value] == 'B':
                inserted[A.value] = False
                res.append(A.value)
            A = A.next
        if B: 
            if B.value not in inserted:
                inserted[B.value] = 'B'
            elif inserted[B.value] == 'A': 
                inserted[B.value] = False
                res.append(B.value)
            B = B.next
    return res

def test(l1, l2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = l1
    element_2 = l2

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print ("UNION:        ", union(linked_list_1,linked_list_2))
    print ("INTERSECTION: ", intersection(linked_list_1,linked_list_2))

# Test case 1
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
test(element_1, element_2)
# Test case 2
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
test(element_1, element_2)
# Test case 3
element_1 = []
element_2 = [1,7,8,9,11,21,1]
test(element_1, element_2)
# Test case 4
element_1 = []
element_2 = []
test(element_1, element_2)
# Test case 5
element_1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
element_2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
test(element_1, element_2)
# Test case 6
element_1 = ['I','am','a','string']
element_2 = ['I','have','the','code']
test(element_1, element_2)