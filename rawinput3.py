gap = "\n" + "*" * 80 + "\n"

print gap
print "Here is another way to get input from a user"
name = raw_input("Name? ")
age = raw_input("How old are you? ")
double_age = age * 2
print "Wow,", age, "is half-way to", double_age
print gap

print "The int() command converts a numerical string into an integer"
age = int(age)
double_age = age * 2
print "Wow,", age, "is half-way to", double_age
print gap

print "You can also use raw_input with variables as the prompt"
lie_prompt = "Hey %s, what's an age you have pretended to be? " % name
lie_age = raw_input(lie_prompt)
print "\nCome on %s, you look more like %r than %r" % (name, age, lie_age)
print "\t**Notice that %r can be used for both integers and strings,"
print "\t but strings are displayed in single quotes."
print gap