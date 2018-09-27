#!/usr/bin/env python

import sys

for line in sys.stdin:
    try:
        data = line.strip().split(" ")
        file = data[6]
        print file
    except:
        raise Exception("offending: " + str(file))
