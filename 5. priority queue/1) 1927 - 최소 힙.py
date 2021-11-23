import sys
import heapq

n = int(sys.stdin.readline())

command = [0]*n

for i in range(n) :
    command[i] = int(sys.stdin.readline())

heap = []
heapq.heapify(heap)


for i in command :
    if i == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap, i)