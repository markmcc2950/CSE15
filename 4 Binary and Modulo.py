import math

# 1. Create a function for modular addition
def modAdd(x, y, m):
  modAdd = (x+y)%m
  return modAdd
  
print "Question 1:"
print "7 + 9 (mod 11):\t\t\t", modAdd(7, 9, 11) # => 5
print "--------------------------------------------"
print

#---------------------------------------------------------------------#
# 2. Create a function for modular multiplication


def modTimes(x, y, m):
  modTimes = (x*y)%m 
  return modTimes
  
print "Question 2:"
print "7 * 9 (mod 11):\t\t\t", modTimes(7, 9, 11) # => 8
print "--------------------------------------------"
print

#---------------------------------------------------------------------#
# 3. Create a function for converting binary to decimal. Binary numbers are represented as strings of 1 and 0
def binToDec(n):
  z = [int(i) for i in str(n)]                    # Converts n to a list
  x = list(reversed(z))                           # Reverses the list z. This makes z[0] = z[n], easier for calculations of 1 * 2^z(n)
  a = 0                                           # Declare an initial value
  for y, i in enumerate(x):                       # Searches the reversed z list for any values equal to 1, if position 0, then y = n-1
    if i == 1:
      newList = pow(2,y)                         
      a += newList
  return a 

print "Question 3:"
print  "1010000100 in decimal:\t\t", binToDec('1010000100') # => 644
print "--------------------------------------------"
print 

#---------------------------------------------------------------------#
# 4. Create a function for converting decimal to binary. Binary numbers are represented as strings of 1 and 0
def decToBin(n):
  val = str(n%2)
  empty = str('')
  divide = n/2
  if n == 0: 
    return empty
  else:
    while n > 0:
      return decToBin(divide) + val

print "Question 4:"  
print "644 in binary:\t\t\t", decToBin(644) # => 1010000100
print "--------------------------------------------"
print

#---------------------------------------------------------------------#
# 5. Create a function for modular exponentiation. Your function should compute in a reasonable time for exponents on the order of 10 billion
def modExp(n, p, m):
  b = 1
  while b:
    if p == 0:
      break
    if p % 2 == 1:
      b = b * n % m
    p /= 2
    n = pow(n, 2, m)

  return b
  

print "Question 5:" 
print "3^644 (mod 645):\t\t", modExp(3, 644, 645) # => 36
print "3^9876543210 (mod 2017):\t", modExp(3, 9876543210, 2017) # => 1040
print "--------------------------------------------"
print

#---------------------------------------------------------------------#
# 6. Write a function to determine the last digit of an integer represented as a base raised to an exponent.
def lastDigit(base, exponent):
  x = decToBin(exponent)
  y = [int(i) for i in str(x)]
  z = list(reversed(y))
  a = 1
  myList = []
  myList2 = []
  for i,j in enumerate(z):
    if j == 1:
      myList.append(modExp(base,i,10))
    for k in myList:
      a = a * k
      myList2 = [int(i) for i in str(a)]
      b = len(myList2)

  return myList2[b-1]
    
  
print "Question 6:"  
print "Last digit of 7^56746365435748:\t", lastDigit(7, 56746365435748) # => 1




