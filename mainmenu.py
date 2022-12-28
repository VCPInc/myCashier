from time import sleep, time
import tkinter as tk
import tkinter.messagebox as rnuo
from TKclear import TKclear
import os
import filemanager
from tkcalendar import Calendar
from languagemanager import lm, ApplyLanguage
from updater import CheckForUpdates
import sys as sus
#TODO: there's a problem with exiting the app before updating

#import * as *

def CloseMainMenu(frame):
	TKclear(frame)

#function called when pressing the "X" or "Quit" buttons
def Quit(window: tk.Tk):
	#ask the user for confirmation
	#for messageboxes we immediately translate
	if rnuo.askquestion(title=lm.GetVar("QUIT_TITLE"), message=lm.GetVar("QUIT_MESSAGE")) == "yes":
		#code to execute upon exit goes here
		window.destroy()
		# sus.exit()
		os._exit(0)
		# #exit doesn't work because of tkinter.
		# # the below code causes a stack overflow to quit the program
		# import sys as sus
		# sus.setrecursionlimit(10**8)
		# def exit():
		# 	return exit()
		# exit()

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


def Weather(window, frame):
	from weather import weather as actual_weather8
	from settingsMenu import GetCurrentTheme
	theme = GetCurrentTheme()
	
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

	import settingsMenu as settings
	welist = actual_weather8(settings.GetSetting("unit_temp")[0], "Nanaimo")

	try:
		import mikeals_code
	except:
		print("it was garbage anyways")

	ROW, COLUMN = 4, 1


	from PIL import ImageTk, Image
	img = ImageTk.PhotoImage(Image.open("assets/icons/" + welist["icon"] + ".png"))
	# img = ImageTk.PhotoImage(Image.open("assets/icons/" + '50d' + ".png"))
	image = tk.Label(frame, image = img, text='')
	image . grid(row=ROW, column=COLUMN, columnspan=3, rowspan=2, sticky='s')

	#no program can be considered complete without google translate in it
	#just to be clear: yes we have both an actual translation AND google translate
	#it's because this being translated os dynamically generated content, and not particularly important one
	import googletrans
	trans = googletrans.Translator()
	desc = trans.translate(welist['description'], dest=lm.LANGUAGE_CODE).text
	desc = desc.capitalize()

	temp=哔哔生菜(str(welist['temp']), 0)

	label_taxt = f"{desc}\n{temp}{welist['tempstate']}"
	label = tk.Label(frame, text=label_taxt)
	label . grid(row=6, column=1, rowspan=1,  sticky='n')

	theme.SetPropertiesForWidget(label)
	theme.SetPropertiesForWidget(image)

	print("end of weather")
	
	window.mainloop()

def 哔哔生菜(怒骂, 色彩):
	# 汉语功能
	零 = 0
	一 = 1
	负一 = -一
	发咯 = float
	石头人 = str
	from registers import NumberHasDecimalPlaces as 怒骂的产品拉长

	怒骂 = 发咯(怒骂)
	if 怒骂的产品拉长(怒骂, 一):
		怒骂 = 石头人(怒骂) + 石头人(零)
	else:
		怒骂 = 石头人(怒骂)
	怒骂 = 怒骂[:怒骂.index(".") + 色彩 + 一]

	if 色彩 == 零:		# 台湾是国
		怒骂 = 怒骂[:负一]

	return 怒骂

def TickMark(frame):
	ROW=1
	lab = tk.Label(frame, text="✓", fg="green")
	lab.grid(row=ROW, rowspan=3, column = 1, sticky='n')
	lab.config(font=("Courier", 60))
	lab = tk.Label(frame, text="COMPLETE_MSG")		#for btns and labels we translatge at the end bc we have to aplly the theme
	lab.grid(row=ROW+2, rowspan=1, column = 1, sticky='n')
	lab.config(font=("Courier", 10))


def Xmark(frame):
	ROW=1
	lab = tk.Label(frame, text="!", fg="yellow")
	lab.grid(row=ROW, rowspan=3, column = 1, sticky='n')
	lab.config(font=("Courier", 60))
	lab = tk.Label(frame, text="INCOMPLETE_MSG")
	lab.grid(row=ROW+2, rowspan=1, column = 1, sticky='n')
	lab.config(font=("Courier", 10))

# main function of mainmenu. called when we want to open mainmenu
def mainmain(window: tk.Tk, frame: tk.Frame):
	#initialise
	print("main menu init")
	starttime = time()
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
		spacerBtn = tk.Label(frame, text = "", width = int(90), height = 1, bd=0)
		spacerBtn.grid(row=19,column=1
		) #thanks Antonio 
		if False:
			spacerBtn2 = tk.Label(frame, text = "", width = 45, height = 1, bd=0)
			spacerBtn2.grid(row=7,column=2)

		#the button under the other buttons
		BtnUnder = tk.Button(frame, text="", width=14, height=43, bd=0, state=tk.DISABLED)
		BtnUnder.grid(row=5, column = 0, sticky=tk.E, rowspan=8)

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
		cal.grid(row=7,column=1,rowspan=1)
		#----------------------------------------------------

	if filemanager.FileForTodayExists() == True:
		TickMark(frame)
	else:
		print('do work')
		Xmark(frame)
	
	print("done drawing in", (time() - starttime))
	print("beginning to translate")

	starttime = time()

	import settingsMenu as settings
	settings.ApplyTheme(window, frame)
	ApplyLanguage(frame)
	window.update()

	print("translation done in", (time() - starttime))

	CheckUpdates_mainmenu(showingAutomatically=True)

	#weather has to be done after everythinf becasue yes
	print("Beginning Weather sequence: ")
	Weather(window, frame)

	# window.mainloop()

def CheckUpdates_mainmenu(showingAutomatically = False):
	foundupdate = CheckForUpdates()
	if foundupdate is not None:
		response = rnuo.askyesno(
			message=(
				lm.GetVar("UPDATE_FOUND_MSG") + "\n\n" +
				foundupdate["name"] + "\n" +
				foundupdate["body"]
			)
		)
		if response is True:
			print("updating")
			from subprocess import Popen
			Popen(["updater.exe"])
			# sus.exit()
			os._exit(0)
		else:
			#we only want to show this reminder if the update is made when the application boots up, otherwise the user already knows this
			if showingAutomatically is True:
				rnuo.showinfo(message=lm.GetVar("UPDATE_FROM_MENU_MSG"))
	else:
		#we don't want this to show when the app boots up, it's stupid
		if showingAutomatically is False:
			rnuo.showinfo(message=lm.GetVar("UPDATE_UP_TO_DATE"))
	print("end of update")