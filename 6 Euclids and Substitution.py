# Exercise 1: Implement Euclid's Algorithm for finding the greatest common divisor of two integers
def gcd(a, b):                                      # A = (A/B) * B + A % B
    A = a
    B = b
    X = A % B
    myList = []
    if A % B == 0:
        return B
    while A % B != 0:
        X = A % B
        A = B
        B = X
    return B
        
print gcd(128,60)
# Expected output: 4



# Exercise 2: Consider the following representation of mathematical expressions: a list of tuples, where each tuple has exactly 2 elements, a
# coefficient and a term. For example, the expression:

# 2x + 5y - 3z is represented as [(2, x), (5, y), (-3, z)]

# We sometimes need to simplify expressions by grouping together like terms. For example:

# 2x + 5y + 4x = 6x + 5y

# Implement the function groupLikeTerms, where the input exp is a mathematical expression represented as a list of tuples, and it should return a
# simplified mathematical expression represented as a list of tuples.
def groupLikeTerms(exp):
    likeTerms = []                                  # The list used for like terms
    answer = []                                     # The list used for summing the values of like terms
    final = []                                      # The list used at the end of the code for the final answer
    for var in exp:                                 # Only adds variables to likeTerms list if not already there, prevents duplicates
        if var[1] not in likeTerms:
            likeTerms.append(var[1])
    for val in likeTerms:                           # Sums the totals for each specific variable set
        total = 0
        for var in exp:
            if var[1] == val:
                total += var[0]
        answer.append(total)
    for y in range(len(likeTerms)):                 # Appends the final list only for terms at equal position (0, 0), (1, 1), etc...
        for x in range(len(answer)):
            if x == y:
                final.append((answer[x], likeTerms[y]))
    return final

print groupLikeTerms([(5, "x"), (5, "y"), (-3, "x")])
# Expected output: [(2, 'x'), (5, 'y')]


    
# Exercise 3: We sometimes need to substitute expressions into other expressions. For example if we have the expression 2x + 5y, and we know that
# x = 3a - b, we can substitute the expression for x into the original expression, resulting in: 6a - 2b + 5y.

# Implement the substitution function below. It should take an expression (list of tuples), a term, and another expression. It should substitute the
# occurences of term in exp, with value. The result should be in its simplest form, i.e. like terms should be grouped together 

# For example: substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)]) results in [(-5, 9), (2, 23)]
def substitute(exp, term, value):
    valList = [value]
    newList = []
    list2 = []
    finalList = []
    badList = []
    for x in exp:
        if term == x[1]:
            for v in value:
                    a = x[0] * v[0]
                    b = a
                    newList.append(b)
    for i in range(len(newList)):
        for x in range(len(exp)):
            if x == i:
                list2.append((newList[i], exp[x][1]))
    for x, y in enumerate(list2):
        if y[1] == term:
            list2.append([y[0], value[x][1]])
    for x in list2:
        if x not in exp:
            finalList.append(x)
        else:
            badList.append(x)
    for x in exp:
        if x not in finalList:
            if x not in badList:
                finalList.append(x)
     
            
    return groupLikeTerms(tuple(finalList))
            
print substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)])
# Expected output: [(-5, 9), (2, 23)]



# Exercise 4: Using the functions you implemented above, implement the Extended Euclidean Algorithm, which returns the GCD of two integers a, and b,
# as a linear combination of a and b.

# For example: extended_euclid(101, 23) results in (1, [(22, 23), (-5, 101)]), where the GCD is 1 and it can be expressed as 22*23 - 5*101
def extended_euclid(a, b):
# --------------------------------------------------------- #
    A = a
    B = b
    X = A % B
    gcdList = [57]                                          # This section reuses Exercise 1's code to make a list so I can find the 2nd to last value
    Z = len(gcdList) - 1                                    # before the final GCD value used
    if A % B == 0:
        return B
    while A % B != 0:
        X = A % B
        A = B
        B = X
        gcdList.append(X)                                   # Gives a list based on each value leading to the GCD
# --------------------------------------------------------- #
    newList = []
    r = len(gcdList)
    for i in range(r-1):
        newList.append((gcdList[i-r], gcdList[i-(r-1)]))    # Makes a list of all the A & B values used in the GCD process
    GCD = gcd(a, b)
    return GCD, gcdList[Z-1], gcdList, newList 

print extended_euclid(101, 23)
# Expected output: (1, [(22, 23), (-5, 101)])



# Exercise 5: Use the Extended Euclidean Algorithm to implement the function for multiplicative inverses. As you know, a multiplicative inverse n
# modulo m is guaranteed to exist if n and m are relatively prime. If they are not, your algorithm should return None (which is the null value of Python),
# otherwise, if n and m are relatively prime, you should return the inverse of n modulo m.
def inverse(n, m):
    # Provide the correct implementation
    return n
    
print inverse(23, 101)
# Expected output: 22
