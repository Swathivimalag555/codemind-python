n=int(input())
l=list(map(int,input().split()))
a=[]
for i in set(l):
    if (i%2==1):
        a.append(i)
print(sum(a))
        
    