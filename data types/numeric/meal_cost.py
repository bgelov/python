#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total_cost = 0
    total_cost = meal_cost + meal_cost / 100 * tip_percent + meal_cost / 100 * tax_percent
    total_cost = round(total_cost)
    print(total_cost)
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
