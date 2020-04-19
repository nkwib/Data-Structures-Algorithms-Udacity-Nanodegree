import heapq
import sys
from collections import Counter 

class Node:
    def __init__(self,value, freq):
        self.value = value
        self.freq = freq        
        self.right = None
        self.left = None
        
    # heapq required method
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(data):
    heap = get_frequecies(data)
    heapq.heapify(heap)
    while len(heap) != 1:
        Z = Node(None,None)
        l = heapq.heappop(heap)
        Z.left  = l
        r = heapq.heappop(heap)
        Z.right  = r
        Z.freq = l.freq + r.freq
        heapq.heappush(heap, Z)
    return heap

def map_characters(tree):
    code = {}
    def getCode(node, currentCode=""):
        if (node == None): return
        if (node.left == None and node.right == None):
             code[node.value] = currentCode
        getCode(node.left, currentCode + "0")
        getCode(node.right, currentCode + "1")
    getCode(tree[0])
    return code

def get_frequecies(data):
  freq = Counter(data)
  freq_sorted = sorted(zip(freq.values(), freq.keys()))
  for i in range(len(freq_sorted)):
     freq_sorted[i] = Node(freq_sorted[i][1], freq_sorted[i][0])
  return freq_sorted

def huffman_encoding(data):
    tree = huffman_tree(data)
    if(len(get_frequecies(data))) == 1: 
        return "0"*len(data), data[0]
    huff_code = ""
    h_map = map_characters(tree)
    for item in data:
      huff_code += h_map[item]
    return huff_code, tree
  
  
def huffman_decoding(data,tree):
    count = 0
    decoded = ""
    if(len(get_frequecies(data))) == 1:
        return len(data)*str(tree)
    while count < len(data):
        curr_node = tree[0]
        while curr_node.left != None and curr_node.right != None:
            curr_node = curr_node.left if data[count] == "0" else curr_node.right
            count+=1
        decoded += curr_node.value
    return decoded

def test(data):
    if data == None: 
        print(None)
        return None
    if data == "": 
        print('empty string')
        return ""
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)


    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('passed' if (decoded_data == data) else 'fail')


if __name__ == "__main__":
    '''
    data = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('passed' if (decoded_data == data) else 'fail')
    '''

test(None)
test("")
test("a")
test("aa")
test("aaa")
test("ab")
test("abbb")
test("abc")
test("The bird is the word")
test("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")