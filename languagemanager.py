
class CatastrophicException(Exception):
	def __init__(self):
		try: os.reboot()
		except: print("bro not cool")
#exec("testVar = 'test value'")
#print(testVar)


class langmanager:

	def __init__(self, lang = "english"):
		self.loadlang(lang)
	def loadlang(self, lang, skipBadLines=True):
		"""loads all variables in a ttr file. if an invalid line is found it will skip it"""

		ln = 0
		#sets all variables
		for line in open("assets/languages/" + lang + ".ttr", encoding="utf-8"):
			ln += 1
			#yes this is dumb but not doing it is even dumber
			#if "import" in line: raise CatastrophicException
			if line == "" or line == "\n" or line[0] == "#": continue	#these two lines are edge case checking

			try:
				exec("self." + line)		#this is either genius or catastrophic
			except Exception as e:
				from os.path import basename	#import here to prevent ACE
				#technically it's not possible with all precautions i took, but you never know

				if skipBadLines is True:
					print("ERROR: invalid syntax in language file '" + basename(lang) + "' on line " + str(ln) + ":\n" + line)
				else:
					raise e

	def GetVar(self, varname):
		return eval("self." + varname)


def ApplyLanguage(frame):
	import tkinter as tk
	for widget in frame.winfo_children():
		try:
			#only these have a text attribute
			if type(widget) in [tk.Label, tk.Button, tk.OptionMenu, tk.Checkbutton]:
				widget["text"] = lm.GetVar(widget["text"])
		except: pass  #print(widget["text"], "is not a valid var")

lm = langmanager()

languages = {
	"English" : "english",
	"Italiano" : "italian",
	"ਪੰਜਾਬੀ" : "punjabi",
	"简体中文" : "chinese",
#	"عربى" : "arabic",
	"日本語" : "japanese",
	"God's Language (simplified)" : "DIO"
}

def SetLanguage(language, window, frame):
	import tkinter.messagebox as rnuo
	#ask for confirmation as this will reload the app
	print("in languagemanager: waiting for user confirmation...")
	if rnuo.askquestion(message=lm.GetVar("WINDOW_RELOAD_MSG")) == "yes":
		print("applying language", language, "...")
		lm.loadlang(language)		#load the new language
		print("reloading main...")
		window.destroy()
		from main import main as notmain
		notmain()
