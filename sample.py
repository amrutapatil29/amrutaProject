def Sample_list(l1):
    x=[]

    for a in l1:

        if a not in x:

            x.append(a)
    return x
print(Sample_list([1,2,2,3,4,4,5,5,5,6,7]))
      