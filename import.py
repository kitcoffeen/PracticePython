def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"


print"""
  In addition to creating commands (called methods in python), other people have
  written commands that you can bring into your script.  Many of these come with
  python, but to save memory they come compressed.  You must "unpack" the 
  package using the command "import method_name."  These imports are always 
  listed at the very first lines of the script.
"""
gap("*^")

print """ 
  The "os" package contains many useful commands similar to those you would use
  from the command line.  The command os.getcwd() = pwd, 
  os.chdir('path') = cd 'path', and os.listdir('path') = ls 'path'
"""

import os  #should be at the very top of the script

wd = os.getcwd()
print wd

ls_list = os.listdir(wd)  #  os.listdir creates a list without needing brackets
print ls_list

gap("*^")

def pwd():            # all defs should be immediately after all imports
  wd = os.getcwd()
  print wd

def ls():
  wd = os.getcwd()
  ls_list = os.listdir(wd)
  for i in range(len(ls_list)):
    print ls_list[i]

pwd()           #  here we actually call the created methods (run the commands)
print"\n"
ls()
print "\n"
gap("*^")


def cd(path):     #  this method requires a argument "path" because...
  print "\n"
  os.chdir(path)  #  os.chdir requires an absolute path as an argument
  pwd()
  ls()

new_path = raw_input("type an absolute path to see what the directory contains> ")
cd(new_path)

gap("*^")


