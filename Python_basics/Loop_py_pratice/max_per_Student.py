sub1=int(input('Enter the first subject marks \n'))
sub2=int(input('Enter the second subject marks \n'))
sub3=int(input('Enter the third subject marks \n'))

if(sub1<33 or sub2<33 or sub3<33):
    print('YOur are failed in any of the subject')
elif(((sub1+sub2+sub3)/3)<40):
    print('You are failed in avg marks')
else:
    print("You are passed")