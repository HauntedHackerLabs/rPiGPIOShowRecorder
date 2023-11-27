import RPi.GPIO as GPIO
import pigpio
import pygame as pyg
import sys
import os
import time

#Check if PIGPIOD is running
try:
    p = pigpio.pi()
    p.read(0)
except:
    print("pigpiod is not running")
    print("Running the following commands:")
    print("sudo systemctl enable pigpiod <-- This enables pigpiod at boot.")
    print("sudo systemctl start pigpiod  <-- This starts pigpiod now.")
    exit()

servo = 25
servo2 = 23
pwm = pigpio.pi()
pwm2 = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm2.set_mode(servo2, pigpio.OUTPUT)

pwm.set_PWM_frequency( servo, 50 )
pwm2.set_PWM_frequency(servo2, 50)

showName = input("Enter the show name: ")
showFile = showName+".py"
showScript = open(showFile,"w")
print("import RPi.GPIO as GPIO\nimport pigpio\nimport pygame as pyg\nimport time\n", file = showScript)
print("servo = 25\npwm = pigpio.pi()\npwm.set_mode(servo, pigpio.OUTPUT)\npwm.set_PWM_frequency(servo,50)\n", file = showScript)

pyg.init()
audioFile = input("Audio file name: ")
pyg.mixer.init()
pyg.mixer.music.load(audioFile)
pyg.mixer.music.play()

print("pyg.init()\nfile="+audioFile+"\npyg.mixer.init()\npyg.mixer.music.load(file)\npyg.mixer.music.play()\n", file = showScript)

pyg.joystick.init()
JNmax=pyg.joystick.get_count()
def All_Joy_init():
    J=[]
    for i in range(JNmax):
        J.append(JY(JN=i))
    return J

class JY(object):
    def __init__(self,JN=0):
        self.J=pyg.joystick.Joystick(JN)
        self.J.init()
        self.NAX=self.J.get_numaxes()
        self.NBT=self.J.get_numbuttons()
        self.NAM=self.J.get_name()
        self.NBALL=self.J.get_numballs()
        self.NHAT=self.J.get_numhats()
        self.JN=self.J.get_id()
        self.JNmax=JNmax

    def read_axis(self):
        self.Jax=[]
        pyg.event.pump()
        for i in range(self.NAX):
            self.Jax.append(self.J.get_axis( i ))
        return  self.Jax

    def read_bt(self):
        self.Jbt=[]
        pyg.event.pump()
        for i in range(self.NBT):
            self.Jbt.append(self.J.get_button( i ))
        return self.Jbt
    
    def read_hat(self):
        self.Jhat=[]
        pyg.event.pump()
        for i in range(self.NHAT):
            self.Jhat.append(self.J.get_hat(i))
        return self.Jhat
    

JJ=JY()
#p.start(0) # Initialization

print("while pyg.mixer.music.get_busy():\n", file = showScript )
print("     pyg.time.Clock().tick(10)\n", file = showScript)
posVar = []
posVar2 = []
try:
    while pyg.mixer.music.get_busy():
        
        pyg.time.Clock().tick(10)
        AX= JJ.read_axis()
        
        if AX[3] >= -1 and AX[3] < -0.8:
            #p.ChangeDutyCycle(5)
            pos = 500
            #pwm.set_servo_pulsewidth( servo, 500 )
            print("1")
        elif AX[3] >= -0.8 and AX[3] < -0.6:
            #p.ChangeDutyCycle(5.5)
            pos = 700
            #pwm.set_servo_pulsewidth( servo, 700 ) 
            print("2")
        elif AX[3] >= -0.6 and AX[3] < -0.4:
            #p.ChangeDutyCycle(6)
            pos = 900
            #pwm.set_servo_pulsewidth( servo, 900 ) 
            print("3")
        elif AX[3] >= -0.4 and AX[3] < -0.2:
            #p.ChangeDutyCycle(6.5)
            pos = 1100
            #pwm.set_servo_pulsewidth( servo, 1100 ) 
            print("4")
        elif AX[3] >= -0.2 and AX[3] < 0:
            #p.ChangeDutyCycle(7)
            pos = 1300
            #pwm.set_servo_pulsewidth( servo, 1300 ) 
            print("5")
        elif AX[3] >= .0 and AX[3] < 0.2:
            #p.ChangeDutyCycle(8)
            pos = 1500
            #pwm.set_servo_pulsewidth( servo, 1500 ) 
            print("7")
        elif AX[3] >= .02 and AX[3] < 0.4:
            #p.ChangeDutyCycle(8.5)
            pos = 1700
            #pwm.set_servo_pulsewidth( servo, 1700 ) 
            print("8")
        elif AX[3] >= .04 and AX[3] < 0.6:
            #p.ChangeDutyCycle(9)
            pos = 1900
            #pwm.set_servo_pulsewidth( servo, 1900 ) 
            print("9")
        elif AX[3] >= .06 and AX[3] < 8:
            #p.ChangeDutyCycle(9.5)
            pos = 2200
            #pwm.set_servo_pulsewidth( servo, 2200 ) 
            print("10")
        elif AX[3] >= -.08 and AX[3] <= 1:
            #p.ChangeDutyCycle(10)
            pos = 2500
            #pwm.set_servo_pulsewidth( servo, 2500 ) 
            print("11")                   
        else:
            pass

        if AX[2] >= -1 and AX[2] < -0.8:
            #p.ChangeDutyCycle(5)
            pos2 = 500
            #pwm.set_servo_pulsewidth( servo, 500 )
            print("1")
        elif AX[2] >= -0.8 and AX[2] < -0.6:
            #p.ChangeDutyCycle(5.5)
            pos2 = 700
            #pwm.set_servo_pulsewidth( servo, 700 ) 
            print("2")
        elif AX[2] >= -0.6 and AX[2] < -0.4:
            #p.ChangeDutyCycle(6)
            pos2 = 900
            #pwm.set_servo_pulsewidth( servo, 900 ) 
            print("3")
        elif AX[2] >= -0.4 and AX[2] < -0.2:
            #p.ChangeDutyCycle(6.5)
            pos2 = 1100
            #pwm.set_servo_pulsewidth( servo, 1100 ) 
            print("4")
        elif AX[2] >= -0.2 and AX[2] < 0:
            #p.ChangeDutyCycle(7)
            pos2 = 1300
            #pwm.set_servo_pulsewidth( servo, 1300 ) 
            print("5")
        elif AX[2] >= .0 and AX[2] < 0.2:
            #p.ChangeDutyCycle(8)
            pos2 = 1500
            #pwm.set_servo_pulsewidth( servo, 1500 ) 
            print("7")
        elif AX[2] >= .02 and AX[2] < 0.4:
            #p.ChangeDutyCycle(8.5)
            pos2 = 1700
            #pwm.set_servo_pulsewidth( servo, 1700 ) 
            print("8")
        elif AX[2] >= .04 and AX[2] < 0.6:
            #p.ChangeDutyCycle(9)
            pos2 = 1900
            #pwm.set_servo_pulsewidth( servo, 1900 ) 
            print("9")
        elif AX[2] >= .06 and AX[2] < 8:
            #p.ChangeDutyCycle(9.5)
            pos2 = 2200
            #pwm.set_servo_pulsewidth( servo, 2200 ) 
            print("10")
        elif AX[2] >= -.08 and AX[2] <= 1:
            pos2 = 2500
            print("11")                   
        else:
            pass

        pwm.set_servo_pulsewidth(servo, pos)
        pwm2.set_servo_pulsewidth(servo2, pos2)
        posVar.append(pos)
        posVar2.append(pos2)

    print(posVar, file=showScript)
except KeyboardInterrupt:
    pwm = pigpio.pi()
    pwm.set_mode(servo, pigpio.OUTPUT)
    pwm.set_PWM_frequency( servo, 50 )
    GPIO.cleanup()
    showScript.close()