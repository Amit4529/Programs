st=int(input("Enter starting point:-"))
end=int(input("Enter ending point:-"))
upd=int(input("Enter updation:-"))
dir=input("Enter h for horizontal and v for vertical:- ")
if(dir=='h'):
    for i in range(st,end+1,upd):
        print(i , end=" ")
else:
    for i in range(st,end,upd):
        print(i)