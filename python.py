#printing a box using stars
def fun(n):
  for i in range(n): #for rows
      for j in range(n): #for columns 
          print("*",end="") #end keyword will print the * in a single row 
        
        print() #this line take us to next line
fun(4)
