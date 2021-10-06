import sys

n= int(sys.stdin.readline())

arr= [0]*n
for i in range(n) :
    arr[i] = list(map(int , sys.stdin.readline().split( )))

arr.sort(key=lambda x: (x[0], x[1]))

for i in range(n) :
    print(arr[i][0] ,arr[i][1])