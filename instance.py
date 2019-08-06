class Dog():
    def __init__(self, color, name):
        self.name = name
        self.color=color

    def display(self):
        print("Name: {}".format(self.name))
        print("Color: {}".format(self.color))
   
obj=Dog('tommy','brown') 
print(type(obj).__name__)