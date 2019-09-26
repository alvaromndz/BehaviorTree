# BehaviorTree
Assignment #1 AI

## Requirements
You need python to run the program. 

## Execution

To run, it's as simple as:
```bash
python main.py
```

User will need to input a command: `spot` or `general`. Afterwards, you need to input a loop frequency. `1` will make the program loop once each second, `0.5` will make it loop once every half a second, `2` once every two seconds and so on...

A successful execution will look something like:

```bash
MacBook-Pro:BehaviorTree vz$ python main.py 
Please enter a mode: general
Please enter your loop speed (1 = 1s per loop): 1
```

At each iteration, the program will log its battery level and what it's doing. For example:

```bash
\%\%\%\%\%\%\%\%\%\% BATTERY: 100
I am cleaning!
```

or

```bash
\%\%\%\%\%\%\%\%\%\% BATTERY: 95
I am cleaning a dusty spot!
There is 33 sec left.
```

To exit the program, you can just press `ctrl + C`.

## Implementation Details

For general cleaning, the battery is drained 1% per loop. When in `general` mode, there is a 10% chance of encountering a dusty spot. If this occurs, the battery will start draining 2% per loop for the duration of the task.

When in `spot` mode, the battery is drained 5% per loop. This will cause for the battery to ALWAYS we drained under 30% before the entire 20 loops of the task. This is due to the old nature of our Roomba.

After spot cleaning or finishing a dusty spot, the mode is automatically switched to `general`.

When the battery drops under 30%, a random number from 1-10 will determine the distance to the dock, and navigation there will start while still losing 1% of battery per loop until docked. When docked, battery is updated back to 100% (old Roomba with quick-charge capabilities) and the mode will be set back to `general` every time.

## Customizations

Variables can be altered in the code to test edge cases. Lines 99, 101 and 103 determine battery loss at each mode. Lines 48 and 85 determine loop duration of spot and dusty spot cleaning.

## Authors

Alvaro Mendez ([alvaro.mendez@tufts.edu](mailto:alvaro.mendez@tufts.edu))

Yuqiao Zhao ([yuqiao.zhao@tufts.edu](mailto:yuqiao.zhao@tufts.edu))

## License
[MIT](https://choosealicense.com/licenses/mit/)