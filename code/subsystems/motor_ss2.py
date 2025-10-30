import logging
log = logging.Logger('P212-robot')

from wpilib import DigitalInput
import commands2
import phoenix6
from constants import ELEC
class MotorSubsystem(commands2.Subsystem): 
    def __init__(self) -> None:
        self.my_motor2 = phoenix6.hardware.TalonFX(
            ELEC.my_motor_CAN_ID2)
    
    
    def go_backward2(self):
        self.my_motor2.set(-ELEC.my_motor_speed)
    def go_forward2(self):
        self.my_motor2.set(ELEC.my_motor_seed)
