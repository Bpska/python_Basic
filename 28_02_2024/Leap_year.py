year=int(input("Enter the Year"))
if  yrar%4==0:
    if yrar%100!=0:
        print('Leap Year')
    elif yrar%400==0:
        print('Leap Year')
else:
   print('Not a Leap Year')