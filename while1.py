def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"
gap("#|")

print """
  A while-loop is similar to a for-loop, but begins with a boolean  as in an 
  if-statement.  Python follows the instructions below the while-statement, 
  and then returns to the beginning to see if the while statement is still true.
  If it is true, the instructions are followed again.  This continues until the
  boolean is false.  This means a while statement will continue forever unless 
  the while loop is designed to eventually make the boolean false.
"""

print "Here is a while-loop that will go on forever:"

# x = 1
# while x > 0:
#   x = x + 1
#   print "\n x is now %d" % x
#   z = raw_input("""
#   Press enter to see the next iteration.
#   Hold enter to see what would happen without this raw_input line
#   You have to break this program by pressing Ctrl+C 
#   or closing this window""")

gap("#|")

print """
  You have to comment out the while-loop above to continue; please note that a
  while loop that doesn't end can be dangerous.
"""
gap("#|")

print "Here is a similar while-loop that will end:"

x = 0
while x < 10:
  print "x is now %d" % x
  x = x + 1

gap("#|")

print """
  While-loops use this 'x = x + 1' so often, there is a shorthand: 'x += 1'
  Another symbol used in many while-loops is '!=' which means 'not equal to'
"""
x = 0
power2_list = []
while x != 10:
  powers = 2 ** x   # the ** symbol makes what follows an exponent
  print "2 to the %d power is %d" % (x, powers)  
  power2_list.append(powers)
  x += 1
  print power2_list, "\n"

print "\nFun fact, those are special numbers in binary, they are represented as:"
print"[0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]"
print power2_list
print """
  Each of these numbers represents a new 'bit' in binary in the same way 
  0, 1, 10, 100, 1000, each represent a new decimal place in base 10.  Each
  place in decimal is called a 'bit.'  Eight 'bits' make up one 'byte,' and
  one byte can be used to create (2**8) = 256 unique combinations.
"""
gap("#|")

