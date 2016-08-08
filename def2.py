def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"



def rochambeau():
  gap("-----><----")
  print "\t\t\_/ Let's Play Roguish Rochambeau \_/"
  pick = raw_input("\n\t\tType you choice (rock/paper/scissors) to begin:\n\n\t\t\t\t>")

  if pick.lower() == "rock":
    print "\n\nSlap, paper covers rock... You lose sucka!"
    again = raw_input("\nplay again? (y/n) ?>")
    if again.lower() == "yes" or again.lower() == "y":
      rochambeau()
    else:
        print "\n\t\t\tThanks for losing!!"
  elif pick.lower() == "scissors":
    print "\n\nBam!  Your scissors got crushed by my rock... Loser!"
    again = raw_input("\nplay again? (y/n) ?>")
    if again.lower() == "yes" or again.lower() == "y":
      rochambeau()
    else:
        print "\n\t\t\tThanks for losing!!"
  elif pick.lower() == "paper":
    print "\n\nSnip, your paper got cut... Don't try to come at me with paper!"
    again = raw_input("\nplay again? (y/n) ?>")
    if again.lower() == "yes" or again.lower() == "y":
      rochambeau()
    else:
        print "\n\t\t\tThanks for losing!!"
  else:
    print "\n\n%r, really?!  I guess you are too afraid or stupid to pick\n" % pick
    print "rock, paper, or scissors."
    again = raw_input("\nplay again? (y/n) ?>")
    if again.lower() == "yes" or again.lower() == "y":
      rochambeau()
    else:
        print "\n\t\t\tThanks for losing!!"

rochambeau()
gap("-----><----")