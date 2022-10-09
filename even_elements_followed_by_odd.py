n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if(i%2==0):
        a.append(i)
for i in l:
    if(i%2==1):
        a.append(i)
for i in a:
    print(i,end=" ")