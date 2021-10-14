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
    #������ ��������� 0 �Է�
    result[idx] = 0

    #�������� �ְ����� ž�� �Է�
    while len(stack) :    
        if peek(stack) > i :
            result[idx] = stack[-1][1]
            break
        else :
            pop(stack)
    push(stack, [i, idx+1])     
    
#����Ʈ�� ���ļ� ���
print(" ".join(map(str, result)))    