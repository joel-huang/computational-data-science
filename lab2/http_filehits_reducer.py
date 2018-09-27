#!/usr/bin/env python

import sys

existing_item = None
count = 0

# each line has a file.
for line in sys.stdin:
    current_item = line

    # if new key, track a new item, reset highest sale
    if existing_item != current_item:

        # print old values
        if existing_item:
            print existing_item, " ", count

        # track new values
        count = 0
    count += 1
    existing_item = current_item

if existing_item is not None:
    print existing_item, " ", count
