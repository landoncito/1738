import logging
log = logging.getLogger('smartdashboardsubsystemlogger')

import commands2
import constants
import wpilib
from constants import OP

from subsystems.smart_dashboard_ss import SmartDashboardSubsystem

## TODO: Change this for your robot!
##       (Change the import line so that it imports your subsystem by its
##        correct name.)
##

from subsystems.motor_ss2 import MotorSubsystem2

class IncrementNumberCommand(commands2.Subsystem): 
      def __init__(self, smart_dashboard_ss: SmartDashboardSubsystem) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        self.smartdashboardss = smart_dashboard_ss
        self.addRequriements(self.smartdashboardss)
        def __init__(self):
         self.smartdashboardss.increment_number()
         
         current_value = self.smartdashboardss.get_number()
         wpilib.SmartDashboard.putNumber("My Stored Number", current_value)
         log.info("Increment number command initialized")
         def isFinished():
             return True