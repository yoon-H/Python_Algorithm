import sys

testcase = int(sys.stdin.readline())
que=[]

for i in range(testcase) :
    que.append([])
    mark, loca = map(int ,sys.stdin.readline().split())
    que[i].append(mark)
    que[i].append(loca)

    seq = list(map(int, sys.stdin.readline().split()))
    que[i].append(seq)

result = [0]*testcase
for i in range(testcase) :
    count = 0
    query = 0
    while 1 :
        if query >= que[i][0] :
            query = 0
            continue

        elif max(que[i][2]) == que[i][2][que[i][1]] and query == que[i][1] :
            count +=1
            break

        elif que[i][2][query] == max(que[i][2]) :
            que[i][2][query] = -1
            query += 1
            count +=1
            continue
        else :
            query +=1
            continue
    print(count)


