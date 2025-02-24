num=int(input("Enter the number: "))
x=0
temp=num
while temp>0:
    y=temp%10
    x=x+y**3
    temp=temp//10
if(num==x):
    print("armstrong number")
else:
    print("not a armstrong number")
