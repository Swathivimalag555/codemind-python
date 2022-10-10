n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    s=0
    while(i>0):
        r=i%10
        s=s*10+r
        i=i//10
    a.append(s)
for i in a:
    print(i,end=" ")