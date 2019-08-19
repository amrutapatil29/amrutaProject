s1=input('enter the string')
d={}
for i in s1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1    
print(d)        