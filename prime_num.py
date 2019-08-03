n=int(input('enter the number'))
if n>1:
    for i in range(2,n+1):
        if n%i==0:
            break
    if n==i:
        print('number is prime number')
    else:
        print('number is not prime number')
else:             
     print('number is not prime number')