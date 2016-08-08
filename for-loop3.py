gap = "\n" + "@" * 80 + "\n"
print gap

print "The boolean '==' tests the truth of a given condition\n"
print "green" == "green"
print 20 == 19
x = 9
print x == 9
print "god" == "God"
print "\t**Notice that boolean values are case-sensitive"
print gap


print """
  Let's combine some stuff we've learned to create a test for the user
  that can be graded automatically.
  """
print gap

print "\t***  Are you smart?  Let's see  ***\n\n"
print "Please type a single word that best answers each of the following:\n"
answers = []
answers.append(raw_input("\nWhat color does chlorophyl make plants? > "))
answers.append(raw_input("\nWhat body sits at the center of our solar system? > "))
answers.append(raw_input("\nWhich is the largest ocean? > "))
answers.append(raw_input("\nWhich is the smallest continent? > "))
answers.append(raw_input("\nWhat is the capital of Arizona? > "))
key = ['green', 'Sun', 'Pacific', 'Australia', 'Phoenix']

print gap
pause = raw_input("Press enter to see your results")
print gap
print """
  Thanks for taking the test.  Here are your results.
  If you don't like your score, next time caplitalize 
  proper nouns you dunce.\n\n
"""

for i in range(len(key)):
  print i + 1 ," You said %r The correct answer was %r" % (answers[i], key[i]) 
  print "\n\n\tWere you correct?--->", answers[i] == key[i], "\n\n"
print gap