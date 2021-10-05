import sys

arr = list(map(int ,sys.stdin.readline().rstrip()))

arr.sort()

arr.reverse()

for i in arr :
    print(i,end='')