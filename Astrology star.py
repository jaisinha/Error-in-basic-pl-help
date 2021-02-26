n=int(input("The number of columns and rows to be inputed"))
bool=input("Enter a true(1) or false(0)")
if(bool==0):
    for i in range(1,n+1):
        for j in range(1,i+1):
            
            print("*",end=" ")
            print()
else:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            
            print("*",end=" ")
