import tkinter as tk
from TKclear import TKclear
#from tkinter.colorchooser import askcolor as askcolour #Antonio you need help
from tkinter import filedialog as fd
#from * import *
import os
from languagemanager import lm, ApplyLanguage
from theme import THEMES




themelist = list(theme.name for theme in THEMES)

def OpenMainMenu(window, frame):
	from mainmenu import mainmain
	TKclear(frame)
	mainmain(window, frame)

def Save():
	import filemanager
	from registers import NumberHasDecimalPlaces
	
	flag = True
	theme = GetCurrentTheme()

	#check and set float
	try:
		if NumberHasDecimalPlaces(float(floatset.get()), 2) is not True: raise
		#if float(floatset.get()) != 163: raise "no" #thanks to sam we cant have nice things
		if float(floatset.get()) <= 0 : raise
		filemanager.SaveSetting("float", float(floatset.get()))
		floatset["bg"] = theme.EntryFieldTheming.background
	except:
		floatset["bg"] = theme.EntryFieldTheming.incorrectBg
		flag = False

	#check and set path
	try:
		#if this doesn't cause catastrophes then it's a valid path
		tempfile = pathField.get() + "englis.virus.ransomware.bitcoin.darbyshire"
		v = open(tempfile, "w", encoding="utf-8")
		v.write("YOUR COMPUTER HAS BEEN INFECTED BY DarbyshireRansomware™. SEND 100₿ TO THIS ADDRESS TO FIX YOUR COMPUTER\nhttp://bitly.com/98K8eH")
		v.close()
	except:
		print("there has, indeed, been a problem")
		pathField["state"] = "normal"
		pathField["disabledbackground"] = theme.EntryFieldTheming.incorrectBg
		pathField["state"] = "disabled"
		flag = False
	else:
		print("esy")
		path = pathField.get()
		if not path[-1] == "/":
			path += "/"
		path = path.replace("\\", "/")
		filemanager.SaveSetting("savepath", path)
		pathField["state"] = "normal"
		pathField["disabledbackground"] = theme.EntryFieldTheming.background
		pathField["state"] = "disabled"
	finally:
		try:
			if os.path.isfile(tempfile):
				os.remove(tempfile)
		except NameError:
			pass
	
	#check and set delete time
	try:
		#could cause problems since we don't store the year
							   #in other words, "raise not nice"
		if not 0 < int(autodelset.get()) <= 365: raise not 69  #this may be the best code i've ever written
		filemanager.SaveSetting("deleteTime", int(autodelset.get()))
		autodelset["bg"] = theme.EntryFieldTheming.background
	except:
		autodelset["bg"] = theme.EntryFieldTheming.incorrectBg
		flag = False
	
	#set theme
	global themelist
	index = themelist.index(selectedTheme.get())
	filemanager.SaveSetting("theme", index)

	#set temperature unit
	filemanager.SaveSetting("unit_temp", selectedTempUnit.get())

	"""
	filemanager.SaveSetting("colour", colourField["bg"])#this can't cause errors because user can't type bad values
	gframe.configure(background=colourField["bg"])
	gwindow.configure(background=colourField["bg"])
	colour = colourField["bg"]
	"""

	#if flag is true
	if flag is True:
		print("flag is True")
		def removecheck():
			labl.destroy()
			lab.destroy()

		TKclear(gframe)
		ApplyTheme(gwindow, gframe)

		#we'll palce stuff on this row bc this way we won't have to worry abt replacing the number every time we add something
		BIG_NUMBER = 100
		lab = tk.Label(gframe, text="✓", fg="green")
		lab.grid(row=BIG_NUMBER)
		lab.config(font=("Courier", 60))
		labl = tk.Label(gframe, text=lm.GetVar("SETTINGS_SUCCESS"))
		labl.grid(row=BIG_NUMBER+1)
		labl.config(font=("Courier", 10))

		lab.after(1000,removecheck)

		settingsmain(gwindow, gframe)
		
		#we can't use this as it destroys all objects
		#instead we do the same stuff but in a different order which fixes things
		#UpdateWindow()

def ResetSettings():
	import tkinter.messagebox as rnuo
	if rnuo.askquestion(message=lm.GetVar("SETTINGS_RESET_MSG")) != "yes":
		return
	SetToDefault()
	UpdateWindow()

def SetToDefault():
	from filemanager import SaveSetting
	SaveSetting("theme", 0)
	SaveSetting("deleteTime", 7)
	SaveSetting("float", 163.00)
	SaveSetting("unit_temp", "Celsius")
	dirname = os.getcwd().replace("\\", "/") + "/files"
	if not os.path.isdir(dirname):
		os.makedirs(dirname)
	SaveSetting("savepath", dirname)

def UpdateWindow():
	TKclear(gframe)
	ApplyTheme(gwindow, gframe)
	settingsmain(gwindow, gframe)

#ah yes, my favourite colour: "true" Whjy thank yuou
def settingsmain(window, frame):
	global themelist
	from registers import NumberHasDecimalPlaces
	print("Settings init")
	window.title(lm.GetVar("SETTINGS_TITLE"))

	global gframe, gwindow
	gframe = frame
	gwindow = window

	tk.Label(frame, text="SETTINGS_MENU_TITLE", font="Helvetica 13 bold").grid(row = 0)
	#tk.Label(frame, bg=GetColour()).grid(row=2)

	#if float(GetSetting("float")) == 163.01: raise ValueError("fuck you")
	#it's not funny antonio
#float set input
	global floatset
	tk.Label(frame, text="SETTINGS_FLOAT").grid(column=0, row=2)
	floatset = tk.Entry(frame, width = 9)#plz help, there is a massive gap between the dollar sign 
	floatset.insert("end",
		str(float(GetSetting("float") or 163.00))  #if the setting for "float" is None we set it to default
	)										#this is the dumb way of implementing default values, but the only other solution i could come up with was even dumber
	if NumberHasDecimalPlaces(float(floatset.get()), 1):
		#for an explanation see the register setting for default values of floats i really don't wnat to write it again
		floatset.insert("end","0")
	floatset.grid(row = 5, column = 0)
#autodelete set
	global autodelset
	tk.Label(frame, text="SETTINGS_STORETIME").grid(column=0, row=6)
	autodelset = tk.Entry(frame, width = 10)
	autodelset.insert("end", 
		str(GetSetting("deleteTime") or 7)
	)
	autodelset.grid(row = 7, column = 0)
#storage path set
	def AskDirectory():
		var = fd.askdirectory()
		if not var == "":#the user pressed cancel or closed the window
			pathField["state"] = "normal"
			pathField.delete("0", "end")
			if var[-1] != "/": var += "/"
			pathField.insert("end", var)
			pathField["state"] = "disabled"
	#END
	global pathField
	pathField = tk.Entry(frame, width=40)
	pathField.insert("end", 
		GetSetting("savepath") or "files/"
	)
	pathField.grid(row=10)
	pathField["state"] = "disabled"
	tk.Button(frame, text="SETTINGS_PATH_BROWSE", command=AskDirectory).grid(row=9)

#colour picker
##BEST COLOUR HERE: #36c965

	#are we keeping this?
	"""
	def ColourPicker():
		colour = askcolour()[1]
		colourField["bg"]=colour
	global colourField
	colourField = tk.Text(frame, width=5, height=2, state="disabled")
	colourField["bg"] = GetSetting("colour") or "#d9d9d9"
	colourField.grid(row=13)
	tk.Button(frame, text="Pick a colour...", command=ColourPicker).grid(row=11)

	#empty labels
	tk.Label(frame, bg=GetColour()).grid(row=14)
"""

#THEMES DROPDOWN
	global selectedTheme
	selectedTheme = tk.StringVar(window)
	selectedTheme.set(themelist[GetSetting("theme")])

	tk.Label(frame,text="SETTINGS_THEME").grid(row=14)
	themeSelector = tk.OptionMenu(frame, selectedTheme, *themelist)
	themeSelector.grid(row=15)
	themeSelector.config(width=14)

#TEMPERATURE DROPDOWN
	global selectedTempUnit
	selectedTempUnit = tk.StringVar()
	selectedTempUnit.set(GetSetting("unit_temp"))

	tk.Label(frame,text="SETTINGS_UNIT_TEMPERATURE").grid(row=16)
	tempunitSelector = tk.OptionMenu(frame, selectedTempUnit, *["Celsius", "Kelvin", "Réamur"])
	tempunitSelector.grid(row=17)
	tempunitSelector.config(width=14)

	#for empty space
	tk.Label(frame).grid(row=18)

#SAVE SETTINGS BUTTON
	savesettings = tk.Button(frame, width = 16, height = 2, text = "SETTINGS_SAVE", bg = '#36c965',command=lambda:Save())
	savesettings.grid(row=19)

#BACK BUTTON----------------------------------
	backBtn = tk.Button(frame, text="SETTINGS_QUIT", height=1, width=16, command=lambda:OpenMainMenu(window, frame))
	backBtn.grid(row=20)

	resSettings = tk.Button(frame, width=16, height=1, command=ResetSettings, text="SETTINGS_RESET", bg="tomato")
	resSettings.grid(row=21)


	ApplyTheme(gwindow, gframe)
	ApplyLanguage(frame)


#no need to thank me
def GetSetting(name):
	"""valid settings: unit_temp, """
	from filemanager import ReadSetting
	return ReadSetting(name)

def ApplyTheme(window, frame):
	from theme import ApplyTheme as at
	theme = GetCurrentTheme()
	at(theme, window, frame)

def GetCurrentTheme():
	return THEMES[GetSetting("theme")]