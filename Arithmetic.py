print("-"*20,"MY CALCULATOR","-"*20)
print(" "*10,"Type ' 1 ' if you want to Add.")
print(" "*10,"Type ' 2 ' if you want to Subtract.")
print(" "*10,"Type ' 3 ' if you want to Multiply.")
print(" "*10,"Type ' 4 ' if you want Divide with decimal.")
print(" "*10,"Type ' 5 ' if you want Divide without decimal.")
print(" "*10,"Type ' 6 ' if you want to power.")
print(" "*10,"Type ' 7 ' if you want remainder.")
print(" "*10,"Type ' 8 ' if you want to exit.")
z=1
while(z!=8):
    z=int(input("Enter your choice: "))
    print()
    print()
    if z==1:
        k=0
        a=1
        print("Enter the terms you want to add.")
        print("Type ' 0 ' to get the sum.")
        while(a):
            a=int(input())
            k+=a
        print("The Sum: ",k)
        print()
        print()
    elif z==2:
        a=int(input("Enter the number: "))
        k=int(input("Enter the number: "))
        d=a-k
        print("The Difference: ",d)
        print()
        print()
    elif z==3:
        k=1
        a=0
        print("Enter the terms you want to multiply.")
        print("Type ' 1 ' to get the product.")
        while(a!=1):
            a=int(input())
            k*=a
        print("The Product: ",k)
        print()
        print()
    elif z==4:
        a=int(input("Enter a numerator: "))
        k=int(input("Enter a denominator: "))
        print("The Quotient: ",a/k)
        print()
        print()
    elif z==5:
        a=int(input("Enter a numerator: "))
        k=int(input("Enter a denominator: "))
        print("The Quotient: ",a//k)
        print()
        print()
    elif z==6:
        a=int(input("Enter a base: "))
        k=int(input("Enter a power: "))
        print("The Power: ",a**k)
        print()
        print()
    elif z==7:
        a=int(input("Enter a numerator: "))
        k=int(input("Enter a denominator: "))
        print("The remainder: ",a%k)
        print()
        print()
    elif z==8:
        print("You're Welcome!!")
    else:
        print("Invalid Number")
        print("Execute the code again")
    

