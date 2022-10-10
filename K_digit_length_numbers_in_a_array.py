n,a=map(int,input().split())
l=list(map(int,input().split()))
k=[]
for i in l:
    c=0
    if(i<0):
        i=-1*i
    elif(i==0):
        i=1
    while(i>0):
        r=i%10
        c=c+1
        i=i//10
    k.append(c)
c=0
for i in range(0,len(k)):
    if(k[i]==a):
        c=c+1
print(c)