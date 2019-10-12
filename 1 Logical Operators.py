#Mark McCullough
#Discrete Mathematics Lab 1
#CSE 015_04L

#Question 1: Implement python functions for all logical operators:

# 1.1 AND (p and q)
def AND(p, q):
  if p and q:
    return True
  else:
    return False

# 1.2 OR (p or q)
def OR(p, q):
  if p or q:
    return True
  else:
    return False

# 1.3 IF (p -> q)
def IF(p, q):
  if p == True:
    return q == True
  else:
    return q == False

# 1.4 NOT (-p, -q)
def NOT(p):
  if p == True:
    return False
  else:
    return True
      
def NOT(q):
  if q == True:
    return False
  else:
    return True
  

# 1.5 IFF (p <-> q)    
def IFF (p, q):
  if p is q:
    return True
  else:
    return False
    
# Question 2:
# Give a prefix representation of a proposition, of the form prop = ('OR', True, False)
# Write a function named evaluate, which will evaluate the proposition
# You should use the functions defined in question 1
def evaluate(formula):
  op = formula[0]
  p = formula[1]
  q = formula[2]
  formula = (op, p, q)
  if op == AND:
    return AND(p, q), 1, 2
    p = formula[1]
    q = formula[2]
  if op == 'AND':
    return [AND(p, q), p, q]
  elif op == 'IF':
    return [IF(p, q), p, q]
  elif op == 'OR':
    return [OR(p, q), p, q]
  elif op == 'IFF':
    return [IFF(p, q), p, q]
  elif op == 'NOT':
    return [NOT(p), p]
    
# Question 3 (Challenge): Create a new version of your evaluate function, named evaluate_r, which also takes in a formula, but it is able to evaluate composite formulae, such as ('OR', ('NOT', True), ('AND', True, False))
# The example formula above is equivalent to (-True 'OR' (True 'AND' False)) in infix notationdef 
def evaluate_r(formula):
  if type(formula[1]) is type(True):
    op1 = formula[1]
  else:
    op1 = evaluate_r(formula[1])
  if formula[0] is 'NOT':
    return NOT(op1)
  else:
    if type(formula[2]) is type(True):
      op2 = formula[2]
    else:
      op2 = evaluate_r(formula[2])
  if formula[0] == 'AND':
    return (AND(p, q), p, q)
  elif formula[0] == 'IF':
    return [IF(p, q), p, q]
  elif formula[0] == 'OR':
    return [OR(p, q), p, q]
  elif formula[0] == 'IFF':
    return [IFF(p, q), p, q]
  elif formula[0] == 'NOT':
    return [NOT(p), p]  



print "Basic Operations Test"
print
p = True
q = False

print AND(p, q)
print OR(p, q)
print IF(p, q)
print IFF(p, q)
print NOT(p)
print NOT(q)

print
print "*" * 40
print

# Simple evaluation function (Question 2)
print "Simple Evaluation Function Test"
print
p = True
q = False
print "p =", p
print "q =", q
print
print "(p or q):   ", evaluate(('OR', p, q))
print "(p and q):  ", evaluate(('AND', p, q))
print "(p -> q):   ", evaluate(('IF', p, q))
print "(p <-> q):  ", evaluate(('IFF', p, q))
print "-p:         ", evaluate(('NOT', p, 0))
print
print "*" * 40
print

# Recursive evaluation function (Question 3)
print "Recursive Evaluation Function Test"
print
p = False
q = False
print "p =", p
print "q =", q
print
print "(p or q) or -p: ", evaluate_r(('OR', ('OR', p, q), ('NOT', p)))
print "(p or q) and -p: ", evaluate_r(('AND', ('OR', p, q), ('NOT', p)))
print
print "*" * 40
