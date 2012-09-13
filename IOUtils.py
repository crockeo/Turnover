import os

try:
	import msvcrt
	_system = "Windows"
except ImportError:
	print "TODO: Implement Posix keyboard input"
	_system = "Posix"

# Clearing the terminal
def clear():
	if _system == "Windows"
		os.system("cls")
	elif os.name == "Posix":
		os.system("clear")

# Getting a single character
def getch():
	if _system == "Windows":
		return msvcrt.getch()
	elif _system == "Posix":
		pass