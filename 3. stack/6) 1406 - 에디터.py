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
    #������ �������� ���� �̵�
    if i[0] == 'L' :
        if len(Lstack) :
            push(Rstack, Lstack[len(Lstack)-1])
            pop(Lstack)
        else :
            continue
    #���� �������� ���� �̵�
    elif i[0] == 'D' :
        if len(Rstack) :
            push(Lstack, Rstack[len(Rstack)-1])
            pop(Rstack)
        else :
            continue
    #���� ���� pop
    elif i[0] == 'B' :
        pop(Lstack)
    #���� ���� push
    else :
        push(Lstack, i[2])

#���� �������� ���� �̵�
while len(Rstack) != 0 :
    push(Lstack, Rstack[len(Rstack)-1])
    pop(Rstack)

#���ļ� ���
print(''.join(Lstack))