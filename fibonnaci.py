num=int(input("Enter a number: "))
a,b=0,1
for i in range(num):
    print(a)
    a,b=b,a+b
print(num)
