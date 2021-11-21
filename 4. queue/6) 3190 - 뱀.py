import sys
from collections import deque


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

apple = ['']*k

for i in range(k) :
    apple[i] = list(map(int, sys.stdin.readline()))

L = int(sys.stdin.readline())
change = ['']*L

for i in range(L) :
    change = list(map(sys.stdin.readline()))

