#printing a box using stars
def fun(n):
  for i in range(n): #for rows
      for j in range(n): #for columns 
          print("*",end="") #end keyword will print the * in a single row 
        
        print() #this line take us to next line
fun(4)

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
  for i in range(n+1):
    print("",end="")
    for j in range (i):
      print(" *",end="")
    print()
    


      
