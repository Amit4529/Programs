a=int(input("Enter a number to find factorial:- "))
product=1
if(a>0):
    for i in range(1,a+1):
        product=product *i
    else:
        print("Factorial = " , product)
elif(a==0):
    print("Factorial = " , 0)
else:
    print("Enter Positive values")