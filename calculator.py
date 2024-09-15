a=int(input("Enter a number"))
b = int(input("Enter a number"))
c=input("Enter operator(+,-,*,/)")
if(c=='+'):
    print("Sum of both numbers is :- ", a+b)
elif(c=='-'):
    print("Subtraction of both numbers is:- " , a-b)
elif(c=='*'):
    print("Multiplication of both numbers is :-" , a*b)
elif(c=='/'):
    print("Division of both numbers is:- " , a/b)
else:
    print("Enter valid operator")
