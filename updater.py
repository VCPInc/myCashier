# + creates this whole file
# + refuses to add comments


#DO NOT include this in the build. this HAS to stay separate because it is the recovery mode, and no update will change it
#TODO: test this with downloading from github and building in an app

from requests import get as _getrequest
#TODO: add a recovery mode that does something in case of a catastrophic occurrence while updating, like all files getting corrupted

with open(".version") as _f:
	CURRENT_VERSION = float(_f.readline())

__FILENAME = "download.zip"

def CheckForUpdates() -> dict:
	"""this returns the found release, or None if none is found"""
	#totally not overcomplicating things
	releaseinfo = eval(str(_getrequest("https://api.github.com/repos/VCPInc/myCashier/releases/latest").json()))
	releasenum = float(releaseinfo["tag_name"])
	if CURRENT_VERSION < releasenum:
		print("newer version found")
		#print(eval(str(_getrequest(releaseinfo["assets_url"]).json()))[0]["browser_download_url"])
		return releaseinfo
	return None

def DownloadAndInstall(link) -> bool | Exception:
	#this way the you get to see the awesome console-based update before it starts
	print("attempting to update...")
	import time, random
	random.seed(time.time())
	time.sleep(1 + random.random())

	try:
		DownloadLatest(link)
		InstallDownloadedFiles()
		return True
	except Exception as e:
		return e

def DownloadLatest(link):
	"""downloads the linked release, and unzips the contents in a new folder"""
	print("downloading from", link, "...")
	file = open(__FILENAME, "wb")
	file.write(_getrequest(link).content)
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
	for dir in os.walk(TEMP_DIR):
		dir = dir[0].replace("\\", "/")
		tmp = dir.split("/")
		tmp.pop(0)
		dir = os.getcwd().replace("\\", "/")
		for i in tmp:
			dir += "/" + i
		if not ( os.path.isdir(dir)):
			os.makedirs(dir)
	print("\t""moving files...")
	for file in glob.glob(TEMP_DIR + "**/*", recursive=True):
		if os.path.isfile(file):
			newfile = file.replace("\\", "/")
			tmp = newfile.split("/")
			tmp.pop(0)
			newfile = os.getcwd().replace("\\", "/")
			for i in tmp:
				newfile += "/" + i
			if os.path.isfile(newfile):
				print("\t\t""file already found for '" + newfile + "', removing it...")
				os.remove(newfile)
			os.rename(file, newfile)
	print("removing temp directory...")
	from shutil import rmtree
	rmtree(TEMP_DIR)
	print("done!")
