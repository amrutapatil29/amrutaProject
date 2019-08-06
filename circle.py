class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=3.14 * self.radius**2
        return a
    def perimeter(self):
        b=2 * 3.14 * self.radius
        return b   
x=int(input('enter radius:')) 

obj= circle(x)
print('area of circle is:',obj.area())
print('perimeter of circle is:',obj.perimeter())
