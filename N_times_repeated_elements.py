n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
c=0
for i in l:
    if (i in a):
        continue
    else:
        a.append(i)
for i in a:
    if(l.count(i)==k):
        c=c+1
        print(i,end=" ")
if(c==0):
    
    print("-1")
    