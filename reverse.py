def reverse():
    s1=input('enter string')
    s2=''
    for x in s1:
        s2=x+s2
    return s2
print('s2=',reverse())    