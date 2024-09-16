st=int(input("Enter starting point:-"))
end=int(input("Enter ending point:-"))
upd=int(input("Enter updation:-"))
dir=input("Enter h for horizontal and v for vertical:- ")
order=input("Enput f for forward order and r for reverse order")
if(dir=='h'):
    if(order=='f'):
        for i in range(st,end+1,upd):
            print(i , end=" ")
    else:
        for i in range(end,st-1,-upd):
            print(i , end=" ")

elif(dir=='v'):
    if(order=='f'):
        for i in range(st,end+1,upd):
            print(i)
    else:
        for i in range(end,st-1,-upd):
            print(i)
