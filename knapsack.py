#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    
    # Iterate over each possible total sum from 1 to k
    for i in range(1, k + 1):
        # Iterate over each element in the array
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)
    
    # The value at dp[k] will be the answer
    return dp[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    results = []
    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)
        results.append(result)

    for res in results:
        fptr.write(str(res) + '\n')

    fptr.close()
