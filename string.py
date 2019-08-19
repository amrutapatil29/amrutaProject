s1=input('enter the string:')
a='ing'
if len(s1)<3:
    print(s1)
elif(s1[-3:]==a):
    print(s1+'ly')
else:    
    print(s1+a)