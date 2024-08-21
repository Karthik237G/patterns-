#printing a box using stars
def fun(n):
  for i in range(n): #for rows
      for j in range(n): #for columns 
          print("*",end="") #end keyword will print the * in a single row 
        
        print() #this line take us to next line
fun(4)
##the same with while loop
def fun(n, i):
    while i < n:
        j = 0  # Reset j for each row
        while j < n:  # Change condition to j < n for n asterisks
            print("*", end="")
            j += 1
        i += 1
        print()  # Print newline after each row
fun(5, 0)
##the same with while loop
def fun(n,i):
    while i<=n:
        j=0
        while j<=i:
            print("*",end="")
            j+=1
        i+=1
        print()
fun(5,0)
#creating a right angled triangle using the stars
def fun(n):
    for i in range(n+1):
        for j in range(i):
            print(" *", end="")
        print()
fun(4)

#creating downward right angled triange
def fun(n):
    for i in range(n+1):
        for j in range(n-i):
            print(" *",end="")
        print()

fun(4)

#creating an equilateral triangle
def fun(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(" ", end="")
        for j in range(0,i,+1):
            print("* ", end="")
        print()
fun(6)

#printing hollow square
def fun(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1 or i==n or j==1 or j==n):
                print("*",end="")
            else:
                print(" ",end="")
        print()

fun(6)

#printing H using stars
def fun(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==n//2 or j==1 or j==n):
                print("*",end="")
            else:
                print(" ",end="")
        print()

fun(6)
