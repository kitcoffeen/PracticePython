gap = "\n" + "&" * 80 + "\n"
print gap

print """
  When a decision involves more that two independent choices, the command 
  elif (else/if) can be used.  Python will check the if-statement, then each 
  elif-statement in order.  If any are true, it will do the commands and skip 
  the rest.  If none of the if and elifs are true, it will follow the else 
  commands.
"""

print "Let's play roguish Rochambeau:"
pick = raw_input("\nType you choice (rock/paper/scissors) to begin:\n")

if pick.lower() == "rock":
  print "Slap, paper covers rock... You lose sucka!"
elif pick.lower() == "scissors":
  print "Bam!  Your scissors got crushed by my rock... Loser!"
elif pick.lower() == "paper":
  print "Snip, your paper got cut... Don't try to come at me with paper, bitch!"
else:
  print "\n%r, really?!  I guess you are too afraid or stupid to pick" % pick
  print "rock, paper, or scissors."
print gap

print """
  It is also possible to put if/elif statements inside of other if/elif
  statements.
"""

age = float(raw_input("How old are you?"))
gender = raw_input("Male or female?")
smoking = raw_input("Do you smoke?")

if gender.lower() == "m" or gender.lower() == "male":
  if smoking.lower() == "yes" or smoking.lower() == "y":
    print "You have about %s years left to live." % (70.1 - age)
  elif smoking.lower() == "no" or smoking.lower() == "n":
    print "You have about %s years left to live." % (80.1 - age)
  else:
    print "Sorry, %r is not recognized, please type 'yes' or 'no.'" % smoking
elif gender.lower() == "f" or gender.lower() == "female":
  if smoking.lower == 'yes' or smoking.lower() == "y":
    print "You have about %s years left to live." % (68.7 - age)
  elif smoking.lower() == 'no' or smoking.lower() == "n":
    print "You have about %s years left to live." % (78.7 - age)
  else:
    print "Sorry, %r is not recognized, please type 'yes' or 'no.'" % smoking
else:
  print "Sorry, %r is not recognized, please type 'male' or 'female'" % gender