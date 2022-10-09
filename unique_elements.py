n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if (i in a):
        continue
    else:
        a.append(i)
for i in a:
    print(i,end=" ")