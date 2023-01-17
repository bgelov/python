#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

nBin = (str(bin(n)[2:])).split("0")
result = max([len(nB) for nB in nBin])
print(result)