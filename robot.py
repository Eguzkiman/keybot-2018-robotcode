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
        self.left_motor = wpilib.Jaguar(0)
        self.right_motor = wpilib.Jaguar(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()
        self.motor1 = wpilib.Jaguar(5)
        self.motor2 = wpilib.Jaguar(6)
        self.motor3 = wpilib.Jaguar(7)



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
            self.motor1.set(1)
            self.motor2.set(1)
        elif self.timer.get() < 5.5:
            self.motor3.set(1)
            self.motor1.set(0)
            self.motor2.set(0)
        elif self.timer.get() < 7.5:
            self.motor1.set(-1)
            self.motor2.set(-1)
            self.motor3.set(0)
        elif self.timer.get() < 9.5:
            self.drive.arcadeDrive(-1, 0)  
            self.motor1.set(0)
            self.motor2.set(0)

        else:
            self.drive.arcadeDrive(0, 0)
            self.motor1.set(0)
            self.motor2.set(0)
            self.motor3.set(0)

              # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)