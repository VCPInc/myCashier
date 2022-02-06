#from er import er as er
#antonio you need help
#someone please give antonio a link to a mental help line
import tkinter as tk
import theme as theme
from settingsMenu import GetCurrentTheme as GetCurrentTheme
from languagemanager import lm as lm, ApplyLanguage as ApplyLanguage

#why are you doing it here#
#wdym? Where else would I do it???
def ppcalc(register):

	#final sizing will need to be done it VScode for proper optomization on Windows. Until then, I left it roughly done, Also, is there a way to find out current theme and apply it to the ppcalc function when it is called. 

	


	res = 0.0
	
	print("Calc func retrieved for register", register, ", beginning calc sequence(This sounds to too star treky)")
	cal=tk.Tk()
	cal.geometry("225x150")
	frame = tk.Frame(cal)
	cal.title(lm.GetVar("PP_TIT"))
		
	def addbut():
		nonlocal caltext
		nonlocal res
		print("OOOOHHH, Push my buttons...")#ffs who wrote this
		value=caltext.get()
		try:
			if float(value) <= 0: raise Exception
			res += round(float(value), 2)
			caltext["bg"] = GetCurrentTheme().EntryFieldTheming.background
		except Exception as e:
			print(e)
			caltext["bg"] = GetCurrentTheme().EntryFieldTheming.incorrectBg
		caltext.delete("0", "end")
		print("done adding values:", res, "is the current running total")
	def donebut():
		nonlocal res
		from registers import pcardsfields, NumberHasDecimalPlaces
		pcardsfields[register].delete("0", "end")
		pcardsfields[register].insert("0", str(res) + "0" if NumberHasDecimalPlaces(res, 1) else "0")
		cal.destroy()
	def cancelbut():
		cal.destroy()

	cal.config(background='light blue')

	textin=tk.StringVar()
	

		
	caltext=tk.Entry(cal,font=("Calibri(Body)",12,'bold'),textvar=textin,width=25 ,bd=2,bg='#EFEFEF')
	caltext.grid()

	space=tk.Label(cal, text="  ", bg='#DBFFFB')
	space.grid(row=0, column=0, rowspan=4)

	add=tk.Button(cal,bd=0,bg='#DBFFFB',command=addbut,text="PP_ADD_BTN",font=("Calibri (Body)",16,'bold'),height=1, width=4)
	add.grid(row=2)

	done=tk.Button(cal,bd=0,bg='#DBFFFB',command= lambda:(addbut(), donebut()) ,text="PP_DONE_BTN",font=("Calibri (Body)",16,'bold'), height=1,  width=4)
	done.grid(row=3)

	cancel=tk.Button(cal,bd=0,bg='#DBFFFB',command=cancelbut,text="PP_EXIT_BTN",font=("Calibri (Body)",16,'bold'), height=1,  width=4)
	cancel.grid(row=4)

	print("end of ppcalc definition")

	import settingsMenu as settings
	settings.ApplyTheme(cal, cal)
	ApplyLanguage(cal)
	cal.mainloop() #wait

	#guys help!
	#nvmd, i got it
	#hey guys, I didnt actually have it, ill get it eventually though
	
	#Thank goodness Stack overflow is a thing, otherwise none of this would ever be possible.
	



















