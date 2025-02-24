leap=int(input("Enter the year"))
if(leap%4==0 and leap%100!=0 or leap%400==0):
    print("year is a leap year")
else:
    print("year is not a leap year")
