import time

# CONSTANTS
MIN_SPEED = 0.005
MAX_SPEED = 2
DEF_SPEED = 0.02
ERROR = [
    "\n🔴 ERROR-0:\nNo arguments were provided.\n  ├─> You need to provide a text to print and a print speed (this last is optional)\n  └─> slowPrint(\"Example Text\", 0.02)\n",
    "\n🔴 ERROR-1:\nThere are too many arguments...\n  ├─> You need to provide a text to print and a print speed (this last is optional)\n  └─> slowPrint(\"Example Text\", 0.02)\n",
    "\n🔴 ERROR-2:\nArgument MUST be a string\n  └─> slowPrint(\"Example Text\")\n",
    "\n🔴 ERROR-3:\nArguments MUST be string, double.\n  └─> slowPrint(\"Example Text\", 0.02)\n"
]

def slowPrint(*args):
    '''
    Prints the value of a string letter by letter. 
    You can set just a text to print or also the print speed of each letter.

    Params in:
        Text (str):    Text to print.
        Speed (float): Print speed (default 0.02).
    
    Example:
        Text: 
            slowPrint("This is a text")\n
        Text, Speed:
            slowPrint("This is a text", 0.05)
    
    Note: 
        Limit speed is set to (0.005s - 2s). If your speed is out of the limits it will be 0.02s by default.
    '''
    s = DEF_SPEED

    if len(args) == 1 :
        if type(args[0]) == str:
            for char in args[0]:
                print(char, end="", flush=True)
                time.sleep(s)
            print()
        else:
            print(ERROR[2])

    elif len(args) == 2:
        if (type(args[0]) == str and (type(args[1]) == float or type(args[1]) == int)):
            if args[1] >= MIN_SPEED and args[1] <= MAX_SPEED:
                s = float(args[1])
            for char in args[0]:
                print(char, end="", flush=True)
                time.sleep(s)
            print()
        else:
            print(ERROR[3])
    
    elif len(args) == 0:
        print(ERROR[0])
    
    else:
        print(ERROR[1]) 
