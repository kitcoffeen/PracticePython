gap = "\n" + "$" * 80 + "\n"

print gap
print "The range() function can be used to specify a certain interval."
for i in range(0,7):
  print i

print "\t**Notice that range(0,7) begins at 0 and stops before 7"
print gap


print "The range() function can be applied to lists to select specified items."
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print "If we want just the first 10 letters, we can do this:"
for i in range(0, 10):
  print letters[i]

print "\nOr simply this:"
for i in range(10):
  print letters[i]

print """
  **Do you see now why the intervals include 0 and stop short of the 
  last number?
"""
print gap

print "The len() function counts the number of elements in a list"
print "\nThere are %d letters in the alphabet" % len(letters)
print gap

print """
  The len() and range() functions can be combined to iterate through a whole 
  list in a for-loop.  This can be useful if you don't want to count a long 
  list or if a list of unknown length is gathered from a user.
  """
for i in range(len(letters)):
  print letters[i]
print gap

print "The range(len()) combo can also help you number a list"
for i in range(len(letters)):
  print i + 1,"--->", letters[i]
print gap