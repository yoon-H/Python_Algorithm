import sys

def push(self,item) :
    self.append(item)

def pop(self) :
    del self[len(self)-1]

def peek(self):
    if len(self) ==0 :
        return -1
    else :
        return self[len(self)-1]

arr = list(sys.stdin.readline().rstrip())
stack = []
sum=0
for idx, i in enumerate(arr) :
    if i == '(' :
        push(stack, i)
    else :
        #전 괄호가 '열림'이면 스택 길이 = '(' 개수 더하기
        if arr[idx-1] == '(':
            pop(stack)
            sum += len(stack)
        # 닫으면 한 조각만 생김
        else :
            sum += 1
            pop(stack)

print(sum)

