n=int(input())
a=[]
for i in range(1,n):
    if(n%i==0):
        a.append(i)
if(n==sum(a)):
    print(True)
else:
    print(False)