def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"
gap("0")

print """
  In addition to python's many built-in commands, there are an endless number of 
  third-party commands that can be brought into python and used in your script.  
  Before importing these at the beginning of a script, they must be installed.  
  Python's installer is called pip.exe.  I reccommend keeping a file called
  "dependencies.txt" where you list every third-pary install, so if you ever 
  have to use another computer, you know exactly wat to install to be sure
  all of you code functions correctly.
"""
gap("0")
print """
  One very powerful third-party package is selenium.  It can open a web browser 
  and interact with the browser in powerful ways.  Documentation for seleium and 
  other packages are good, and a quick google search will help you find ways to 
  do particular things.  Here is a quick demonstration of using selenium to 
  open firefox and login to gmail (for now firefox seems to be selenium's most 
  compatible browser.)
"""

from selenium import webdriver   # if this fails, remember to install selenium
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1')
browser.implicitly_wait(10)  #ensures the browser loads before looking for content
username = browser.find_element_by_id('Email')
username.send_keys("youremail")
submituser = browser.find_element_by_css_selector("#next")
submituser.click()

browser.implicitly_wait(10)
password = browser.find_element_by_id("Passwd")
submit = browser.find_element_by_css_selector("#signIn")

password.send_keys("#pass")
submit.click()

gap("0")

print"""
  Another simple but useful tool is pyperclip.  It can copy text into your 
  clipbord and paste it somewhere else.  As basic as this sounds, think about
  how often your use copy and paste every time you use a computer.  Here is a
  quick example of how it can be useful:
"""

print """
  I can tell you how many letters are in anything.  Select any amount of text 
  and press ENTER to find out how many letters are in it.
"""

import pyperclip
print len(pyperclip.paste())