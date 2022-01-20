

def PrintErrorLog(error : Exception):
	"""print the error to a file for easier bug reporting"""
	import traceback
	tb_str = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
	
	file = open("errors.log", "a")
	file.write(tb_str)
	file.write("\n\n\n\n\n")
	file.close()