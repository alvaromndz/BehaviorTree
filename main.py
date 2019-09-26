from Node import *
import time

blackboard = {
    'BATTERY_LEVEL': 100,
    'SPOT': False,
    'GENERAL': True,
    'DUSTY_SPOT': False,
    'HOME_PATH': '',
    'RUNNING_NODE': None,
    'TASK_TIME': 0,
    'CLEANING_DUSTY_SPOT': False
}

# constructing the tree
# the first layer
priority_1 = Priority(blackboard)
sequence_1 = Sequence(blackboard)
selection_1 = Selection(blackboard)
do_nothing = DoNothing(blackboard)

priority_1.addchild(sequence_1)
priority_1.addchild(selection_1)
priority_1.addchild(do_nothing)

# the second layer
# the sequence node in the left
batteryCond_1 = BatteryCond(blackboard, 30)
find_home = FindHome(blackboard)
go_home = GoHome(blackboard)
dock = Dock(blackboard)

sequence_1.addchild(batteryCond_1)
sequence_1.addchild(find_home)
sequence_1.addchild(go_home)
sequence_1.addchild(dock)

# the selection node in the middle
sequence_2 = Sequence(blackboard)
sequence_3 = Sequence(blackboard)

selection_1.addchild(sequence_2)
selection_1.addchild(sequence_3)

# the third layer
# the sequence node in the left
spot = SpotCond(blackboard)
clean_spot_1 = CleanSpot(blackboard, 20)
done_spot = DoneSpot(blackboard)

sequence_2.addchild(spot)
sequence_2.addchild(clean_spot_1)
sequence_2.addchild(done_spot)

#the sequence node in the right
general = GeneralCond(blackboard)
sequence_4 = Sequence(blackboard)

sequence_3.addchild(general)
sequence_3.addchild(sequence_4)

# the fourth layer
sequence_5 = Sequence(blackboard)
done_general = DoneGeneral(blackboard)

sequence_4.addchild(sequence_5)
sequence_4.addchild(done_general)

# the fifth layer
batteryCond_2 = BatteryCond(blackboard, 100)
selection_2 = Selection(blackboard)

sequence_5.addchild(batteryCond_2)
sequence_5.addchild(selection_2)

# the sixth layer
sequence_6 = Sequence(blackboard)
clean = Clean(blackboard)

selection_2.addchild(sequence_6)
selection_2.addchild(clean)

# the seventh layer
dusty_spot = DustySpotCond(blackboard)
clean_spot_2 = CleanSpot(blackboard, 35)

sequence_6.addchild(dusty_spot)
sequence_6.addchild(clean_spot_2)

def start():
    mode = raw_input("Please enter a mode: ")
    loop_time = float(raw_input("Please enter your loop speed (1 = 1s per loop): "))

    while True:
        print("\%\%\%\%\%\%\%\%\%\% BATTERY: " + str(blackboard['BATTERY_LEVEL']))
        if blackboard['TASK_TIME'] > 0: 
            blackboard['TASK_TIME'] -= 1
        if blackboard['SPOT']: 
            blackboard['BATTERY_LEVEL'] -= 5
        elif blackboard['CLEANING_DUSTY_SPOT']:
            blackboard['BATTERY_LEVEL'] -= 2
        else:
            blackboard['BATTERY_LEVEL'] -= 1

        if mode != "exit":
            if mode == 'spot':
                blackboard['SPOT'] = True
                mode = 'general'
            elif mode == 'general':
                blackboard['GENERAL'] = True
            else:
                print("Mode is invalid, please enter another one.")
                mode = raw_input("Please enter a mode: ")

            priority_1.action()
        else:
            return

        time.sleep(loop_time)

start()