#Mark McCullough
#Discrete Mathematics
#Lab Report 2
#CSE 015_04L

X = [1, 2]
Y = ['a', 'b', 'c', 'd']

def cartesian_product(X,Y):
  for i in X:
    for j in Y:
      print (i, j)
    
print "Cartesian Product of",X,"and",Y,"is:"
cartesian_product(X, Y)

def power_set(X):
  for o in range (0,len(Y)):
    print "{",Y[o],"}"
    for p in range (o,len(Y)):
      if Y[o] != Y[p]:
        print "{",Y[o],",",Y[p],"}"
      for q in range (p,len(Y)):
        if Y[o] != Y[p] and Y[o] != Y[q] and Y[p] != Y[q]:
          print "{",Y[o],",",Y[p],",",Y[q],"}"
        for r in range (q,len(Y)):
          if Y[o] != Y[p] and Y[o] != Y[q] and Y[o] != Y[r]:
            if Y[p] != Y[o] and Y[p] != Y[q] and Y[p] != Y[r]:
              if Y[q] != Y[o] and Y[q] != Y[p] and Y[o] != Y[r]:
                if Y[r] != Y[p] and Y[r] != Y[q] and Y[r] != Y[o]:
                  print "{",Y[o],",", Y[p],",",Y[q],",",Y[r],"}"
                  print "{","}"

print  
print "Power set of",Y,":"  
power_set(Y)

