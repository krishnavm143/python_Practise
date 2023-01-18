x=10
print(type(x))
a=2.5
print(type(a))
b="abc"
print(type(b))
x = 4j
print(type(x))
x=[1,2,4]
print(type(x))
x=(1,2,3)
print(type(x))
x={"name":'kiity',"age":20}
print(type(x))
x={'one',"two","three"}
print(type(x))
x=None
print(type(x))

# complex number are written with j as an imaginary part
x=1j
print(x)

# if u specify the data type use the constructor fucntion

x=str('krisna')
print(type(x))

x=bytes(5)
print(type(x))
print(x)

x=bytearray(5)
print(x)

x=memoryview(bytes(5))
print(x)

x=10
a=complex(x)
print(a)