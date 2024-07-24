#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    n = len(p)  # number of towns
    m = len(y)  # number of clouds

    # Step 1: Calculate which towns are covered by each cloud
    cloud_coverage = [[] for _ in range(m)]
    town_covered_by = [[] for _ in range(n)]
    total_population = sum(p)

    for i in range(m):
        cloud_start = y[i] - r[i]
        cloud_end = y[i] + r[i]
        for j in range(n):
            if cloud_start <= x[j] <= cloud_end:
                cloud_coverage[i].append(j)
                town_covered_by[j].append(i)

    # Step 2: Calculate population covered by each cloud
    population_in_darkness = [0] * m
    population_single_covered = [0] * m
    sunny_population = total_population

    for i in range(m):
        for town in cloud_coverage[i]:
            population_in_darkness[i] += p[town]
            if len(town_covered_by[town]) == 1:
                population_single_covered[i] += p[town]

    # Step 3: Evaluate the effect of removing each cloud
    max_sunny_population = 0
    for i in range(m):
        max_sunny_population = max(max_sunny_population, sunny_population - population_in_darkness[i] + population_single_covered[i])

    return max_sunny_population

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
