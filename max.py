def max_two(a,b):
    if a>b:
        return a
    else:
        return b
def max_three(a,b,c):
    return max_two(a,max_two(b,c))
print(max_three(50,100,30))
