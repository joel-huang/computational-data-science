#!/usr/bin/env python

import sys

existing_item = None
highest_sale = 0

# each line has item, cost:
# Men's Clothing	214.05
# Women's Clothing	153.57
# ...
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    current_item, current_sale = data_mapped

    # if new key, track a new item, reset highest sale
    if existing_item != current_item:

        # print old values
        if existing_item:
            print existing_item, "\t", highest_sale

        # track new values
        highest_sale = 0
    existing_item = current_item

    if float(current_sale) > float(highest_sale):
        highest_sale = current_sale

if existing_item is not None:
    print existing_item, "\t", highest_sale
