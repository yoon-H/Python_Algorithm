import sys

n, k= input().split()
n= int(n)
k= int(k)
que = [0]*n
idx = 0

for i in range(n) :
    que[i] = i+1

output = [0]*n

for i in range(n) :
    idx = idx + k-1
    if idx >= len(que) :
        idx = idx % len(que)
    output[i] = que[idx]
    del que[idx]
    
print('<',end="")
str_output = [str(a) for a in output]
print(", ".join(str_output),end="")
print(">")
