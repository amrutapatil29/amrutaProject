def fact():
    fact=1
    x=int(input('enter the number'))
    for i in range(2,x+1):
        fact=fact*i
    return fact
print('factorial is',fact())    
