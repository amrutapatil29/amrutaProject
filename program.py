s = input("Input a string:")
count1=0
count2=0
for i in s:
    if i.isdigit():
        count1+=1
    elif i.isalpha():
        count2+=1
    else:
        pass
        

print("Letters", count1)
print("Digits", count2)
