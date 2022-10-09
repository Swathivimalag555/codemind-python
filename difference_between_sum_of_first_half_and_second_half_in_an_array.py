n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(0,n//2):
    a=a+l[i]
for j in range(n//2,n):
    b=b+l[j]
print(abs(a-b))