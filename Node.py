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
    def __init__(self, blackboard, level):
        self.level = level
        self.blackboard = blackboard

    def action(self):
        if self.level == 100:
            if self.blackboard['BATTERY_LEVEL'] > 30:
                return 'True'
        if self.blackboard['BATTERY_LEVEL'] < self.level:
            print("LOW BATTERY!")
            return 'True'
        else:
            return 'False'


class FindHome(Node):
    def action(self):
        self.blackboard['HOME_PATH'] = 'A new home path.'
        self.blackboard['SPOT'] = False
        print('I found a path to home!')
        return 'True'


class GoHome(Node):
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def action(self):
        self.blackboard['RUNNING_NODE'] = self

        if self.blackboard['TASK_TIME'] == 0:
            self.blackboard['TASK_TIME'] = random.randrange(1,10,1)
        
        print("I'm going home! Approximately " + str(self.blackboard['TASK_TIME']) + " sec away.")

        if self.blackboard['TASK_TIME'] > 1:
            return 'Running'
        else:
            return 'True'


class Dock(Node):
    def action(self):
        self.blackboard['BATTERY_LEVEL'] = 100
        self.blackboard['SPOT'] = False
        self.blackboard['CLEANING_DUSTY_SPOT'] = False
        self.blackboard['GENERAL'] = True
        print("Charging...")
        print("Charging complete! The current battery level is: " + str(self.blackboard['BATTERY_LEVEL']))
        return 'True'


class SpotCond(Node):
    def action(self):
        if self.blackboard['SPOT']:
            return 'True'
        else:
            return 'False'


class CleanSpot(Node):
    def __init__(self, blackboard, worktime):
        self.worktime = worktime 
        self.blackboard = blackboard

    def action(self):
        # begin to clean spot
        if self.blackboard['TASK_TIME'] == 0:
            self.blackboard['TASK_TIME'] = self.worktime
        if self.blackboard['TASK_TIME'] > 1:
            if self.blackboard['CLEANING_DUSTY_SPOT']:
                print("I am cleaning a dusty spot!")
            else:
                print("I'm cleaning a spot!")

            print("There is " + str(self.blackboard['TASK_TIME']) + " left.")
            return 'Running'
        else: 
            self.blackboard['SPOT'] = False
            self.blackboard['CLEANING_DUSTY_SPOT'] = False
            return 'True'


class DoneSpot(Node):
    def action(self):
        self.blackboard['SPOT'] = False
        print("I am done cleaning spot!")
        self.blackboard['GENERAL'] = True
        return 'True'


class GeneralCond(Node):
    def action(self):
        if self.blackboard['GENERAL']:
            return 'True'
        else:
            return 'False'


class DustySpotCond(Node):
    def action(self):
        dusty_prob = random.random()
        if not self.blackboard['CLEANING_DUSTY_SPOT'] and dusty_prob <= 0.1:  # 10% chance of encountering
            self.blackboard['CLEANING_DUSTY_SPOT'] = True
            return 'True'
        elif self.blackboard['CLEANING_DUSTY_SPOT']:
            return 'True'
        else:
            return 'False'


class Clean(Node):
    def action(self):
        print("I am cleaning!")
        return 'True'


class DoneGeneral(Node):
    def action(self):
        if self.blackboard['GENERAL'] == False:
            print ("I am done with cleaning!")
            return 'False'
        return 'True'


class DoNothing(Node):
    def action(self):
        print ("I'm doing nothing...")
        return 'True'