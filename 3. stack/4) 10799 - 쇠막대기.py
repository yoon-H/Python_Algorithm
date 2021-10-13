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
        #�� ��ȣ�� '����'�̸� ���� ���� = '(' ���� ���ϱ�
        if arr[idx-1] == '(':
            pop(stack)
            sum += len(stack)
        # ������ �� ������ ����
        else :
            sum += 1
            pop(stack)

print(sum)

