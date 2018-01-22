#!/usr/bin/env python3
"""
	This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
from wpilib.buttons import JoystickButton


class MyRobot(wpilib.IterativeRobot):

	def robotInit(self):
		"""
		This function is called upon program startup and
		should be used for any initialization code.
        """

		self.stick = wpilib.Joystick(0)
		self.timer = wpilib.Timer()
		self.lift1 = wpilib.Jaguar(4)
		self.lift2 = wpilib.Jaguar(5)
		self.drop = wpilib.Jaguar(6)

		self.button_RB = JoystickButton(self.stick, 1)
		self.button_LB = JoystickButton(self.stick, 2)
		self.button_B = JoystickButton(self.stick, 3)
	
	def autonomousInit(self):
		"""This function is run once each time the robot enters autonomous mode."""
		self.timer.reset()
		self.timer.start()
	

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""

		
		if self.button_RB.get():
			self.lift1.set(1)
			self.lift2.set(1)


		elif self.button_LB.get():
			self.lift1.set(-0.7)
			self.lift2.set(-0.7)
		
		else:
			self.lift1.set(0)
			self.lift2.set(0)


		if self.button_B.get():
			self.drop.set(1)

			
		else:
			self.drop.set(0)


if __name__ == "__main__":
	wpilib.run(MyRobot)