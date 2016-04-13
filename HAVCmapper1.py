#!/usr/bin/env python

import sys

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
    print '%s\t%s' % (words[4], abs(int(words[2]) - int(words[3])))