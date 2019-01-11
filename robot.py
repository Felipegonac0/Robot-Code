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
        read_input()

        self.front_left_motor = wpilib.Spark(0)
        self.rear_left_motor = wpilib.Spark(1)
        self.front_right_motor = wpilib.Spark(2)
        self.rear_right_motor = wpilib.Spark(3)

        self.left_motor = wpilib.SpeedControllerGroup(self.front_left_motor,self.rear_left_motor)
        self.right_motor = wpilib.SpeedControllerGroup(self.front_right_motor,self.rear_right_motor)

        self.eguzki_motor = wpilib.Spark(4) 

        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def teleopPeriodic(self):
        
        x = state["chasis_x_mov"]
        y = state["chasis_y_mov"]
        
        if state["button_y_on"] == True:
            if self.sensor_1.get():
                self.left_motor.set(-.7)
                self.right_motor.set(.7)
            elif self.sensor_2.get(): 
                self.left_motor.set(-.3)
                self.right_motor.set(.3)  
            elif self.sensor_4.get(): 
                self.right_motor.set(-.3)
                self.left_motor.set(.3)
            elif self.sensor_5.get(): 
                self.right_motor.set(-.7)
                self.left_motor.set(.7)
            elif self.sensor_3.get(): 
                self.right_motor.set(0)
                self.left_motor.set(0)
            else:
                print("nada")
        else: 
            self.drive.arcadeDrive(y, x)


if __name__ == "__main__":
    wpilib.run(MyRobot)