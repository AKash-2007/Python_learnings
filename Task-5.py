a=input("Enter a sentence: ")
if (a.lower()).count("python")>=1:
    print(a[::-1])
elif (a.lower()).count("java")>=1:
    print(a.upper())
else:
    print(a.lower())
    
    
