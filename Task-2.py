a=input("Enter a word: ")
k=len(a)
b=1
if (k%2==0):
    z=k//2
else:
    z=k
for _ in a:
    print(b*z)
    b+=1
    
