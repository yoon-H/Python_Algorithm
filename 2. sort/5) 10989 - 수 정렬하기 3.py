import sys

n= int(sys.stdin.readline())

arr=[0]*10000

for i in range(n) :
    num = int(sys.stdin.readline())
    #해당 인덱스에 카운팅
    arr[num-1] = arr[num-1] +1

for i in range(10000) :
    if arr[i] != 0 :
        #들어있는 양만큼 출력
        for j in range(arr[i]) :
            print(i+1) 
