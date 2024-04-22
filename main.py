#To find factorial of given number
z=int(input("Enter the number: "))
x=1
for i in range(1,z+1):
    x*=i
print("The factorial of",z,"is",x)    
