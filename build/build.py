import time
starttime = time.time()

DEBUG = False		#is it a debug build?
FINAL = False		#full build means ready for github
from sys import argv
if len(argv) > 1:
	if argv[1] == "debug":
		DEBUG = True
	if argv[1] == "final":
		FINAL = True
		DEBUG = False
if DEBUG is True:
	print("DEBUG BUILD STARTED\n\n")
if FINAL is True:
	print("FINAL BUILD STARTED\n\n")

import os, glob

SRC_DIR   = "../"							#path of the source files
NAME_MAIN = "main.py"						#name of the main app py source
NAME_UPDT = "updater.py"					#name of the updater py source
OUTN_MAIN = "myCashier.exe"					#name of the output for main app
OUTN_UPDT = "updater.exe"					#name of the output for the updater
DEST_DIR  = "../"							#path to place it in

ASSETS_DIR = SRC_DIR + "assets"
ICON_PATH = ASSETS_DIR + "/myCashier.ico"

try:
	print("compiling the main app...")
	os.system(f"nuitka {SRC_DIR + NAME_MAIN} --remove-output --onefile --follow-imports --include-module=babel.numbers --enable-plugin=tk-inter --enable-plugin=numpy {'--windows-disable-console' if DEBUG is False else ''} -o {OUTN_MAIN}")

	print("\n\ncompiling the updater...")
	os.system(f"nuitka {SRC_DIR + NAME_UPDT} --remove-output -o {OUTN_UPDT}")

	#there are some bad ugly files we don't want but the compiler creates, so remove them
	print("\n\nremoving build files...")
	for fike in glob.glob("*.cmd"):
		os.remove(fike)

	print("\n\nmoving built files...")
	if os.path.isfile(DEST_DIR + OUTN_MAIN):
		os.remove(DEST_DIR + OUTN_MAIN)
	if os.path.isfile(DEST_DIR + OUTN_UPDT):
		os.remove(DEST_DIR + OUTN_UPDT)
	os.rename(OUTN_MAIN, DEST_DIR + OUTN_MAIN)
	os.rename(OUTN_UPDT, DEST_DIR + OUTN_UPDT)

	#for the final build we also want to create a zip archive and place the files in there
	if FINAL is True:
		DIRNAME = "archive/"		#directory we place the build in (inside of the current build dir of course)
		ARCHIVE_NAME = "myCashier"	#name of the archive we create

		#remove all the temp files created during the thing
		def RemoveBuildFiles():
			#the build dir contains everything
			stuff_to_remove = [
				DIRNAME,
			]
			for thing in stuff_to_remove:
				shutil.rmtree(thing) if os.path.isdir(thing) is True else 1

		try:
			print("\n\ncreating the archive...")
			import shutil
			#add the archive dir
			os.makedirs(DIRNAME) if os.path.isdir(DIRNAME) is False else 1	#wtf is this line

			print("copying the files...")
			#move the assets
			shutil.copytree(ASSETS_DIR, (DIRNAME + "assets"))
			#move the EXEs
			shutil.copyfile(DEST_DIR + OUTN_MAIN, DIRNAME + OUTN_MAIN)
			shutil.copyfile(DEST_DIR + OUTN_UPDT, DIRNAME + OUTN_UPDT)

			print("removing ignorable files...")
			#ignore all files marked to be ignored
			for ignored_file in glob.glob(DIRNAME + "**/_*"):
				os.remove(ignored_file)

			print("compressing...")
			#creates the archive
			shutil.make_archive(ARCHIVE_NAME, 'zip', DIRNAME)

			RemoveBuildFiles()
		except:
			#we remove things
			RemoveBuildFiles()
			raise	#reraise the exception, it'll be caught later
	#END FINAL BUILD

	print("\n\ndone!")
	if DEBUG is True:
		print("debug", end=" ")
	if FINAL is True:
		print("final", end=" ")
	print("build completed in", time.time() - starttime, "seconds.")
except Exception as e:
	print("there was a problem:", e)

os.system("pause")