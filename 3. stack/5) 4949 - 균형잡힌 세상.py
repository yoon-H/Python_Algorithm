import sys

def push(self, item) :
    self.append(item)

def pop(self) :
    if len(self) ==0 :
        return False
    else :
        del self[len(self)-1]
        return True

def peek(self) :
    if len(self) ==0 :
        return -1
    else :
        return self[len(self)-1]


arr = []

while True :
    arr.append(list(sys.stdin.readline().rstrip()))
    if arr[len(arr)-1][0] == '.' :
        pop(arr)
        break


for i in range(len(arr)):
    stack =[]
    for j in arr[i] :
        result = True
        if j == '(' or j=='[' or j==')' or j==']' :
            if j == '(' or j== '[' :
                push(stack, j)
            elif j == ')' and peek(stack) == '(' :
                pop(stack)
            elif j == ']' and peek(stack) == '[' :
                pop(stack)
            else :
                print('no')
                result =False
                break
        else :
            continue
        
    #break를 만나면 출력 없이 다음 루프
    if result == False :
        continue
    else :
        if len(stack) :
            print('no')
        else :
            print('yes')
