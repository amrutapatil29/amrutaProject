def palindrome():
    s1=input('enter the string')
    s2=''
    for x in s1:
        s2=x+s2
    if s1==s2:
            print('string is palindrome')
    else:
                print('string is not palindrome')
    return s2
palindrome()