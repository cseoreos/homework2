import glob

allPaths = glob.glob("./problem2[1-3]_[1-6].py")

for path in allPaths:
	with open(path, "r+") as file:
		lines = file.readlines()
		file.seek(0)
		file.write(
			"'''\n"
			"Gurkirat Singh: A11593827\n"
			"Anirudh Chava:  A99415981\n"
			"Jason Geneste:  A11357496\n"
			"'''\n")
		file.writelines(lines)
	
