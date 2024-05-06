a=len(input())
i=2
while(i<a):
    if a%i==0:
        print((a//2)**2)
        break
    i+=1
if i==a:
    print(a**3)
