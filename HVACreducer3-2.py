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
        if arr[building_id].has_key(time) :
            arr[building_id][time][0] += temp
            arr[building_id][time][1] += 1
        else :
            arr[building_id][time] = [temp, 1]
    else:
        arr[building_id] = {time :[temp,1]}

# do not forget to output the last word if needed!
for key,value in arr.items():

    for time, val in value.items():
        print '%s,%s,%s' % (key, time, float(val[0])/float(val[1]))







