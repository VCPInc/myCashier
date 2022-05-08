import tkinter as tk
from enum import Enum

#enum representing all possible text alignments because tkinter sucks
class TextAlignment(Enum):
	center = "center"
	left = "left"
	right = "right"
#enum representing all possible relief modes because tkinter sucks
class ReliefMode(Enum):
	flat = "flat"
	sunken = "sunken"
	raised = "raised"
	groove = "groove"
	ridge = "ridge"
#enum representing all possible cursors because tkinter sucks
class Cursor(Enum):
	text="xterm"
	arrow="arrow"
	circle="circle" #no shit
	clock="clock"
	cross="cross"
	dotbox="dotbox"
	exchange="exchange"
	fleur="fleur"
	heart="heart"
	man="man"
	mouse="mouse"
	pirate="pirate"
	plus="plus"
	shuttle="shuttle"
	sizing="sizing"
	spider="spider"
	spraycan = "spraycan"
	star="star"
	target="target"
	tcross="tcross"
	trek="trek"

#from the above we can conclude that tkinter sucks yet, here we are using it anyway
#because we have to



#types to be used in the thing
validTypes = [ tk.Button, tk.Entry, tk.Label, tk.Checkbutton, tk.OptionMenu ]

#i hate classes in python
class Theme:
	"""
	Data container for a window theme\n
	
	Contains different methods, like:\n
	+ test
	"""

	class LabelTheme:
		"""Theme data for a Label"""
		textcolour = "#000000"
		font = None

		def __init__(self, fg = "#000000", font = None):
			self.font = font
			self.textcolour = fg
	#END CLASS
	class ButtonTheme:
		"""Theming data for a Button widget"""
		background = "#d9d9d9"
		textcolour = "#000000" #aka black
		activebg   = "#d9d9d9"
		activetext = "#000000"
		highlightcolour = "#d9d9d9"
		disabledfg = "#111"
		image = None  #if none, it won't add the image

		#textalignment = TextAlignment.center

		borderwidth = 2
		relief = ReliefMode.raised

		font = None #if none will just use default of the Theme

		def __init__(self, bg = "#d9d9d9", fg = "#000000", abg = "#d9d9d9", afg = "#000000", dfg = "#111", hl = "#d9d9d9", img = None, reliefMode=ReliefMode.raised, bd = 2, font = None):
			self.background = bg
			self.textcolour = fg
			self.activebg = abg
			self.activetext = afg
			self.highlightcolour = hl
			self.image = img
			self.borderwidth = bd
			self.relief = reliefMode
			self.font = font
			self.disabledfg = dfg
	#END CLASS

	class FieldTheme:
		"""Theming data for an Entry Field widget"""
		background = "#d9d9d9"		#normal background
		textcolour = "#000000"		#normal text colour
		activebg   = "#d9d9d9"		#background when you're typing
		activetext = "#000000"		#text colour when you're typing
		highlightcolour = "#d9d9d9"	#i have no idea what this is
		disabledbg = "#dbdbdb"		#disabled background
		disabledfg = "#111"			#disabled text colour

		incorrectBg = "#ff0000"		#colour of the field when the data you entered is invalid

		#textalignment = TextAlignment.left

		borderWidth = 2
		activeborderwidth = 1
		relief = ReliefMode.sunken
		cursor = Cursor.text		#how the cursor looks when hovering over it

		font = None

		def __init__(self, bg = "#d9d9d9", fg = "#000000", abg = "#d9d9d9", afg = "#000000", dbg = "#dbdbdb", dfg = "#111", incorrectBG = "#FF0000", hl = "#d9d9d9", cur=Cursor.text, img = None, reliefMode=ReliefMode.sunken, bd = 2, abd=1, font = None):
			self.background = bg
			self.activebg   = abg
			self.textcolour = fg
			self.activetext = afg
			self.highlightcolour = hl
			#self.textalignment = txtal
			self.borderwidth = bd
			self.activeborderwidth = abd
			self.cursor = cur
			self.relief = reliefMode
			self.font = font
			self.disabledbg = dbg
			self.disabledfg = dfg
			self.incorrectBg = incorrectBG
	#END CLASS

	#yes, this is literally the same as a button
	class CheckboxTheme():
		"""Theming data for a Checkbox widget"""
		background = "#d9d9d9"
		textcolour = "#000000" #aka black
		activebg   = "#d9d9d9"
		activetext = "#000000"
		highlightcolour = "#d9d9d9"
		image = None  #if none, it won't add the image
		disabledfg = "#111"

		#textalignment = TextAlignment.center

		borderwidth = 2
		relief = ReliefMode.flat

		font = None #if none will just use default of the Theme

		def __init__(self, bg = "#d9d9d9", fg = "#000000", abg = "#d9d9d9", afg = "#000000", dfg = "#111", hl = "#d9d9d9", img = None, reliefMode=ReliefMode.flat, bd = 2, font = None):
			self.background = bg
			self.textcolour = fg
			self.activebg = abg
			self.activetext = afg
			self.highlightcolour = hl
			self.image = img
			self.borderwidth = bd
			self.font = font
			self.relief = reliefMode
			self.disabledfg = dfg
	#END CLASS

	class DropdownTheme:
		#i don't actually need to define variables here. it was nice to have but ffs i dont want to
		#anyways the variables with "m" befrore the name are for the entries
		def __init__(self, bg = "#d9d9d9", fg = "#000000", abg = "#d9d9d9", afg = "#000000", img = None, reliefMode=ReliefMode.flat, bd = 2, font = None, mbg = None, mfg = None, mabg = None, mafg = None, mimg = None, mreliefMode=None, mbd = None, mfont = None):
			self.background = bg
			self.textcolour = fg
			self.activebg = abg
			self.activetext = afg
			self.image = img
			self.borderwidth = bd
			self.font = font
			self.relief = reliefMode
			#if any of these values is none it just defaults it to the ones above
			self.menubackground = mbg if mbg is not None else bg
			self.menutextcolour = mfg if mfg is not None else fg
			self.menuactivebg = mabg if mabg is not None else abg
			self.menuactivetext = mafg if mafg is not None else afg
			self.menuimage = mimg if mimg is not None else img
			self.menuborderwidth = mbd if mbd is not None else bd
			self.menufont = mfont if mfont is not None else font
			self.menurelief = mreliefMode if mreliefMode is not None else reliefMode

	name = None

	font = "Consolas 11"
	transparency = 0

	windowBg = "#d9d9d9"

	ButtonTheming = EntryFieldTheming = CheckBoxTheming = DropdownTheming = LabelTheming = None

	windowWidth	 = 1000
	windowHeight = 800

	#something for message boxes?

	#if, for example, you wanted the "PRINT_BTN" button to look green even though the default colour is red you'd add a "PRINT_BTN" key with the property as value
	specialWidgets = {  }

	def __init__(self, name : str, font : str, windowBG : str, buttonAppearance : ButtonTheme, entryAppearance : FieldTheme, checkboxAppearance : CheckboxTheme, labelAppearance : LabelTheme, dropdownAppearance : DropdownTheme, windowWidth : int, windowHeight : int, transparency : float = 0, specialWidgets : dict = {}):
		"""
		+ Font: the default font for the window.\n
		+ WindowBG: the colour of the window.\n
		+ transparency: must be from 0 to 1, where 1 is fully transparent.\n
		+ buttonAppearance, entryAppearance, checkboxAppearance: data for these types of widgets
		"""
		self.self = self #ah yes

		#type checking
		#font
		if not isinstance(font, str):
			raise ValueError("The font should be a font")
		#colour
		try:
			ts = tk.Tk()   #this is the dumbest fucking idea ive ever had
			ts["bg"] = windowBG #we try to apply the background. if not a valid colour, raise exception
			ts.destroy()
		except:
			ts.destroy()
			raise ValueError("your colour sucks")
		#stuff
		if not (isinstance( labelAppearance, self.LabelTheme) and
				isinstance( buttonAppearance, self.ButtonTheme) and
				isinstance( checkboxAppearance, self.CheckboxTheme) and
				isinstance( entryAppearance, self.FieldTheme) and
				isinstance( dropdownAppearance, self.DropdownTheme)):
			raise ValueError("bad theme")
		#transparency
		if not (isinstance(transparency, int) or isinstance(transparency, float)):
			raise ValueError("transparency is not a number")
		if not 0 <= transparency < 1:
			raise ValueError("transparency is to be between 0 and 1")
		#special widgets
		if not isinstance(specialWidgets, dict):
			raise ValueError(str(specialWidgets), "is bad")
		if type(windowWidth) is not int or type(windowHeight) is not int:
			raise ValueError("who even reads exceptions anyways")
		if windowHeight <= 0 or windowWidth <= 0:
			raise ValueError("are you fucking stupid")

		self.name = name
		self.font = font
		self.windowBg = windowBG
		self.LabelTheming = labelAppearance
		self.ButtonTheming = buttonAppearance
		self.CheckBoxTheming = checkboxAppearance
		self.DropdownTheming = dropdownAppearance
		self.EntryFieldTheming = entryAppearance
		self.transparency = transparency  #from 0 to 1 where 0 is not transparent and 1 is invisible
		self.specialWidgets = specialWidgets
		self.windowHeight = windowHeight
		#self.windowWith = windowWidth		#i won't delete this line. this will forever stay as a testament to why python classes suck ass
		self.windowWidth = windowWidth
	#END INIT

	#this is like "1000x600"
	def GetWindowShape(self):
		return str(self.windowWidth) + "x" + str(self.windowHeight)
	
	#labels just set the font to the default and background the same as the window
	def SetWindowProperties(self, window, frame):
		"""This will apply all properties contained in the theme to the given window"""
		window.configure (background=self.windowBg)
		frame .configure (background=self.windowBg)
		window.attributes("-alpha", (1 - self.transparency))
		window.option_add("*Font", self.font)
	#END

	def SetAllProperties(self, window, frame):
		"""Sets all properties in the given frame"""
		self.SetWindowProperties(window, frame)
		for windget in frame.winfo_children():
			if not type(windget) in validTypes: continue #skips if not button or such
			if windget["text"] in self.specialWidgets:
				self.SetSpecialProperties(windget, windget["text"])
				continue
			#if not
			self.SetPropertiesForWidget(windget)
	#END FUNC

	def SetSpecialProperties(self, widget, name):
		"""Used for widgets that require special themes, different from the defaults"""
		props = self.specialWidgets[name]
		
		self.__SetPropertiesWithProps(widget, props)
	#END FUNC
	
	def SetPropertiesForWidget(self, widget):
		"""Given a widget, this function will set all its properties"""

		#get the props given the type. since python is too cool for switch statements, we have to do this monstruosity
		widgetType = type(widget)
		match widgetType:
			case  tk.Entry:
				props = self.EntryFieldTheming
			case tk.Button:
				props = self.ButtonTheming
			case tk.Checkbutton:
				props = self.CheckBoxTheming
			case tk.OptionMenu:
				props = self.DropdownTheming
			case tk.Label: #
				print(widget["text"], "is label")
				props = self.LabelTheming

		self.__SetPropertiesWithProps(widget, props)
	#END

	#it's much better to have it in a different function considering all code was the same
	#this is for both "set widget properties" funcs
	def __SetPropertiesWithProps(self, widget, props):
		widgetType = type(widget)

		if widgetType == tk.OptionMenu:
			widget.config(
				bg = props.background,
				fg = props.textcolour,
				activebackground = props.activebg,
				activeforeground = props.activetext,
				image = props.image,
				bd = props.borderwidth,
				relief = props.relief.value
			)
			widget["menu"].config(
				bg = props.menubackground,
				fg = props.menutextcolour,
				activebackground = props.menuactivebg,
				activeforeground = props.menuactivetext,
				image = props.menuimage,
				bd = props.menuborderwidth,
				relief = props.menurelief.value
			)
			return
		elif widgetType == tk.Label: #label
			print("doing the thing")
			#this is stuff just for labels, after this we return
			if type(props) == str:
				#first set the properties normal
				self.SetPropertiesForWidget(widget)
				#then change the font
				widget["font"] = props
			else:
				widget["bg"] = self.windowBg
				widget["fg"] = props.textcolour
				widget["font"] = props.font
			return

		widget["bg"] = props.background
		widget["fg"] = props.textcolour
		widget["bd"] = props.borderwidth
		widget["highlightcolor"] = props.highlightcolour
		widget["relief"] = props.relief.value
		#PRINT_BTN(widgetType)
		widget["disabledforeground"] = props.disabledfg

		if props.font is not None:
			widget["font"] = props.font
		else:
			widget["font"] = self.font

		if   widgetType == tk.Entry:
			widget["disabledbackground"] = props.disabledbg
			widget["cursor"] = props.cursor.value
			widget["selectbackground"] = props.activebg
			widget["selectforeground"] = props.activetext
			widget["selectborderwidth"] = props.activeborderwidth
		elif widgetType == tk.Button or widgetType == tk.Checkbutton:
			widget["activebackground"] = props.activebg
			widget["activeforeground"] = props.activetext
			if props.image is not None: widget["image"] = props.image
	#END
#END CLASS

def ApplyTheme(theme : Theme, window, frame):
	theme.SetAllProperties(window, frame)

#REGION THEME DEFINITION

DefaultTheme = Theme("Default Theme",
	font="Courier 11", windowBG="#d9d9d9",
	#these two are the only changed, to improve visibility of disabled stuff
	buttonAppearance=Theme.ButtonTheme(dfg="#808080"),
	entryAppearance=Theme.FieldTheme(dbg="#d0d0d0", dfg="#808080"),
	checkboxAppearance=Theme.CheckboxTheme(),
	labelAppearance=Theme.LabelTheme(),
	dropdownAppearance=Theme.DropdownTheme(),
	windowWidth=1000,
	windowHeight=650,
	transparency=0,
	specialWidgets = {
		"✓" : Theme.LabelTheme(fg="#2dbd3a", font="Courier 60"),
		"!" : Theme.LabelTheme(font="Courier 60",fg="#fF0"),
		"COMPLETE_MSG" : "Courier 10",
		"INCOMPLETE_MSG" : "Courier 10",
		"SETTINGS_MENU_TITLE" : "Helvetica 13 bold",
		#main menu
		"START_BTN" : Theme.ButtonTheme(),
		"PRINT_BTN" : Theme.ButtonTheme(),
		"SETTINGS_BTN" : Theme.ButtonTheme(),
		"QUIT_BTN" : Theme.ButtonTheme(),
		#settings menu
		"Save Settings" : Theme.ButtonTheme(),
		"Reset Settings" : Theme.ButtonTheme(),
		#registers menu
		"save" : Theme.ButtonTheme(),
		"back" : Theme.ButtonTheme(),
	}
)

DumbTheme = Theme("Dumb Theme",
	"Courier 11", "#d9d9d9",
	buttonAppearance=Theme.ButtonTheme(),
	entryAppearance=Theme.FieldTheme(),
	checkboxAppearance=Theme.CheckboxTheme(),
	labelAppearance=Theme.LabelTheme(),
	dropdownAppearance=Theme.DropdownTheme(),
	windowWidth=1000,
	windowHeight=650,
	transparency=0,
	specialWidgets = {
		"✓" : "Courier 60",
		"!" : "Courier 60",
		"Today's work is complete!" : "Courier 10",
		"Today's work is incomplete!" : "Courier 10",
		"Settings Menu" : "Helvetica 13 bold",
		#no these aren't staying this is just for testing
		"START_BTN" : Theme.ButtonTheme(bg="#ff0000", fg="#0f0", abg="#00f", afg="#808080", img=None, reliefMode=ReliefMode.sunken, bd=5),
		"PRINT_BTN" : Theme.ButtonTheme(bg="#ff0", fg="#0ff", abg="#f0f", afg="#32fa82", img=None, reliefMode=ReliefMode.groove, bd=5),
		"SETTINGS_BTN" : Theme.ButtonTheme(bg="#67b9af", fg="#fa667b", abg="#768fba", afg="#67afb0", img=None, reliefMode=ReliefMode.ridge, bd=5),
		"QUIT_BTN" : Theme.ButtonTheme(bg="#78fbad", fg="#6adb87", abg="#98bfaf", afg="#dac675", img=None, reliefMode=ReliefMode.flat, bd=5),
	}
)

TestTheme = Theme("Test Theme",
	"Courier 11", "#d9d9d9",
	Theme.ButtonTheme(), Theme.FieldTheme(), Theme.CheckboxTheme(),
	labelAppearance=Theme.LabelTheme(),
	dropdownAppearance=Theme.DropdownTheme(),
	windowWidth=1000,
	windowHeight=650,
	transparency=0,
	specialWidgets = 
	{
		"✓" : "Courier 60",
		"!" : "Courier 60",
		"Today's work is complete!" : "Courier 10",
		"Today's work is incomplete!" : "Courier 10",
		"Settings Menu" : "Helvetica 13 bold",
		#no these aren't staying this is just for testing
		"START_BTN" : Theme.ButtonTheme(bg="#ff0000", fg="#ffffff", abg="#8c0000", afg="#808080", img=None, reliefMode=ReliefMode.flat, bd=5),
		"PRINT_BTN" : Theme.ButtonTheme(bg="#ff0", fg="#0ff", abg="#f0f", afg="#32fa82", img=None, reliefMode=ReliefMode.flat, bd=5),
		"SETTINGS_BTN" : Theme.ButtonTheme(bg="#67b9af", fg="#fa667b", abg="#768fba", afg="#67afb0", img=None, reliefMode=ReliefMode.flat, bd=5),
		"QUIT_BTN" : Theme.ButtonTheme(bg="#78fbad", fg="#6adb87", abg="#98bfaf", afg="#dac675", img=None, reliefMode=ReliefMode.flat, bd=5),
	}
)

KermitTheFrogTheme = Theme(name="Kermit The Frog",
	font="Courier 10",
	windowBG="#8beb67",
	buttonAppearance=Theme.ButtonTheme(bg="#8beb67", fg="#03c11b", bd=1, abg="#03c11b", afg="#8beb67"),
	entryAppearance=Theme.FieldTheme(bg="#8beb67", fg="#03c11b", abg="#03c11b", afg="#8beb67", dbg="#382", dfg="#212", incorrectBG="#fa7a55"),
	checkboxAppearance=Theme.CheckboxTheme(bg="#8beb67", fg="#03c11b", abg="#03c11b", afg="#8beb67"),
	labelAppearance=Theme.LabelTheme(fg="#03c11b"),
	dropdownAppearance=Theme.DropdownTheme(bg="#8beb67", fg="#03c11b", abg="#03c11b", afg="#8beb67"),
	windowWidth=1000,
	windowHeight=650,
)
#fa7a55

DarkTheme = Theme("Dark Theme",
	font="Courier 10",
	windowBG="#222",
	buttonAppearance=Theme.ButtonTheme(bg="#282828", fg="#fff", bd=1, abg="#383838", afg="#fff"),
	entryAppearance=Theme.FieldTheme(bg="#282828", fg="#fff", abg="#383838", afg="#fff", dbg="#111", dfg="#555"),
	checkboxAppearance=Theme.CheckboxTheme(bg="#282828", fg="#fff", abg="#383838", afg="#fff"),
	labelAppearance=Theme.LabelTheme(fg="#fff"),
	dropdownAppearance=Theme.DropdownTheme(bg="#282828", fg="#fff", abg="#383838", afg="#fff"),
	windowWidth=1000,
	windowHeight=650,
	specialWidgets = {
		#"Reset Settings" : Theme.ButtonTheme(bg="#862222", fg="#fff", abg="#863636", afg="#fff", hl="#000000", img=None, reliefMode=ReliefMode.flat, bd=5),

		#"Save Settings" : Theme.ButtonTheme(bg="#228622", fg="#fff", abg="#368636", afg="#fff", hl="#000000", img=None, reliefMode=ReliefMode.flat, bd=5)
	}
)

#DarkerTheme = Theme(
#	font = "courier 60", windowBG = "#000000", buttonAppearance = Theme.ButtonTheme()
#)

#should we add a Sam theme and an Antonio theme as well?

NoorTheme = Theme("Noor Theme",
	"Courier 11", "#d9d9d9",
	Theme.ButtonTheme(), Theme.FieldTheme(), Theme.CheckboxTheme(),
	labelAppearance=Theme.LabelTheme(),
	dropdownAppearance=Theme.DropdownTheme(),
	windowWidth=1000,
	windowHeight=650,
	transparency=0,
	specialWidgets = 
	{
		"✓" : "Courier 60",
		"!" : "Courier 60",
		"COMPLETE_MSG" : "Courier 10",
		"INCOMPLETE_MSG" : "Courier 10",
		"SETTINGS_MENU_MSG" : "Helvetica 13 bold",
		#no these aren't staying this is just for testing
		"START_BTN" : Theme.ButtonTheme(bg="#000000", fg="#069420", abg="#000000", afg="#000000", hl="#000000", img=None, reliefMode=ReliefMode.flat, bd=5),
		"PRINT_BTN" : Theme.ButtonTheme(bg="#000000", fg="#000000", abg="#069", afg="#000000", hl="#000000", img=None, reliefMode=ReliefMode.flat, bd=5),
		"SETTINGS_BTN" : Theme.ButtonTheme(bg="#000000", fg="#420", abg="#000000", afg="#000000", hl="#000000", img=None, reliefMode=ReliefMode.flat, bd=5),
		"QUIT_BTN" : Theme.ButtonTheme(bg="#000000", fg="#000000", abg="#000000", afg="#000000", hl="#000000", img=None, reliefMode=ReliefMode.flat, bd=5),
	}
)

HackerTheme = Theme("Hacker Theme",
	"Terminal 10", "#000",
	Theme.ButtonTheme(bg="#101", fg="#0f0", abg="#101", afg="#0f0", dfg="#020"),
	Theme.FieldTheme(bg="#202020", incorrectBG="#500000", fg="#0d0", abg="#202020", afg="#0d0", dbg="#202020", dfg="#080"),
	Theme.CheckboxTheme(bg="#111", fg="#0f0", abg="#111", afg="#0f0", dfg="#020"),
	Theme.LabelTheme(fg="#0f0"),
	Theme.DropdownTheme(bg="#101", fg="#0f0", abg="#101", afg="#0f0"),
	windowWidth=900,
	windowHeight=650,
	transparency=0,
	specialWidgets= {
		#"!" : Theme.LabelTheme(font="Courier 60",fg="red")#,fg="#"),
	}

)

#ENDREGION THEME DEFINITION

#list containing all themes (NOT the names)
THEMES = [
	DefaultTheme,
	DarkTheme,
	HackerTheme,
	KermitTheFrogTheme,
	# DumbTheme,
	# TestTheme,
	# NoorTheme,
]