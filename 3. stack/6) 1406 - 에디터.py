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


Lstack = []
Rstack = []

str = sys.stdin.readline().rstrip()

for i in str :
    push(Lstack, i)

n = int(sys.stdin.readline())

command=['']*n

for i in range(n) :
    command[i] = list(sys.stdin.readline().rstrip())

for i in command :
    #오른쪽 스택으로 문자 이동
    if i[0] == 'L' :
        if len(Lstack) :
            push(Rstack, Lstack[len(Lstack)-1])
            pop(Lstack)
        else :
            continue
    #왼쪽 스택으로 문자 이동
    elif i[0] == 'D' :
        if len(Rstack) :
            push(Lstack, Rstack[len(Rstack)-1])
            pop(Rstack)
        else :
            continue
    #왼쪽 스택 pop
    elif i[0] == 'B' :
        pop(Lstack)
    #왼쪽 스택 push
    else :
        push(Lstack, i[2])

#왼쪽 스택으로 전부 이동
while len(Rstack) != 0 :
    push(Lstack, Rstack[len(Rstack)-1])
    pop(Rstack)

#합쳐서 출력
print(''.join(Lstack))