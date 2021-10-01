import sys

n=int(sys.stdin.readline())

num = [0]*n

num = list(map(int,sys.stdin.readline().split( )))

num.sort()


sum=0
count=n

# first : n times, second : n-1 times ... and add all
for i in num :
    sum += i*count
    count -= 1

print(sum)