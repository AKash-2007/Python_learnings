a=input("Enter the sentence: ")
z=0
if len(a)%2==0:
    k=len(a)//2
else:
    k=len(a)
for i in range(1,k+1):
    z+=i
print("The Sum:",z)
    
