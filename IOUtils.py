import os

try:
	import msvcrt
	_system = "Windows"
except ImportError:
	print "TODO: Implement Unix keyboard input"

# Clearing the terminal
def clear():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")