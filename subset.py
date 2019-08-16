class sol:
    def __init__(self, l):
        self.l = l
    def subsets(self):
        sb = self.subsets =[[]]
        for i in range(len(self.l)+1):
            print("i:",i)
            for j in range(i+1,len(self.l)+1):
                print("j:",j)
                a=self.l[i:j]
                sb.append(a)
         
        return sb
    
l=[4,5,6]
obj = sol(l)
print(obj.subsets())