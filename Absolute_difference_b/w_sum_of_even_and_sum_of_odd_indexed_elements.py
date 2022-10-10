n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,n,2):
    a.append(l[i])
for j in range(1,n,2):
    b.append(l[j])
s1=sum(a)
s2=sum(b)
print(abs(s1-s2))