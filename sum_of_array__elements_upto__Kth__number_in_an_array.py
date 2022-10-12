n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in range(0,k):
    a.append(l[i])
print(sum(a))      