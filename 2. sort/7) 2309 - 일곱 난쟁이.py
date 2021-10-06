import sys

arr= [0]*9

for i in range(9) :
    arr[i] = int(sys.stdin.readline())

idx1 =0
idx2 =0

count = True
for i in range(9) :
    for j in range(i+1, 9) :
        if (sum(arr) - (arr[i]+arr[j])) == 100 :
            idx1= i
            idx2= j
            count=False
            break

    if count==False :
        break

del arr[idx1], arr[idx2-1]

arr.sort()

for i in range(len(arr)) :
    print(arr[i])


