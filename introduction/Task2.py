"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time_map = defaultdict(int)
for calling, answering, _, time in calls:
    time_map[calling] += int(time)
    time_map[answering] += int(time)

max = max(time_map.items(), key=lambda call: call[1])

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(max[0], max[1]))