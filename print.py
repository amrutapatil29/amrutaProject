for n in range(2,501):
    for i in range(2,n+1):
        if n%i==0:
            break
    if n==i:
       print(n)
   