import tkinter as tk
import tkinter.messagebox as rnuo
from TKclear import TKclear
import os
import filemanager
from tkcalendar import Calendar
from languagemanager import lm, ApplyLanguage

#import * as *

def CloseMainMenu(frame):
	TKclear(frame)

#function called when pressing the "X" or "Quit" buttons
def Quit(window):
	#ask the user for confirmation
	#for messageboxes we immediately translate
	if rnuo.askquestion(title=lm.GetVar("QUIT_TITLE"), message=lm.GetVar("QUIT_MESSAGE")) == "yes":
		#code to execute upon exit goes here
		window.destroy()

#clear the window and call the settings menu
def OpenSettingsMenu(window, frame):
	from settingsMenu import settingsmain
	CloseMainMenu(frame)
	settingsmain(window, frame)

#clear the window and call the register menu
def OpenRegistersMenu(window, frame):
	from registers import registersmain
	CloseMainMenu(frame)
	registersmain(window, frame)

#tries to print today's thing, prints a fail notice if the document is not found
def Printer():
	print(not 69)
	fp = filemanager.GetTodaysFileWithPath()
	if not os.path.isfile(fp): #if there's no file for today display an error message
		rnuo.showerror(lm.GetVar("FILENOTFOUND_TITLE"), lm.GetVar("FILENOTFOUND_MESSAGE"))
		return
	print("sending to printer...")
	try:
		os.startfile(fp, "print")  #tries to print
	except Exception as e:
		print(e)
		rnuo.showerror(lm.GetVar("PRINTERROR_TITLE"), lm.GetVar("PRINTERROR_MESSAGE"))

def TickMark(frame):
	ROW=1
	lab = tk.Label(frame, text="✓", fg="green")
	lab.grid(row=ROW, rowspan=3, column = 1)
	lab.config(font=("Courier", 60))
	lab = tk.Label(frame, text="COMPLETE_MSG")		#for btns and labels we translatge at the end bc we have to aplly the theme
	lab.grid(row=ROW+2, rowspan=1, column = 1)
	lab.config(font=("Courier", 10))

def Weather(frame):
	from weather import weather as actual_weather8
	
	try:
		import your_own_goddamned_computer
	except:
		print("i can't so i'll steal samothy's")
	try:
		import Mikeal
		import dafydd
		import chakWang
	except:
		print("the police prevented us from importing some people. too bad!")

	return

	import settingsMenu as settings
	welist = actual_weather8(settings.GetSetting("unit_temp")[0], "Nanaimo")

	ROW, COLUMN = 1, 1

	from PIL import ImageTk, Image

	img = ImageTk.PhotoImage(Image.open("assets/icons/" + welist["icon"] + ".png"))
	panel = tk.Label(frame, image = img)
	panel.grid(row=ROW, column=COLUMN)#, rowspan=3, columnspan=2)

def Xmark(frame):
	ROW=1
	lab = tk.Label(frame, text="!", fg="yellow")
	lab.grid(row=ROW, rowspan=3, column = 1)
	lab.config(font=("Courier", 60))
	lab = tk.Label(frame, text="INCOMPLETE_MSG")
	lab.grid(row=ROW+2, rowspan=1, column = 1)
	lab.config(font=("Courier", 10))

# main function of mainmenu. called when we want to open mainmenu
def mainmain(window, frame):
	#initialise
	print("main menu init")
	window.title(lm.GetVar("MAIN_TITLE"))
	#window.config(bg = 'SkyBlue1')

#	frame.configure(background=settings.GetSetting("colour"))
#	window.configure(background=settings.GetSetting("colour"))

	#CHANGE THIS VALUE TO 0 FOR NORMAL USE
	#CHANGE THIS VALUE TO 1 FOR ALT MAIN MENU
	#CHANGE THIS VALUE TO 2 FOR ALT ALT MAIN MENU (MAIN MENU 3)

	#DEBUG = 2
	
	"""
	#window-----------------------------------------------
	if DEBUG == 0:
		#update registers button
		startBtn = tk.Button(frame, text="appleCopy", width=14, height=2, bd=0, bg="lavenderblush3", command=lambda:OpenRegistersMenu(window, frame))
		startBtn.pack()
		startBtn.grid(row=0, column = 0)

		#print button
		tk.Button(frame, text="Print", height=2, width=14, bd=0, bg="Cadet Blue", command=Printer).grid(row=1, column = 0)

		#settings button
		settingB = tk.Button(frame, text="Settings", height=2, width=14, bd=0, bg='dodgerblue', command=lambda:OpenSettingsMenu(window, frame))
		settingB.grid(row=2, column = 0)

		#quit button
		tk.Button(frame, text="Quit", width=14, height=2, bd=0, bg="red", command=Quit).grid(row=3, column = 0)

	#menu test---------------------------------------------------------
	elif DEBUG == 1:
		print('debugmode')
		#UI CLEANING THINGS
		#spacer button
		underbtnclr = 'steelblue'
		spacerBtn = tk.Button(frame, text = "", width = 58, height = 1, bd=0, state=tk.DISABLED)
		spacerBtn.grid(row=0,column=1)

		#the button under the other buttons
		BtnUnder = tk.Button(frame, text="", width=14, height=16, bd=0, bg=underbtnclr, state=tk.DISABLED)
		BtnUnder.grid(row=4, column = 0, sticky=tk.E)

		#the button by the button under the other buttons
		BtnUnderBtn = tk.Button(frame, text="", width=75, height=20, bd=0, bg=underbtnclr, state=tk.DISABLED)
		BtnUnderBtn.grid(row=5, column = 0, columnspan = 2, sticky=tk.N)

		#calendar placeholder
		calbtn = tk.Button(frame, text="", width=41, height=21, bd=0, bg='white', state=tk.DISABLED)
		calbtn.grid(row=1, column = 1, rowspan=6, sticky=tk.N)
		#update registers button
		startBtn = tk.Button(frame, text="Update Registers", width=14, height=2, bd=0, bg="lavenderblush3", command=lambda:OpenRegistersMenu(window, frame))
		startBtn.grid(row=0, column = 0, sticky=tk.E)

		#print button
		tk.Button(frame, text="Print", height=2, width=14, bd=0, bg="Cadet Blue", command=Printer).grid(row=1, column = 0, sticky=tk.E)

		#settings button
		settingB = tk.Button(frame, text="Settings", height=2, width=14, bd=0, bg='dodgerblue', command=lambda:OpenSettingsMenu(window, frame))
		settingB.grid(row=2, column = 0, sticky=tk.E)

		#quit button
		tk.Button(frame, text="Quit", width=14, height=2, bd=0, bg="red", command=Quit).grid(row=3, column = 0, sticky=tk.E)

	#MAIN MENU 3 TEST-------------------------------------------
		print('debugmode')
		#UI CLEANING THINGS
		#spacer button
	"""
	if True:
#		underbtnclr = 'steelblue'
		spacerBtn = tk.Button(frame, text = "", width = int(90), height = 1, bd=0, state=tk.DISABLED)
		spacerBtn.grid(row=7,column=1
		) #thanks Antonio 
		if False:
			spacerBtn2 = tk.Button(frame, text = "", width = 45, height = 1, bd=0, state=tk.DISABLED)
			spacerBtn2.grid(row=7,column=2)

		#the button under the other buttons
		BtnUnder = tk.Button(frame, text="", width=14, height=30, bd=0, state=tk.DISABLED)
		BtnUnder.grid(row=4, column = 0, sticky=tk.E)

		#update registers button
		# bg="lavenderblush3"
		startBtn = tk.Button(frame, text="START_BTN", width=14, height=2, bd=0, command=lambda:OpenRegistersMenu(window, frame))
		startBtn.grid(row=0, column = 0, sticky=tk.E)

		#print button
		# bg="Cadet Blue"
		tk.Button(frame, text="PRINT_BTN", height=2, width=14, bd=0, command=Printer).grid(row=1, column = 0, sticky=tk.E)

		#settings button
		#bg='dodgerblue'
		settingB = tk.Button(frame, text="SETTINGS_BTN", height=2, width=14, bd=0, command=lambda:OpenSettingsMenu(window, frame))
		settingB.grid(row=2, column = 0, sticky=tk.E)

		#quit button
		# bg="red"
		tk.Button(frame, text="QUIT_BTN", width=14, height=2, bd=0, command=lambda:Quit(window)).grid(row=3, column = 0, sticky=tk.E)
		
		from datetime import date
		today = date.today()
		"""
		#datelabel
		d1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][today.weekday()]
		d3 = "st" if today.day % 10 == 1 else "nd" if today.day % 10 == 2 else "rd" if today.day % 10 == 3 else "th"
		d2 = today.strftime("%B %d" + d3 + ", %Y")
		datelabel = tk.Label(frame, text="Today's date is: " + d1 + ", " + d2)
		datelabel.grid(row=4,column=1)
		#"\n\nCopyRight Ⓒ 2021 \nNoor, samothy, Antonio\nProprietary and Confidential\nAll #Rights Reserved",
"""
		#calendar
		cal = Calendar(frame, selectmode = 'none', year = today.year, month = today.month, day = today.day)
		cal.grid(row=4,column=1,rowspan=1)
		#----------------------------------------------------

	if filemanager.FileForTodayExists() == True:
		TickMark(frame)
	else:
		print('do work')
		Xmark(frame)
	
	import settingsMenu as settings
	settings.ApplyTheme(window, frame)
	ApplyLanguage(frame)

	#weather has to be done after everythinf becasue yes
	print("Beginning Weather sequence: ")
	Weather(frame)