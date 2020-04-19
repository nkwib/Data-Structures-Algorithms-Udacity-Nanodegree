
import hashlib
from datetime import datetime, timezone

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.utcnow()
      self.data = data
      self.previous = None
      self.previous_hash = previous_hash
      if type(data) != 'str': data = str(data)
      self.hash = calc_hash(data + str(self.timestamp))

def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.head = None
    def new_block(self, data):
        if self.head == None: self.head = Block(data, '')
        else:
            previous_hash = self.head.hash
            new_block = Block(data, previous_hash)
            new_block.previous = self.head
            self.head = new_block

def list_blocks(A):
    res = []
    current = A.head
    if current:
        res.append(current)
    while current and current.previous != None:
        current = current.previous
        res.append(current)
    res.reverse()
    return res

def test(Blockchain):
    for item in list_blocks(Blockchain):
        print('\nTimeStamp : ',item.timestamp)
        print('Data : ',item.data)
        print('Hash : ',item.hash)
        print('Previous Hash: ', item.previous_hash)

A = Blockchain()

#test 1: empty chain

#test 2: one block
#A.new_block('first')

'''
#test3: multiple blocks
A.new_block('first')
A.new_block('second')
A.new_block('third')
A.new_block('fourth')
A.new_block('fifth')
A.new_block('sixth')
'''
'''
#test4: multiple blocks with longer data
A.new_block('Exercitation dolor consequat non ullamco ea.')
A.new_block('Nostrud tempor proident aute do elit.')
A.new_block('Velit ipsum exercitation nulla eu adipisicing culpa nisi dolore.')
A.new_block('Esse amet excepteur incididunt velit.')
A.new_block('Enim laboris dolore consectetur voluptate commodo.')
A.new_block('Aute laboris excepteur labore incididunt amet ad duis pariatur.')
'''
#test5: misc data
A.new_block('Exercitation dolor consequat non ullamco ea.')
A.new_block({1253511364: 125})
A.new_block(1365371375)
A.new_block(['pulp fiction', 'reservoir dogs', 'django'])
A.new_block(datetime.now())
A.new_block(calc_hash('SuperSecret'))



test(A)

