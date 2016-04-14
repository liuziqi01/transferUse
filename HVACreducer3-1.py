#!/usr/bin/env python

from operator import itemgetter
import sys
import operator

building_id = None
temp = None
time = None
arr = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    building_id, temp, time= line.split('\t')

    # convert count (currently a string) to int
    try:
        temp = int(temp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if arr.has_key(building_id):
        arr[building_id][0] += temp
        arr[building_id][1] += 1
    else:
        arr[building_id] = [temp,1]
counter =0
# do not forget to output the last word if needed!
for key,value in arr.items():
    t = 0
    arr[key] = float(value[0]) / float(value[1])
for key, value in sorted(arr.items(), key = itemgetter(1),reverse = True):
    #print '%d \t %d' % (value[0], value [1])
    if counter < 5 :
           print '%s\t%s' % (key, value)
           counter+=1
    else :
           break
