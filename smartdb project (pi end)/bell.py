import RPi.GPIO as GPIO
import time
import os
import glob
#GPIO SETUP
GPIO.setmode(GPIO.BCM)
Button = 7
n = 1
GPIO.setup(Button,GPIO.IN)
#loop
print("Program Running")
while 1 == 1:#loops forever till keyboard interupt (ctr + C) 
  if GPIO.input(Button) == False:#when button pressed:
    print("Button Pressed")
    
    #    ------|    photo & Bell    |------ #
    #Get FileName
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
    #Make command to run OCMMDS
    command = "bash oscmds.sh " +  str(now)

    #run command
    os.system(command)
    #diagnostics
    print("Filename:", now)

    # ----| Pyrebase     |---- #
    print("Pyrebase")
    pyrecommand = 'python3 base.py ' + ' "photos/' + now + '.jpg"'
    os.system(pyrecommand)

    # -- End Diagnostic Info
    print("Done Process")
    #-space out for next "Press of Button"
    print("")
    print("")
