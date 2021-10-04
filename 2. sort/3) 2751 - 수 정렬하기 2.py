import sys

n= int(sys.stdin.readline())

num = [0]*n
for i in range(n) :
    num[i] = int(sys.stdin.readline())

num.sort()

for i in range(n) :
    print(num[i])