import sys

n= int(sys.stdin.readline())

ans= [0 for i in range(n)]
for i in range(n) :
    ans[i]=list(sys.stdin.readline().rstrip())


for i in range(n) :
    point =1
    sum = 0

    for j in range(len(ans[i])) :
        if ans[i][j] == 'O' :
            sum += point
            point+=1
        else :
            point=1
        
    
    
    print(sum)

