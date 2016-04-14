#!/usr/bin/env python

from operator import itemgetter
import sys

building_id = None
diff = None
arr = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    building_id, diff= line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        diff = int(diff)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if arr.has_key(building_id):
        arr[building_id][0] += diff
        arr[building_id][1] += 1
    else:
        arr[building_id] = [diff,1]

# do not forget to output the last word if needed!
for key, value in arr.iteritems():
    #print '%d \t %d' % (value[0], value [1])
    print '%s\t%s' % (key, float(value[0])/float(value[1]))
