#	"leave all hope, ye who enter"
#this is the worst code you'll ever see
#but it runs
#my grandma runs faster than this code
#all thanks to english.virus.ransomeware.bitcoin.darbyShire 


# import updater
#--------------------------------------------------------------------------------------------------------------------------------------
#hello my dear friend, I helped write this code many moons ago, then I and god understood how it worked, now, only god understands
#so as a warning to fellow programmers, Please update the counter after you have most certainly given up all will to live
TOTAL_HOURS_WASTED_HERE = 500
print("total hours wasted here:", TOTAL_HOURS_WASTED_HERE)
#**************************************************************************************************************************************
#***************************************************************************************************************************************


#TODO: some system for notifications from us
#TODO: something about the .version file not being found


#() #why
#　##＃これにレジスタの名前が続きます（例：「レジスターAの合計」）

# import dis
# dis.dis(dis.dis)

# f = open("assets", "r")
# print(f.read(-1))
# exit()

print("Thanks Noor")

# x = memoryview(bytes(69420))#ffs, who tf thought this was ok
# import thankYou
#x = memoryview(bytes(thankYou))

# import dis
# dis.dis(dis.dis)

#all the juicy imports
import mainmenu
import tkinter as tk
from mainmenu import Quit
from mainmenu import CheckUpdates_mainmenu as CheckForUpdates
import tkinter.messagebox as ms
import webbrowser
from languagemanager import lm
import settingsMenu as settings
import sys as sus
#import os
#from datetime import date

#from GODPROGRAMMING import LetThereBeFile
#LetThereBeFile(), exit()

#i found an arbitrary code execution exploit in our program lmao
# lm.GetVar("loadlang('ace2', False)")
#there's two actually
#i fixed both now
#nvm it can't be fixed
#and theres way more than two

#do not import weather

#one thing i REALLY don't like is that we're switching windows by calling functions over and over and over
#unless they actively try to break it, or unless they use it without closing it for years then it shouldn't cause catastrophes
#GENIUS IDEA THEN?? WHAT IF WE MAKE IT THAT THE PROGRAM FORCES THE USER TO RESTART THE WHOLE COMPUTER, JUST HAVE IT IMMEDIATLY EXECUTE OS.RESTART EVERYTIME THE QUIT BUTTON IS PRESSED. WE COULD ALSO ENSURE THAT THEY WONT JUST KEEP THE PROGRAM RUNNING WITHOUT QUITTING FOR A WHILE BY HAVING IT AUTOMATTICALLY EXECUTING OS.RESTART AT RANDOM INTERVALS THOUGHOUT THE DAY. I know Im a genius, thank me later.
#thank you noor
#what if we just install a custom version of linux mint or ubuntu on the computer that this will be needed on, then have this program automattically begin on startup in full screen mode, then it will have sudo permissions, so the quit button will shutdown the computer. Again, thank me later.
#thank you again noor
#thanks for thanking noor

#import thankYou  #it's very important that this stays here

#x = memoryview(thankYou)

class rickrollexception(Exception):
	def __init__(self):
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

"""
#this is the improved version. it changes dynamically every time it is run, making it an ever-changing and more fun experience for the user every time
class rickrollexception(Exception):
	def __init__(self):
		from time import sleep
		import random
		for i in range(int(random.random() * 15)):
			webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
			sleep(1 + random.random())
"""


def openreplit(name):
	"""Opens replit of a specific developer based on the name given, the name argument should be passed as a string, supported options include "NS" for Noor, "AL" for Antonio, "SW" for Sam, also, "about" opens the about the devs message box, while "vcp" opens the vcp messagebox Additionally, Passing "nice" to the function will result in a rickrollexception being raised.  Passing anything unsupported to the function results in either a ID10T error, A DKO error, or a PICNIC error. """

	if name == "NS":
		webbrowser.open("replit.com/@NoorSaroya"), print(
			"Opened Noor's replit")

	elif name == "AL":
		webbrowser.open("https://github.com/AlphaL64"), print(
			"Opened Antonios's thing")

	elif name == "SW":
		webbrowser.open("replit.com/@SamWiebe"), print("Opened Sam's replit")

	elif name == "nice":
		raise rickrollexception
		print('Never Gonna Give You Up!')

	elif name == 'about':
		ms.showinfo(message=lm.GetVar("ABOUT_DEVS_MSG")), print(
			"About the devs popup\n")

	elif name == 'vcp':
		ms.showinfo(
			message=lm.GetVar('ABOUT_VCPINC_MSG')), print("VCP inc popup\n")

	else:
		print(
			'It looks like an invalid parameter was passed to the function, one of the devs suffers from an ID10T impairment, it is likely a DKO error(defective keyboard operator), other possibilities include: \n Layer 8 issue: Biological interface error, Pebkac error(problem exists between keyboard and chair) or various other errors relating to shortage of memory, in the developer, not the system.'
		)
	#webbrowser.open will open a browser window to the os default browser and navigate to the link passed in the argument.
	# the print is soley for debugging as the console is never seen by the end user.
#END


def bugreport():
	"""Bug report function, the parameters are reserved for future use"""

	import datetime
	if datetime.date.today().month == 4 and datetime.date.today().day == 1:
		#it's showtime
		raise rickrollexception

	print("\nFirst of all, it's probably a feature not a bug\n")
	print("\nOpening Bug report menu...")
	ms.showerror(message=lm.GetVar("BUGREPORT_MSG"))
	print("Done, it should have opened Sucessfully!\n\n")


def CreateCreditsMenu():  #credits menu
	credits = tk.Menu(menubar)
	menubar.add_cascade(label=lm.GetVar('MENU_CREDITS'),
						menu=credits)  #name the menu

	#vcp inc main credits
	vcpInc = tk.Menu(credits)
	credits.add_cascade(label=lm.GetVar("VCPINC_NAME"),
						menu=vcpInc)  #this is the spacer at the top.
	vcpInc.add_command(label=lm.GetVar("NAME_NOOR"),
					   command=lambda: openreplit("NS"))
	#print(thankYou)
	vcpInc.add_command(label=lm.GetVar("NAME_ANTONIO"),
					   command=lambda: openreplit("AL"))
	vcpInc.add_command(label=lm.GetVar("NAME_SAM"),
					   command=lambda: openreplit("SW"))

	vcpInc.add_command(label=lm.GetVar("NAME_RICK"),
					   command=lambda: openreplit("nice"))


	#translators credits
	translators = tk.Menu(credits)
	credits.add_cascade(label=lm.GetVar("TRANSLATORS"), menu=translators)
	from languagemanager import languages, langmanager
	for language in languages:
		#we can't use the main language manager as that's set to english
		langmang = langmanager(languages[language])
		#we don't create a window if there's no credits
		if langmang.GetVar("TRANSLATOR") != "":
			text = langmang.GetVar("LANGUAGE_NAME") + " - " + langmang.GetVar("TRANSLATOR")
			_command = lambda:None
			#command is open the given link
			if langmang.GetVar("CONTACT_INFO") != "":
				_command = lambda page=langmang.GetVar("CONTACT_INFO"):webbrowser.open(page)
			
			#add it at the end
			translators.add_command(label=text, command=_command)
	#END TRANSLATION CREDIT

	#other stuff
	othercredits = tk.Menu(credits)
	credits.add_cascade(label=lm.GetVar("OTHER_THANKS"), menu=othercredits)
	othercredits.add_command(label="Dafydd Taylor - Production Design", command=lambda:webbrowser.open("replit.com/@DafyddTaylor"))
	othercredits.add_command(label="Chak Wang - Head of VCP inc. Chinese Division", command = lambda:( webbrowser.open("replit.com/@ChakWang"), print("oof")))


	#about messages
	credits.add_command(label=lm.GetVar("ABOUT_DEVS"),
						command=lambda: openreplit("about"))
	credits.add_command(label=lm.GetVar("ABOUT_VCP"),
						command=lambda: openreplit("vcp"))
	menubar.add_separator()


#END


#lang menu function
def createlangmenu():
	print("Lang menu init")
	langb = tk.Menu(menubar)
	menubar.add_cascade(label=lm.GetVar("LANGUAGE_TXT"), menu=langb)

	from languagemanager import languages, SetLanguage
	for language in languages:
		langb.add_command(
			label=(
				language
			),  #label is the name of the language in the language itself
			command=lambda language=language: SetLanguage(
				languages[language], window, frame
			)  #command takes as parameter the name of the file
			#this is so fucking stupid i hate lambdas so fucking much
		)
	menubar.add_separator()


#END

#we got japan
#works perfectly as you can see

def CreateUpdateMenu():
	menubar.add_command(label=lm.GetVar("MENU_UPDATE"), command=CheckForUpdates)	# showingAutomatically is false by default, so we don't need to pass an argument here
	menubar.add_separator()


def CreateHelpMenu():
	helpb = tk.Menu(menubar)
	menubar.add_cascade(label=lm.GetVar("MENU_HELP"), menu=helpb)

	helpb.add_command(
		label=lm.GetVar("HELP_GUIDE"),
		command=lambda: webbrowser.open(
			"https://docs.google.com/document/d/1rMopoiUosTWNzhmI6NOTJdxxQJxMxSCOjZbprwocihM/edit?usp=sharing"
		))
	helpb.add_command(label=lm.GetVar("HELP_BUG"),
					  command=bugreport)
	menubar.add_separator()


def CreateMenuBar():
	global menubar
	menubar = tk.Menu(window)
	window.config(menu=menubar)

	CreateCreditsMenu()
	createlangmenu()
	CreateUpdateMenu()
	CreateHelpMenu()


def main():
	global menubar, window, frame
	print("main init")
	print("Opening Tkinter Window...")
	window = tk.Tk()
	frame = tk.Frame(window)
	frame.pack()

	window.geometry(settings.GetCurrentTheme().GetWindowShape())
	
	from PIL import Image, ImageTk
	ico = Image.open('assets/myCashier.png')
	photo = ImageTk.PhotoImage(ico)
	window.wm_iconphoto(False, photo)

	print('Window opened Sucessfully!\n')

	window.protocol("WM_DELETE_WINDOW", lambda:Quit(window))  #to ask the user before quitting

	CreateMenuBar()

	mainmenu.mainmain(window, frame)  # this opens the mainmenu window

	window.mainloop()

	sus.exit(0)
	#os.reboot()		#nothing to see here#nice try
	#os.remove("*")		#again, nothing to see here#wow you think you are so funny
#print(type(type(type(type(type(type(type(type(type(type(type(type(type(type(type(type(type(type(type)))))))))))))))))))
#print(type(rickrollexception))
#print(type(main))
#print(type(__name__))
#print(type(print))


if __name__ == "__main__":  #this way it won't be triggered if it's just imported
	main()

"""
today = date.today()#date is first set. 
d1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][today.weekday()]
d3 = "st" if today.day % 10 == 1 else "nd" if today.day % 10 == 2 else "rd" if today.day % 10 == 3 else "th"
d2 = today.strftime("%B %d" + d3 + ", %Y")
d = tk.Label(
	window, text="Today's date is: " + d1 + ", " + d2 + 
		"\n\nCopyRight Ⓒ 2021 \nNoor, Sam, Antonio\nProprietary and Confidential\nAll Rights Reserved",
	pady = 200,
	bg=settings.GetColour()
)
d.pack()#temporarily commented out, we need this stuff only in the settings menu, not on the main menu
"""

#got it working! use this stuff for the autoclear
#for windows only:
#thankyou=input("Please press any key to continue(Except the power key......Antonio!)")
#print("Thank You", thankyou)

#while True:
#	work()
