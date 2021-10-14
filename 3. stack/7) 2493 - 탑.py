import sys

def push(self,item) :
    self.append(item)

def pop(self) :
    if len(self) :
        del self[-1]
    else :
        return -1

def peek(self) :
    if len(self) :
        return self[-1][0]
    else :
        return -1

n = int(sys.stdin.readline())
tower = map(int,(sys.stdin.readline().rstrip().split()))

stack =[]
result = [0]*n
for idx, i in enumerate(tower) :
    #스택이 비어있으면 0 입력
    result[idx] = 0

    #루프에서 최고점인 탑만 입력
    while len(stack) :    
        if peek(stack) > i :
            result[idx] = stack[-1][1]
            break
        else :
            pop(stack)
    push(stack, [i, idx+1])     
    
#리스트를 합쳐서 출력
print(" ".join(map(str, result)))    