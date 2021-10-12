import sys

def push(self, item) :
    self.append(item)

def pop(self) :
    del self[len(self)-1]


n = int(sys.stdin.readline())

stack=[]

arr= [0]*n

for i in range(n) :
    arr[i] = int(sys.stdin.readline())

for i in arr :
    if i ==0 :
        pop(stack)
    else :
        push(stack, i)

print(sum(stack))