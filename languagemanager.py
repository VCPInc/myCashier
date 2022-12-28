#basically eval but with no security issues (AFAIK, dont come crying to me later if it still doesnt work)
from ast import literal_eval as _eval
from os.path import basename as _basename

LANGUAGE_PATH = "assets/languages/"
FILE_EXT = ".ttr"

class langmanager:

	LANGUAGE_NAME: str = None
	TRANSLATOR: str = None
	LANGUAGE_CODE: str = None

	def __init__(self, lang = "english"):
		self.loadlang(lang)
	def loadlang(self, lang, skipBadLines=True):
		"""loads all variables in a ttr file. if an invalid line is found it will skip it"""
		
		self.language = lang
		ln = 0
		#sets all variables
		for line in open((LANGUAGE_PATH + lang + FILE_EXT), encoding="utf-8"):
			ln += 1

			if "=" not in line or line[0] == "#":
				continue

			try:
				NAME = line[:line.index("=")]
				VALUE = _eval(line[line.index("=") + 2:])

				exec(f"self.{NAME}=VALUE")
			except:
				if skipBadLines is True:
					print("ERROR: invalid syntax in language file '" + _basename(lang) + "' on line " + str(ln) + ":\n" + line)
				else:
					raise

	def GetVar(self, varname):
		try:
			return eval("self." + varname)
		except:
			raise AttributeError(f'No key named "{varname}" in language {self.language}')


def ApplyLanguage(frame):
	import tkinter as tk
	for widget in frame.winfo_children():
		try:
			#if exception happens they didn't have a text attribute or an invalid var, so skip either way
			widget["text"] = lm.GetVar(widget["text"])
		except: pass  #print(widget["text"], "is not a valid var")

lm = langmanager()

languages = {
	"English" : "english",
	"Italiano" : "italian",
	"ਪੰਜਾਬੀ" : "punjabi",
	"简体中文" : "chinese",
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