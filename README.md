# Simple stack smashing tool
A simple stack smash tool that I designed for use in CPSC213

##
To configure the tool to run from anywhere, add a symbolic link `stacksmash` to one of your `/bin/` directories (I used `/usr/local/bin/`). I set mine up as:
    
    /usr/local/bin/$ sudo ln ~/dev/tools/simplestacksmashtool/stacksmash stacksmash
        
where `~/dev/tools/simplestacksmashtool/` is the folder for this repository. In addition, inside of the `stacksmash` file, change the directory to match where it is located on your device. Perhaps I will eventually add some files that auto-configure all of this (including adding it to the binaries folders).

## Using command line arguments
#### beginstr:
The code that you want to run in hexadecimal
#### addr:
The address that you want to jump to (the location of beginstr in your system. most likely)
#### num:
The number of times you want to repeat addr (can go on indefinitely and say 1000, however this may overwrite data outside the stack, etc.)
### Example
    ~$ stacksmashtool.py 0ff322f320001902992010eece2200 00220199 20
    Your hex string:
    0ff322f320001902992010eece22000022019900220199002201990022019900220199002201990022019900220199002201990022019900220199002201990022019900220199002201990022019900220199002201990022019900220199
    Your formatted string:
    ?"? ? ??""?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?%

## Using regular input
Exactly the same inputs as above, except you will be prompted for the input instead of specifying it beforehand
### Example
    ~$ python3 stacksmashtool.py
    Enter the code you want to run:
    0ff322f320001902992010eece2200
    What is the address you want to jump to?
    00220199
    How many entries do you want to overwrite?
    20
    Your hex string:
    0ff322f320001902992010eece22000022019900220199002201990022019900220199002201990022019900220199002201990022019900220199002201990022019900220199002201990022019900220199002201990022019900220199
    Your formatted string:
    ?"? ? ??""?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?%
    
