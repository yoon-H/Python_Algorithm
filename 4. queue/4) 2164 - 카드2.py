import sys
from collections import deque

n= int(sys.stdin.readline())

deq = deque([a for a in range(1,n+1)])

deqry = 0
while len(deq) > 1 :
    deq.popleft()
    deq.append(deq.popleft())
    

print(deq.popleft())