text=input('Enter the name:\n')
print(f"the name:{text} contains less then 10 charaters which is {len(text)}") if len(text)<10 else print(f"the name:{text} contains greater then 10 charaters which is {len(text)}")