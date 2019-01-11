#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""
import time
import wpilib
import wpilib.drive
from state import state
from oi import setup_for_robot
from oi import read_input


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """ 
        setup_for_robot(self)

        self.front_left_motor = wpilib.Spark(0)
        self.rear_left_motor = wpilib.Spark(1)
        self.front_right_motor = wpilib.Spark(2)
        self.rear_right_motor = wpilib.Spark(3)

        self.left_motor = wpilib.SpeedControllerGroup(self.front_left_motor,self.rear_left_motor)
        self.right_motor = wpilib.SpeedControllerGroup(self.front_right_motor,self.rear_right_motor)

        self.eguzki_motor = wpilib.Spark(4) 

        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def teleopPeriodic(self):

        read_input()




        x = state["chasis_x_mov"]
        y = state["chasis_y_mov"]


        
        if state["button_y_on"]:
            if self.sensor_1.get():
                self.drive.arcadeDrive(0.7, 0)
            elif self.sensor_2.get(): 
                self.drive.arcadeDrive(0.4, 0)
            elif self.sensor_4.get(): 
                self.drive.arcadeDrive(0, 0.4)
            elif self.sensor_5.get(): 
                self.drive.arcadeDrive(0, 0.7)
            elif self.sensor_3.get(): 
                self.drive.arcadeDrive(0, 0)
        else: 
            self.drive.arcadeDrive(y, x)


if __name__ == "__main__":
    wpilib.run(MyRobot)