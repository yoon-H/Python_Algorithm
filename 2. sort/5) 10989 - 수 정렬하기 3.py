import sys

n= int(sys.stdin.readline())

arr=[0]*10000

for i in range(n) :
    num = int(sys.stdin.readline())
    #�ش� �ε����� ī����
    arr[num-1] = arr[num-1] +1

for i in range(10000) :
    if arr[i] != 0 :
        #����ִ� �縸ŭ ���
        for j in range(arr[i]) :
            print(i+1) 
