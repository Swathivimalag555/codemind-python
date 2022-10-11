n=int(input())
s=0
temp=n
while(n!=0):
    r=n%10
    s=s*10 + r
    n=n//10
n=temp
if(n==s):
    print(True)
else:
    print(False)
    