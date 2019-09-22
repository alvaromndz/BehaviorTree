import random
import time

class Node:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def action(self):
        pass


class Composites(Node):
    def __init__(self, blackboard):
        self.children = []
        self.blackboard = blackboard

    def addchild(self, child):
        self.children.append(child)


class Sequence(Composites):

    def action(self):
        for child in self.children:
            result = child.action()
            if result == 'False':
                return 'False'
            elif result == 'Running':
                return 'Running'

        return 'True'


class Priority(Composites):
    def action(self):
        for child in self.children:
            result = child.action()
            if result == 'True':
                return 'True'
            elif result == 'Running':
                return 'Running'

        return 'False'


class Selection(Composites):
    def action(self):
        for child in self.children:
            result = child.action()
            if result == 'True':
                return 'True'
            elif result == 'Running':
                return 'Running'

        return 'False'


class BatteryCond(Node):
    def __init__(self, blackboard, low, high):
        self.low = low
        self.high = high
        self.blackboard = blackboard

    def action(self):
        if self.low <= self.blackboard['BATTERY_LEVEL'] < self.high:
            return 'True'
        else:
            return 'False'


class FindHome(Node):
    def action(self):
        self.blackboard['HOME_PATH'] = 'A new home path.'
        print('I found a path to home!')
        return "True"


class GoHome(Node):
    batteryLostPerSec = 0.1

    def action(self):
        self.blackboard['BATTERY_LEVEL'] -= self.batteryLostPerSec * random.randrange(1,10,1)
        print "I'm going home!"
        return 'True'


class Dock(Node):
    def action(self):
        self.blackboard['BATTERY_LEVEL'] = 100
        print "Charging...Charging complete! The current battery level is: " + str(self.blackboard['BATTERY_LEVEL'])
        return 'True'


class SpotCond(Node):
    def action(self):
        if self.blackboard['SPOT']:
            return 'True'
        else:
            return 'False'


class CleanSpot(Node):
    batteryLostPerSec = 1

    def __init__(self, blackboard, worktime):
        self.worktime = worktime  # the time set to work
        self.blackboard = blackboard

    def action(self):
        # begin to clean spot
        if self.blackboard['RUNNING_NODE'] != self:
            self.blackboard['RUNNING_NODE'] = self
            self.blackboard['START_TIME'] = time.time()
            if self.worktime <= 20:
                print("I'm cleaning a spot!")
            else:
                print("I'm cleaning a dusty spot!")
            return 'Running'
        else:  # cleaning the spot
            timedelta = time.time() - self.blackboard['START_TIME']
            if timedelta >= self.worktime:  # finished working
                self.blackboard['RUNNING_NODE'] = None
                self.blackboard['BATTERY_LEVEL'] -= CleanSpot.batteryLostPerSec * self.worktime
                self.blackboard['CLEANING_DUSTY_SPOT'] = False
                return 'True'
            else:
                if self.worktime <= 20:
                    print("I'm cleaning a spot!")
                else:
                    print("I'm cleaning a dusty spot!")
                return 'Running'


class DoneSpot(Node):
    def action(self):
        self.blackboard['SPOT'] = False
        print("I've done spot clean!")
        return 'True'


class GeneralCond(Node):
    def action(self):
        if self.blackboard['GENERAL']:
            return 'True'
        else:
            return 'False'


class DustySpotCond(Node):
    def action(self):
        index = random.choice([1, 2, 3, 4, 5])
        print("index"+str(index))
        print(self.blackboard['CLEANING_DUSTY_SPOT'])
        if not self.blackboard['CLEANING_DUSTY_SPOT'] and index == 3:  # if index=3 then it's a dusty spot
            self.blackboard['CLEANING_DUSTY_SPOT'] = True
            return 'True'
        elif self.blackboard['CLEANING_DUSTY_SPOT']:
            return 'True'
        else:
            return 'False'


class Clean(Node):
    def action(self):
        lost = random.randrange(5,10,1)
        self.blackboard['BATTERY_LEVEL'] -= lost
        self.blackboard['CLEANING_DUSTY_SPOT'] = False
        print("I've done cleaning!")
        return 'True'


class DoneGeneral(Node):
    def action(self):
        print ("I've done gereral cleaning!")
        self.blackboard['GENERAL'] = False
        return 'True'


class DoNothing(Node):
    def action(self):
        print ("I'm doing nothing...")
        return 'True'