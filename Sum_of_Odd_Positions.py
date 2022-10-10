n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(1,n,2):
    a.append(l[i])
print(sum(a))