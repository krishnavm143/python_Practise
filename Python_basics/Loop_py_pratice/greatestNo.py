num1=int(input('Enter the no1 :'))
num2=int(input('Enter the no2 :'))
num3=int(input('Enter the no3 :'))
num4=int(input('Enter the no4 :'))

if(num1>num2):
    f1=num1
else:
    f1=num2

if(num3>num4):
    f2=num3
else:
    f2=num4

if(f1>f2):
    print(str(f1)+' is the greatest')
else:
    print(str(f2)+" is the greatest")