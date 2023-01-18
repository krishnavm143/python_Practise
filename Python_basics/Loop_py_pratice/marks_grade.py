# marks=int(input("Enter the marks : \n"))

# if(marks>=90 and marks<=100):
#     print(f"You got {marks} in the subject and Ex grade")
# elif(marks>=80 and marks<=90):
#     print(f"You got {marks} in the subject and A grade")
# elif(marks>=70 and marks<=80):
#     print(f"You got {marks} in the subject and B grade")
# elif(marks>=60 and marks<=70):
#     print(f"You got {marks} in the subject and C grade")
# elif(marks>=50 and marks<=60):
#     print(f"You got {marks} in the subject and D grade")
# else:
#     print(f'sorry You got {marks} in the subject and F grade')

marks=int(input("Enter the marks : \n"))

if marks>=90 :
    grade='A'
elif marks>=80:
    grade='A'
elif marks>=70:
    grade='B'
elif marks>=60:
    grade='C'
elif marks>=50:
    grade='D'
else:
    grade='F'

print(f'Your grade is {grade}')
    