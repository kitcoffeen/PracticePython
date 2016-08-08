gap = "\n" + "^" * 80 + "\n"
print gap

print """
  An if-stament looks to a boolean value to see if it is true or false.  If the
  the boolean is true, python follows the instructions of the indented line(s)
  below.  If false, python skips those steps.
"""

age = int(raw_input("How old are you? > "))

if age > 30:
  print "\nNevermind, you are too old to be trusted."
if age < 30:
  print "\nGood, then let's talk"
print gap

print """
  If the if-statement is false and is followed by an esle-statement, python will 
  follow the commands after the else-statement.
"""
age = int(raw_input("How old are you? > "))

if age > 30:
  print "\nNevermind, you are too old to be trusted."
else:
  print "\nGood, then let's talk."
print gap

print """
  In boolean terms:
  True and True = True
  True and False = False
  False and False = False
"""
first = raw_input("First name? > ")
last = raw_input("Last name? > ")

if first == "Max":
  print "\nCool, we have the same name!"

if first == "Max" and last == "Coffeen":
  print "\n...wait, is this identity theft, or what?"
else:
  print "\nNice to meet you %s %s" % (first, last)
print gap

print """
  In boolean terms:
  True or True = True
  True or False = True
  False or False = False
"""
answer = raw_input("John has six slices of pizza.  "
  "What percent is left after he eats 3 slices? > ")
if answer =='50%' or answer = '50':
  print "\nCorrect!"
else:
  print "\nWrong!"
print gap
