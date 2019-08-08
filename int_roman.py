class Roman:
    def __init__(self,num):
        self.num=num 
    def conversion(self):    
          int = [ 1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 
                  1 ]
          rom = [ "M", "CM", "D", "CD",
                  "C", "XC", "L", "XL",
                  "X", "IX", "V", "IV",
                  "I" ]
          roman_num = ''
          i = 0
          while self.num > 0:
            for j in range(self.num // int[i]):
                roman_num += rom[i]
                self.num -= int[i]
            i += 1
          return roman_num
x=int(input('enter the numbre:'))
a = Roman(x)
print(a.conversion())
  