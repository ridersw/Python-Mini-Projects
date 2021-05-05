from tkinter import *
import os
import tkinter.font as font
import time
import tkinter.messagebox as tkmb
import sys

#shell:startup -> cmd to get program in startup
def check_battery():

	# opens a pipe to or from command
	message = os.popen('WMIC PATH Win32_Battery Get EstimatedChargeRemaining').read()
	message = message.split()

	#message[1] has battery percent
	if int(message[1]) < 25:
		info_message="Battery Low"
		tkmb.showinfo("Warning", info_message)
		sys.exit()
	else:
		print("Battery Percent: ", message[1])
	
def executeSomething():
    check_battery()
	
	#time in secs
    time.sleep(900)

while True:
    executeSomething()
