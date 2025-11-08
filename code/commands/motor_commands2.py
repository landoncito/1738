import logging
log = logging.Logger('P212-robot')

import commands2
import constants

## TODO: Change this for your robot!
##       (Change the import line so that it imports your subsystem by its
##        correct name.)
##

from subsystems.motor_ss2 import MotorSubsystem2



class GoForwardCommand2(commands2.Command):
    ## TODO: Change this for your robot!
    ##       (Write reasonable documentation for your command.)
    ##
    """
    Make the robot go forward. 
    """
    ## TODO: Change this for your robot!
    ##       (Change the name and class of the constructor's subsystem
    ##        parameter.)
    ##
    def __init__(self, motor_ss: MotorSubsystem2) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        self.motor_ss2 = MotorSubsystem2

        # addRequirements() declares that this command needs exclusive use of
        # this subsystem.  If another command that needs this subsystem gets
        # scheduled to run, this command won't be able to run anymore, so it
        # will get cancelled.  For example, commands such as RaiseElevator and
        # LowerElevator both use the Elevator subsystem and can't run at the
        # same time, so they must each call addRequirements(self.elevator_ss)
        #
        #self.addRequirements(self.motor_ss)

    def initialize(self):
        """
        Perform any setup to initialize the command, and/or perform any
        command that can be completed all in one shot.
        This method runs when the scheduler schedules the command.
        """
        ## TODO: Change this for your robot!
        ##       (Can this command do everything in one shot?  If not, does
        ##        this command need to do anything to set up?  If so, put that
        ##        code here.)
        ##
        self.motor_ss2.go_forward2()

        """
        Performs the main part of any command that needs to happen on an
        ongoing basis, such as continuously reading a joystick.
        This method runs 50 times a second while the command is active.
        """
        ## TODO: Change this for your robot!
        ##       (What does this command need to do continuously?  Put that
        ##        code here.  If you don't need to do anything continuously,
        ##        you can delete the entire execute() method.)
        ##

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """
        ## TODO: Change this for your robot!
        ##       (What test determines whether this command has completed?  If
        ##        you did everything in initialize(), then then command has
        ##        already completed (and will always have completed), so you
        ##        can just return True.)
        ##

        # stop the motor if the sensor value is over 5.0
        return True

class GoBackwardCommand2(commands2.Command):
    ## TODO: Change this for your robot!
    ##       (Write reasonable documentation for your command.)
    ##
    """
    Make the robot go forward. 
    """
    ## TODO: Change this for your robot!
    ##       (Change the name and class of the constructor's subsystem
    ##        parameter.)
    ##
    def __init__(self, motor_ss: MotorSubsystem2) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        super().__init__()
        ## TODO: Change this for your robot!
        ##       (Assign the correct named parameter to a sensibly named
        ##        instance variable.)
        ##
        self.motor_ss2 = MotorSubsystem2

        # addRequirements() declares that this command needs exclusive use of
        # this subsystem.  If another command that needs this subsystem gets
        # scheduled to run, this command won't be able to run anymore, so it
        # will get cancelled.  For example, commands such as RaiseElevator and
        # LowerElevator both use the Elevator subsystem and can't run at the
        # same time, so they must each call addRequirements(self.elevator_ss)
        #
        #self.addRequirements(self.motor_ss)

    def initialize(self):
        """
        Perform any setup to initialize the command, and/or perform any
        command that can be completed all in one shot.
        This method runs when the scheduler schedules the command.
        """
        ## TODO: Change this for your robot!
        ##       (Can this command do everything in one shot?  If not, does
        ##        this command need to do anything to set up?  If so, put that
        ##        code here.)
        ##
        self.motor_ss2.go_backward2()

        """
        Performs the main part of any command that needs to happen on an
        ongoing basis, such as continuously reading a joystick.
        This method runs 50 times a second while the command is active.
        """
        ## TODO: Change this for your robot!
        ##       (What does this command need to do continuously?  Put that
        ##        code here.  If you don't need to do anything continuously,
        ##        you can delete the entire execute() method.)
        ##

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """
        ## TODO: Change this for your robot!
        ##       (What test determines whether this command has completed?  If
        ##        you did everything in initialize(), then then command has
        ##        already completed (and will always have completed), so you
        ##        can just return True.)
        ##

        # stop the motor if the sensor value is over 5.0
        return True
    
class StopCommand(commands2.Command):
    ## TODO: Change this for your robot!
    ##       (Write reasonable documentation for your command.)
    ##
    """
    Make the robot go forward. 
    """
    ## TODO: Change this for your robot!
    ##       (Change the name and class of the constructor's subsystem
    ##        parameter.)
    ##
    def __init__(self, motor_ss: MotorSubsystem2) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
       
        ##
        self.motor_ss2 = MotorSubsystem2

        # addRequirements() declares that this command needs exclusive use of
        # this subsystem.  If another command that needs this subsystem gets
        # scheduled to run, this command won't be able to run anymore, so it
        # will get cancelled.  For example, commands such as RaiseElevator and
        # LowerElevator both use the Elevator subsystem and can't run at the
        # same time, so they must each call addRequirements(self.elevator_ss)
        #
        self.addRequirements(self.motor_ss2)

    def initialize(self):
        """
        Perform any setup to initialize the command, and/or perform any
        command that can be completed all in one shot.
        This method runs when the scheduler schedules the command.
        """
        ## TODO: Change this for your robot!
        ##       (Can this command do everything in one shot?  If not, does
        ##        this command need to do anything to set up?  If so, put that
        ##        code here.)
        ##
        self.motor_ss2.stop()

        """
        Performs the main part of any command that needs to happen on an
        ongoing basis, such as continuously reading a joystick.
        This method runs 50 times a second while the command is active.
        """
        ## TODO: Change this for your robot!
        ##       (What does this command need to do continuously?  Put that
        ##        code here.  If you don't need to do anything continuously,
        ##        you can delete the entire execute() method.)
        ##

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """
        ## TODO: Change this for your robot!
        ##       (What test determines whether this command has completed?  If
        ##        you did everything in initialize(), then then command has
        ##        already completed (and will always have completed), so you
        ##        can just return True.)
        ##

        # stop the motor if the sensor value is over 5.0
        return True