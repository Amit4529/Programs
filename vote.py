print("Let's see you are Eligible for vote or not ")
a = int(input("Enter your age:- "))
if(a==18 or a>18):
    print("You are eligible for vote ")
    print("Press 1 For BJP \n Press 2 For Congress")
    vote=int(input())
    if(vote==1):
        print("Thnks For voting, You choosed BJP")
    elif(vote==2):
        print("Thnks For voting, You choosed Congress")
    else:
        print("Select valid option")
else:
    print("You are not eligible for vote")