gap = "\n" + "#" * 80 + "\n"
print gap

print "Lists of strings are stored in variables like this:  fish = ['tuna', 'salmon', 'carp']"
fish = ['tuna', 'salmon', 'carp']
print "calling a certian item on the list is done like this: fish[1]"
print fish[1]
print "\t**Notice, the first element in the list is number 0"
print gap

print "A for-loop can be used to move through a list"
for element in fish:
  print "some fish are %s" % element
print gap

print "Lists of numbers are stored like this: fives = [5, 10, 15, 20, 25, 30]"
fives = [5, 10, 15, 20, 25, 30]
for i in fives:
  print i
print gap

print "The append function can be used to combine lists:"
fish.append(fives)
print fish
print gap

print "Append can be combined with a for-loop to make a list from a list"
integers = [1,2,3,4,5,6,7,8,9,10]

twos = []
for i in integers:
  twos.append(i * 2)

threes = []
for each in integers:
  threes.append(each * 3)

fives = []
for each_number in integers:
  fives.append(each_number * 5)

print integers
print twos
print threes
print fives
print gap

print "You can even put lists into lists and for-loops into for-loops!"
counts = [twos, threes, fives]
for each in counts:
  print "\nLook Ma, I can count by multiples"
  for i in each:
    print i
print gap