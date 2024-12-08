b=1;
n=int(input("Enter Number of rows: "))
#Printing the First row
print(b)
previous=1
#Number of rows
for i in range(1,n-1):
    #Printing the first element of the next row
    print(b,end=" ")
    for j in range(i):
        #incrementing the value according to bell triangle logic
        next=previous+b;
        #Printing the next element of the same row
        print(next,end=" ")
        #updating the values for next itereation
        previous=b;
        b=next; 
    #Changing line
    print()
