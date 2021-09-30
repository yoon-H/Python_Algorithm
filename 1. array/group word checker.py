import sys

n=int(sys.stdin.readline())

word=[0 for i in range(n)]

for i in range(n) :
    word[i] = list(sys.stdin.readline().rstrip())

sum = 0

for i in range(n):
    count = 0
    alp = []
    for idx, j in enumerate(word[i]) :
        if j not in alp :
            alp.append(j)
        else :
            if word[i][idx-1] != j :
                break
        count+=1
    if count == len(word[i]) :
        sum +=1
print(sum)