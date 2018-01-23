#!/usr/bin/env python3
"""
	hue
	hue

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
		self.frontLeft = wpilib.Jaguar(1)
		self.rearLeft = wpilib.Jaguar(2)
		self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

		self.frontRight = wpilib.Jaguar(3)
		self.rearRight = wpilib.Jaguar(4)
		self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

		self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

		self.stick = wpilib.Joystick(1)
		self.timer = wpilib.Timer()
		self.lift1 = wpilib.Jaguar(5)
		self.lift2 = wpilib.Jaguar(6)
		self.drop = wpilib.Jaguar(7)

		self.button_RB = JoystickButton(self.stick, 1)
		self.button_LB = JoystickButton(self.stick, 2)
		self.button_B = JoystickButton(self.stick, 3)
	
	def autonomousInit(self):
		"""This function is run once each time the robot enters autonomous mode."""
		self.timer.reset()
		self.timer.start()

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""

		# Drive for two seconds
		if self.timer.get() < 2.0:
			self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
		else:
			self.drive.arcadeDrive(0, 0)  # Stop robot

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""

		self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
		
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