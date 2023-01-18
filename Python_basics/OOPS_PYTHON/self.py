class Employee:
    company="google"

    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
        print('Employee is created')
    
    def getDetails(self):
        print("name",self.name)
        print("salary",self.salary)
        print("age",self.age)
    @staticmethod
    def getSalary():
        print("100")

 
krishna = Employee("krishna",10000,27)
krishna.getSalary()
krishna.getDetails()
