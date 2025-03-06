#find the frequency of the words in a sentence EX: A cat is sitting on a mat
#convert a number in different forms 1) binary to decimal to octal to hexa vice versa 
#patterns using alphabets 
#printing 
def fun(n):
  for i in range(n):
    for j in range(i):
      print(chr(i+65),end='')
    print()
fun(5)
'''
A
AB
ABC
ABCD
'''
def fun(n):
  for i in range(n):
    for j in range(n,i,-1):
      print(" ",end='')
    for k in range(i+1):
      print(chr(i+65),end='')
    print()
fun(5)
'''
     A
    BB
   CCC
  DDDD
 EEEEE
 '''
def fun(n):
  for i in range(n):
    print(" "*n-i-1,end='')
    for j in range(2*i+1):
      print(chr(j+65),end='')
    print()
fun(3)
'''
  A
 ABC
ABCDE
'''
