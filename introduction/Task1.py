"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
nums = set()

for num in range(len(texts)):
    nums.add(texts[num][0])
    nums.add(texts[num][1])
for num in range(len(calls)):
    nums.add(calls[num][0])
    nums.add(calls[num][1])
    
print('There are {} different telephone numbers in the records.'.format(str(len(nums))))