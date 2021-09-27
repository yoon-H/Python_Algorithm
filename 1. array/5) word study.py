import sys

word = sys.stdin.readline().rstrip()
alp = [0]*26
word = word.upper()
str = list(word)

for i in str :
    alp[ord(i)-65] +=1

max=0
count=0

for i in alp :
    if i > max :
        max = i

for i in range(len(alp)) :
    if alp[i] == max :
        count +=1


if count > 1 :
    print('?')
else :
    print(chr(alp.index(max)+65))