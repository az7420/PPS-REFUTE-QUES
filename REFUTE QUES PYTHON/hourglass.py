n=int(input("Enter no. of rows:"))
#For even number of rows
if n%2 == 0:
    #Upside down Triangle
    for i in range (int(n/2)):
        
        for k in range (0,i):
            print(end=" ")
        
        for j in range((int)(n/2) - i):          print("*", end=" ")
        if i != (int)(n/2)-1:
            print()

    #Straight Up Triangle
    for i in range((int)(n/2)+1):
        for k in range((int)(n/2) - i):
            print(end=" ")

        for j in range(i):
            print("*",end=" ")
        print()
#For odd Number of rows:
else:
    #Upside down Triangle
    for i in range (int(n/2)+1):
        
        for k in range (0,i):
            print(end=" ")
        
        for j in range((int)(n/2) - i + 1):
            print("*", end=" ")
        if i != (int)(n/2):
            print()

    #Straight Up Triangle
    for i in range(1,(int)(n/2)+2):
        for k in range((int)(n/2) - i + 1):
            print(end=" ")
