a=len(input())
i=1
while(i<a):
    if a%i==0:
        print((a//2)**25)
        break
    i+=1
if i==a:
    print(a**3)
