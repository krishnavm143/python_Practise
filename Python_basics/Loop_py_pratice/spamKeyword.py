text=input('Enter the text \n')
spam=False

if("make a lot of money" in text):
    spam=True
elif('buy now' in text):
    spam=True
elif('click this' in text):
    spam=True
elif('subscribe this' in text):
    spam=True
else:
    spam=False
print('the message is spam') if spam else print("the message is not spam")