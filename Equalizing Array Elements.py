import os
import sys

def minOperations(arr, threshold, d):
    dp = {}
    arr.sort()
    ans = sys.maxsize
    
    for x in arr:
        steps = 0
        current = x
        while True:
            if current not in dp:
                dp[current] = [0, 0]
                
            dp[current][0] += 1
            dp[current][1] += steps
            
            if dp[current][0] >= threshold:
                ans = min(ans, dp[current][1])
            
            if current == 0:
                break
            
            current //= d
            steps += 1
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = []

    for _ in range(arr_count):
        arr.append(int(input().strip()))

    threshold = int(input().strip())
    d = int(input().strip())

    result = minOperations(arr, threshold, d)

    fptr.write(str(result) + '\n')
    fptr.close()
