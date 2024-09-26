import time

# CONSTANTS
MIN_SPEED = 0.005
MAX_SPEED = 2

def slowPrint(_text: str, _speed: float = 0.02):
    '''
    Prints the value of a string letter by letter. 
    You can set just a text to print or also the print speed of each letter.

    Params in:
        _text (str):    Text to print.
        _speed (float): Print speed (default 0.02).
    
    Example:
        _text: 
            slowPrint("This is a text")\n
        _text, _speed:
            slowPrint("This is a text", 0.05)
    
    Note: 
        Limit speed is set to (0.005s - 2s). If your speed is out of the limits it will be 0.02s by default.
    '''

    speed = 0.02 if _speed > MAX_SPEED or _speed < MIN_SPEED else _speed

    for char in _text:
        print(char, end="", flush=True)
        if char != " ": time.sleep(speed)
    print()
