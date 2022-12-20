n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        k=65
        print(chr(k+n-1),end=" ")
    n-=1
    print()