def TKclear(f):
	print('clearing tkinter window')
	for widgets in f.winfo_children():
		widgets.destroy()
	print('done!')