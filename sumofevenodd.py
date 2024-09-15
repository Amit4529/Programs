j=0
for i in range(1,51,1):
    if((i%2)==0):
        j+=i
print("Sum of even numbers :- " , j)

k=0
for i in range(1,51):
    if((i%2)!=0):
        k+=i
print("Sum of odd numbers :- " , k)
    