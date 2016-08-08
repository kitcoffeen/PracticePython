print "\nHere is another way to collect info with raw_input:\n"
first = raw_input("first name >")
last = raw_input("last name >")
eyes = raw_input("eye color >")
weight = raw_input("weight >")

print "\n\nHello " + first + last + ", I like your " + eyes + " eyes.  I bet you weigh about " + weight

print "\n\tThese plus signs can get to be too much, commas can be used in their place:"
print "\nHello ", first, last, ", I like your " , eyes, " eyes.  I bet you weigh about ", weight

print "\n\n\tConcatenating variables into strings is tedious, the precent sign can help"
print "\tPercent s is a symbol that indicates to python that a string variable %s should be inserted" % first

print "\n\tNow our code becomes:"
print "Hello %s %s, I like your %s eyes.  I bet you weight about %s" % (first, last, eyes, weight)

print "\nThis system may not seem much better now, but there is something to be said for having all"
print "the variables at the end so you don't have to search through the text to find which are being called.\n"

print "\nNotice that weight is a number, but percent s calls it as a string.  Raw_input stores all input as strings."
print eyes * 3
print weight * 3