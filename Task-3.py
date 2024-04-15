a=int(input("Enter the number of terms: "))
k=0
print("Enter",a,"terms: ")
for i in range(1,a+1):
    ai=int(input())
    k+=ai
z=input("Enter 'A' if you want to get the Sum or Enter 'B' if you want to get the Average:")
if z=='A':
    print("The Sum:",k)
elif z=='B':
    print("The Average:",k/a)
else:
    print("Invalid Option")
