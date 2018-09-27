#!/usr/bin/env python

import sys

for line in sys.stdin:
    try:
        data = line.strip().split(" ")
        ip = data[0]
        print ip
    except:
        raise Exception("offending: " + str(ip))
