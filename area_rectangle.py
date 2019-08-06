class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        a=self.length*self.width
        return a
x=int(input('enter lenghth:')) 
y=int(input('enter width:'))
obj= Rectangle(x,y)
print('area of rectangale is:',obj.area())