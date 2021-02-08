#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.


def extraLongFactorials(n):
    a = 0
    result = 1
    while a < n:
        result = result*(result-a)
        a += 1
    print(result)


nn = int(input())
extraLongFactorials
