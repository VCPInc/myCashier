from sys import argv as _args
from requests import get as _getrequest
from ntpath import basename as _basename
#TODO: add a recovery mode that does something in case of a catastrophic occurrence while updating, like all files getting corrupted

#we need to know the version of the program. we store it in a file because it's easier
try:
	with open(".version") as _f:
		CURRENT_VERSION = float(_f.readline())
except:#if there is a problem here there will also be one later when we try to use this value, but at least there we have exception handling
	pass

#how the downloaded files will be saved
__FILENAME = "download.zip"
#how the updater app is called when built. used to check whether to execute the update or not
__BUILT_APP_NAME = "updater.exe"

def CheckForUpdates() -> dict:
	"""this returns the found release, or None if none is found"""
	#uses the github API to get information about the latest release
	releaseinfo = eval(str(_getrequest("https://api.github.com/repos/VCPInc/myCashier/releases/latest").json()))
	releasenum = float(releaseinfo["tag_name"])
	#if the current version is lower than the latest we return that there is a new release, else not
	if CURRENT_VERSION < releasenum:
		print("newer version found")
		return releaseinfo
	return None

def DownloadAndInstall() -> bool:
	#this way the you get to see the awesome console-based update before it starts
	print("attempting to update...")
	import time, random
	random.seed(time.time())
	time.sleep(1 + random.random())

	update = CheckForUpdates()
	if update is None:
		print("the program is up to date!")
		return False

	link = update["assets"][0]["browser_download_url"]

	try:
		DownloadLatest(link)
	except:
		print("\n\n\n\n\nthere was a problem while downloading, please retry later")
		return False
	try:
		InstallDownloadedFiles()
	except:
		print("\n\n\n\n\nthere was a problem while installing, please retry later")
		return False
	try:
		print("writing version file...")
		with open(".version", "w") as vfile:
			vfile.write(str(update["tag_name"]))
		print("done!")
	except:
		print("\n\n\n\n\nthere was a problem while installing, please retry later")
		return False
	return True

def DownloadLatest(link):
	"""downloads the linked release, and unzips the contents in a new folder"""
	#the link is a direct download
	print("downloading from", link, "...")
	file = open(__FILENAME, "wb")
	file.write(_getrequest(link).content)#this will get us a zipped archive
	file.close()
	print("succesfully downloaded", __FILENAME, "!")

def InstallDownloadedFiles():
	"""this assumes the files have already been downloaded and unzipped.
	this will replace all the current files with the newly downloaded ones,
	moving them in the current directory"""
	import zipfile, glob, os
	TEMP_DIR = "temp/"
	print("unzipping...")
	with zipfile.ZipFile(__FILENAME, 'r') as zip_ref:
		zip_ref.extractall(TEMP_DIR)
	os.remove(__FILENAME)

	print("moving installed files...")
	print("\t""making directories...")
	#create new directories for the newly installed files if needed
	for dir in os.walk(TEMP_DIR):
		#get the relativce path of the current directory
		dir = dir[0].replace("\\", "/")
		tmp = dir.split("/")
		tmp.pop(0)
		dir = os.getcwd().replace("\\", "/")
		for i in tmp:
			dir += "/" + i
		#if the dir is not found add it
		if not ( os.path.isdir(dir)):
			os.makedirs(dir)
			print("\t\t""created", dir)
	print("\t""moving files...")
	for file in glob.glob(TEMP_DIR + "**/*", recursive=True):
		#if the current thing is a file move it
		if os.path.isfile(file):
			#does the same thing as above
			newfile = file.replace("\\", "/")
			tmp = newfile.split("/")
			tmp.pop(0)
			newfile = os.getcwd().replace("\\", "/")
			for i in tmp:
				newfile += "/" + i
			#if there is already a file remove it
			if os.path.isfile(newfile):
				print("\t\t""file already found for '" + newfile + "', removing it...")
				os.remove(newfile)
			#this is like os.move, except it exists
			os.rename(file, newfile)
	print("removing temp directory...")
	from shutil import rmtree
	#eliminate temp folder AND all the subdirectories
	rmtree(TEMP_DIR)
	print("done!")


if _basename(_args[0]) == __BUILT_APP_NAME:
	result = DownloadAndInstall()
	input("press enter to continue...")
	import sys as sus
	from subprocess import Popen
	Popen(["myCashier.exe"])
	sus.exit()