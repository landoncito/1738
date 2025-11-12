import logging
log = logging.Logger('P212-robot')
import wpilib
from wpilib import DigitalInput
import commands2
import phoenix6
from constants import ELEC

## TODO: Change this for your robot!
##       (Import the libraries you need.)


## TODO: Change this for your robot!
##       (Change the name of the subsystem.  Use InitialCapitals.)
##
class MotorSubsystem(commands2.Subsystem):
    """
    This class represents an example subsystem for your robot.  Edit it to
    model your actual subsystems.
    """
    def __init__(self) -> None:
        """Creates a new ExampleSubsystem"""
        self.my_motor = phoenix6.hardware.TalonFX(
            ELEC.my_motor_CAN_ID)
        
    
    def go_forward(self):
        self.my_motor.set(ELEC.my_motor_speed)
    def go_backward(self):
        self.my_motor.set(-ELEC.my_motor_speed)
   

    def stop(self):
        """
        Example method that stops everything on the robot
        """
        self.my_motor.set(0.0)

class DisplayEncoderValue(commands2.Command):
     def __init__(self, motor_ss: MotorSubsystem):
         super().__init__()
         self.motor_ss = motor_ss
         self.addRequirements(self.motor_ss)

     def initialize(self):
        position = self.motor_ss.get_encoder_position()
        wpilib.SmartDashboard.putNumber("Second Motor Encoder", position)

     def isFinished(self):
         return True
