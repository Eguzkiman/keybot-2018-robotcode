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
        self.frontLeft = wpilib.Jaguar(0)
        self.rearLeft = wpilib.Jaguar(1)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Jaguar(2)
        self.rearRight = wpilib.Jaguar(3)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.button_a = JoystickButton(self.stick, 1)

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
        if self.stick.getX() < 0.1 and self.stick.getY() < 0.1 and self.stick.getX() > -0.1 and self.stick.getY() > -0.1:
            self.drive.arcadeDrive(0,0)
        else: 
            powerY = self.stick.getY()
            powerX = self.stick.getX()

            if self.button_a.get():
                powerY *= 1

 
            else:
                powerY *= 0.7



            self.drive.arcadeDrive(powerY, powerX)







        

if __name__ == "__main__":
    wpilib.run(MyRobot)
