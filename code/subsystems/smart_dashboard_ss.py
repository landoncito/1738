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

class SmartDashboardSubsystem(commands2.Subsystem):
    def __init__(self):
        self.stored_number = 0
        log.info("Increment number command initialized")
    def increment_number(self):
        self.stored_number = self.stored_number + 1
    def get_number(self):
        return self.stored_number
    
   