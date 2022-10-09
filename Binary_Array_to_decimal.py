n=int(input())
l=list(map(int,input().split()))
l.reverse()
m=0
for i in range(0,n):
    if (l[i]==0):
        continue
    else:
        m=m+2**i
print(m)