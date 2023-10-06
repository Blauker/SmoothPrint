# SmoothPrint v1.0.2 
**SmoothPrint** is a python package to print texts letter by letter. <br/>
You can use the **slowPrint** function for that. <br/>
By default, the speed is set to 0.02 seconds, but you can **customize** it by providing a different speed in seconds as the second argument. <br/>
![A](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2Z2ZXVjbTgweGdxY2Y1bzN6NGlidG1jMGh6OWZlMm83amhhbXRuayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1NE8pz1zbffBvcnY7w/giphy.gif)

## How to install
To install **SmoothPrint** you can use the following command: <br/>
```pip install SmoothPrint``` <br/>
or <br/>
```pip install -U SmoothPrint``` to update to latest version.

## How to use SmoothPrint?
```python
import SmoothPrint as SP  # SP can be whatever you want to call the package

# Printing only a text (default speed is 0.02s)
SP.slowPrint("This would be a text to print with a speed of 0.02s!")

# Printing a text with custom speed -> 0.1s
SP.slowPrint("This would be a text to print with a custom speed!", 0.1)
```
NOTE: _You will get error if the arguments are invalid_ 


