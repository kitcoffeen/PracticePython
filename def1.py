gap = "\n" + "><" * 40 + "\n"
print gap

print """
  The def function allows you to create a command that is made up of multiple
  commands.  The command takes the form def command(argument).  If no argument 
  is needed, it will take the form def command().
"""

def add():
  print "I can add any two numbers, watch:"
  a = int(raw_input("\nGive me a number> "))
  b = int(raw_input("\nGive me another number> "))
  c = a + b
  print "\nAnswer---> %d" % c 

add()
print gap

print """
  The command() can be called anywhere in a script.  Usually, they are all 
  listed near the top of the script instead of right before they are called.
  The argument in def command(argument) is not needed in many cases, but 
  comes in handy when variations on the command are useful.
"""

def gap(symbol):
  print "\n" + symbol * 80 + "\n"

gap("$")
print "I am above questions and below the money line."
gap("?")

print"""
  The def command(argument) can be as simple or complex as it needs to be to
  accomplish a goal.  You can use if/elif statements in these defs to great 
  effect.
"""

def gap(symbol):
  if len(symbol) == 1:
    print "\n" + symbol * 80 + "\n"
  elif len(symbol) == 2:
    print "\n" + symbol * 40 + "\n"
  elif len(symbol) == 3:
    print "\n" + symbol * 26 + "\n"
  elif len(symbol) == 4:
    print "\n" + symbol * 20 + "\n"
  else:
    print "\n" + "!" * 80 + "\n"

gap("I")
gap("do")
gap("not")
gap("like")
gap("failure")

print """
  Coders are lazy by nature.  I stopped the above def after 4 if/elif, even 
  though I needed 80 to cover all possible symbols.  Coders also hate messy code; 
  an elegant code (like an elegant theorem or theory) is one that accomplishes 
  the most with the fewest number of words or symbols.  Here are two "more elegant"
  versions of the above code I thought up in lieu of copying and pasting 80 times
"""

def gap(char):
  x = len(char)
  print "\n" + char * (80/x) + "\n"

gap("I")
gap("am")
gap("the")
gap("greatest!")

def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"

gap("1")
gap("line")
gap("from")
gap("160")