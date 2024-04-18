a=input("Enter a word: ")
if len(a)%3==0:
    print(a[::-1])
elif len(a)%2==0:
    print(a.upper())
else:
    print(a.lower())
