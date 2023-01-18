# def sum(n):
#     if(n<=1):
#         return n
#     else:
#         return n+sum(n-1)

# print(sum(2))

def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)
        
print(recursive_factorial(3))
