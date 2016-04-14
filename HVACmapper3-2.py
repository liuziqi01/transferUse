#!/usr/bin/env python

import sys
top5 = sys.argv[1:6]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    #print words
    try:
        words[2] = int(words[2])
    except ValueError:
        continue
    time = int(words[1].split(':')[0])
    if time < 17 and time > 8 and (words[6] in top5):
         print '%s\t%s\t%s ' % (words[6], words[3], time)
