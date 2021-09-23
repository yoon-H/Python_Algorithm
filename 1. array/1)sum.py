import sys

n = int(sys.stdin.readline())

arr = int(sys.stdin.readline())
sum = 0
for i in range(n):
    sum += arr % 10
    arr = arr //10

print(sum)