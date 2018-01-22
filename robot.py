#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.frontLeft = wpilib.Jaguar(0)
        self.rearLeft = wpilib.Jaguar(1)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Jaguar(2)
        self.rearRight = wpilib.Jaguar(3)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
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

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(1, 0)  
        elif self.timer.get() < 4.0:
            self.lift1.set(1)
            self.lift2.set(1)
        elif self.timer.get() < 5.5:
            self.drop.set(1)
            self.lift1.set(0)
            self.lift2.set(0)
        elif self.timer.get() < 7.5:
            self.lift1.set(-1)
            self.lift2.set(-1)
            self.drop.set(0)
        elif self.timer.get() < 9.5:
            self.drive.arcadeDrive(-1, 0)  
            self.lift1.set(0)
            self.lift2.set(0)

        else:
            self.drive.arcadeDrive(0, 0)
            self.lift1.set(0)
            self.lift2.set(0)
            self.drop.set(0)

              # Stop robot

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