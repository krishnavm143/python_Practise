number=int(input("Enter the number to be factorial\n"))
facval=1
for i in range(1,number+1):
    facval=facval*i

print(f'the factorial value is : {facval}')
