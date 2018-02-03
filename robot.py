#!/usr/bin/env python3

import wpilib
import wpilib.drive
from wpilib.buttons import JoystickButton


class MyRobot(wpilib.IterativeRobot):

	def robotInit(self):		#Declaring function

		self.stick = wpilib.Joystick(0) 	#Joystick in port 0 declared
		self.timer = wpilib.Timer()       
	
		self.frontLeft = wpilib.Jaguar(0)   #Chasis motor declared (PWM0)
		self.rearLeft = wpilib.Jaguar(1)	#Chasis motor declared (PWM1)
		self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

		self.frontRight = wpilib.Jaguar(2)	#Chasis motor declared (PWM2)
		self.rearRight = wpilib.Jaguar(3)	#Chasis motor declared (PWM3)
		self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

		self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

		self.lift_1 = wpilib.Jaguar(4)		#First Lift motor declared (PWM4)
		self.lift_2 = wpilib.Jaguar(5)		#Second Lift motor declared (PWM5)
		self.drop = wpilib.Jaguar(6)		#Drop motor declared (PWM6)
		self.led = wpilib.Jaguar(7)			#Led Talon motor declared (PWM7)

		self.button_A = JoystickButton(self.stick, 1)		#Fija Button_A al puerto 1 de botones (Xbox A)
		self.button_B = JoystickButton(self.stick, 2)		#Fija Button_B al puerto 2 de botones (Xbox B)
		self.button_X = JoystickButton(self.stick, 3)		#Fija Button_X al puerto 3 de botones (Xbox X)
		self.button_Y = JoystickButton(self.stick, 4)		#Fija Button_Y al puerto 4 de botones (Xbox Y)
		self.button_LB = JoystickButton(self.stick, 5)		#Fija Button_LB al puerto 5 de botones (Xbox LB)
		self.button_RB = JoystickButton(self.stick, 6)		#Fija Button_RB al puerto 6 de botones (Xbox RB)
		


	def autonomousInit(self):
		
		self.timer.reset()
		self.timer.start()



	#Autonomous Function
	def autonomousPeriodic(self):

		#(3 sec duration) goes foward, turns on led
		if self.timer.get() < 3:
			self.drive.arcadeDrive(1, 0)
			self.led.set(1)  

		#(3 sec duration) moves lift up
		elif self.timer.get() < 6:
			self.lift_1.set(1)
			self.lift_2.set(1)

		#(2 sec duration) activates drop motor
		elif self.timer.get() < 8:
			self.drop.set(1)
			self.lift_1.set(0)
			self.lift_2.set(0)

		#(2 sec duration) moves lift down
		elif self.timer.get() < 11:
			self.lift_1.set(-1)
			self.lift_2.set(-1)
			self.drop.set(0)

		#(2 sec duration) goes backwards, stops lift's movement
		elif self.timer.get() < 14:
			self.drive.arcadeDrive(-1, 0)
			self.lift_1.set(0)
			self.lift_2.set(0)

		# Stops all of the motor, turns off led
		else:		
			self.drive.arcadeDrive(0, 0)
			self.lift_1.set(0)
			self.lift_2.set(0)
			self.drop.set(0)
			self.led.set(0)


			
	#Function to control robot with Xbox controller
	def teleopPeriodic(self):
	
		if self.stick.getX() < 0.1 and self.stick.getY() < 0.1 and self.stick.getX() > -0.1 and self.stick.getY() > -0.1:  #Seguro para palanca del control (chasis)
			self.drive.arcadeDrive(0,0)

		else: 
			powerY = self.stick.getY()
			powerX = self.stick.getX()

			if self.button_A.get(): #When (xbox A) activated
				powerY *= 1     	#Full power

			else:					#If (xbox A) not activated
				powerY *= 0.7		#70% power

			self.drive.arcadeDrive(powerY, powerX)

		

		if self.button_RB.get():	#When (xbox RB) activated
			self.lift_1.set(.9)		#First lift motor activated 90% power
			self.lift_2.set(.9)		#Second lift motor activated 90% power
		elif self.button_LB.get():	#When (xbox LB) activated
			self.lift_1.set(-0.9)	#First lift motor activated 90% power (inverted)
			self.lift_2.set(-0.9)	#Second lift motor activated 90% power (inverted)
		else:
			self.lift_1.set(0)		#First lift motor desactivated
			self.lift_2.set(0)		#Second lift motor desactivated



		if self.button_B.get():		#When (xbox B) activated
			self.drop.set(1)		#Drop motor activated
		else:
			self.drop.set(0)		#Drop motor desactivated



		if self.button_Y.get():		#When (xbox Y) activated
			self.led.set(.5)		#Led turn on (50% power)


		if self.button_X.get():		#When (xbox X) activated
			self.led.set(0)			#Led turn off
		


	#All motors desactivated, Robot disabled
	def disabledInit (self):
		self.drive.arcadeDrive(0,0)
		self.lift_1.set(0)
		self.lift_2.set(0)
		self.drop.set(0)
		self.led.set(0)


if __name__ == "__main__":
	wpilib.run(MyRobot)





""" 
Instrucciones para desplegar y probar el codigo

	- Debes instalar pip con el comando "pip3 install pyfrc" en la terminal
	- Si te dice que no esta actualizado usa "pip3 install --upgrade pyfrc"
	- Entra a la carpeta "keybot-2018-robotcode" 
	- Con "git branch master" te mueves al codigo principal
	- Para correr el codigo en el simulador escribes "py -3 robot.py sim"
	- Para subir el codigo al roboRIO escribes "py -3 robot.py deploy --skip-tests --no-version-check"
	- IP adress del Rio es roborio-5716-frc.local

"""


""" 
Copyright (c) 2018 KEYBOT 5716

Permission is hereby granted, free of charge, to any
person obtaining a copy of this software and associated
documentation files, to deal in the
Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

"""
