def prime(i):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return 0
    else:
        return 1
n1=int(input())
n2=int(input())
a=n1+n2
for i in range(1,10):
    k=a+i
    if(prime(k)):
        print(i)
        break