import time
print("build started\n\n\n")
starttime = time.time()

import os, glob

NAME_MAIN = "../main.py"		#path of the main app py source
NAME_UPDT = "../updater.py"		#path of the updater py source
OUTN_MAIN = "myCashier.exe"		#name of the output for main app
OUTN_UPDT = "updater.exe"		#name of the output for the updater
DEST_DIR  = ".."				#path to place it in

ICON_PATH = "../assets/myCashier.ico"

try:
	print("compiling the main app...")
	x = os.system(f"nuitka {NAME_MAIN} --remove-output --windows-disable-console -o {OUTN_MAIN}")

	print("\n\ncompiling the updater...")
	os.system(f"nuitka {NAME_UPDT} --remove-output -o {OUTN_UPDT}")

	#there are some bad ugly files we don't want but the compiler creates, so remove them
	print("\n\nremoving build files...")
	for fike in glob.glob("*.cmd"):
		os.remove(fike)

	print("\n\nmoving built files...")
	os.rename(OUTN_MAIN, f"{DEST_DIR}/{OUTN_MAIN}")
	os.rename(OUTN_UPDT, f"{DEST_DIR}/{OUTN_UPDT}")

	print("\n\ndone!")
	print("build completed in", time.time() - starttime, "seconds.")
except Exception as e:
	print("there was a problem:", e)

os.system("pause")