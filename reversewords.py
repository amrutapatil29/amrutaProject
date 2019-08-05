class solution:
    def reverse_words():
        x=input('enter the string')
        x=x.split()
        x=x[-1::-1]
        y=' '.join(x)
        return y
obj=solution
print(obj.reverse_words())        