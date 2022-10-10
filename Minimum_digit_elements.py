n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    while(i>0):
        r=i%10
        c=c+1
        i=i//10
    a.append(c)
print(a.count(min(a)))