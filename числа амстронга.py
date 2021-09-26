for i in range(1,10000):
    s=0
    k=i
    n=0
    l=0
    while k!=0:
        k=k//10
        n=n+1
    k=i
    while k!=0:
        l=k%10
        s=s+l**n
        k=k//10
    if i==s:
        print(s)
        
