# class Calculator:
#     def __init__(self,num):
#         self.number=num
    
#     def square(self):
#         print(self.number**2)
    
#     def squareRoot(self):
#         print(self.number**.5)
    
#     def cube(self):
#         print(self.number**3)
    
# a=Calculator(10)
# a.cube()
# a.square()
# a.squareRoot()

class Sample:
    a="krishna"
    @staticmethod
    def greet():
        print(f'Hello {Sample.a}')

name=Sample()
print(Sample.a)
name.a="naveen"
print(name.a)
name.greet()
# print(Sample.a)
# print(Sample.a)


