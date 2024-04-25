a=int(input())
k=list(input())
for i in range(a-1):
    k.remove(" ")
k.sort()
z=""
for i in range(a):
    z+=k[i]+" "
print(z)

