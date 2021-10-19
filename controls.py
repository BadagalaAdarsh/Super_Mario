from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

global key
global space_pressed

key = None
space_pressed = False

# for pressing the space
# keyboard.press(Key.space) and keyboard.release(Key.space) 

# for pressing shift plus some key
# with keyboard.pressed(Key.shift):
# 		keyboard.press('a')
# 		keyboard.release('a')


def do_nothing():
    global key
    global space_pressed

    # if space is pressed release it
    if space_pressed:
        keyboard.release(Key.space)
        space_pressed = False

    if key != None:
        keyboard.release(key)

def move_left():

    global key
    global space_pressed

    # if space is pressed release it
    if space_pressed:
        keyboard.release(Key.space)
        space_pressed = False

    if key == 'd':
        keyboard.release(key)

    key = 'a'
    for i in range(100):
        keyboard.press(key)

def move_right():
    global key
    global space_pressed
    
    # if space is pressed release it
    if space_pressed:
        keyboard.release(Key.space)
        space_pressed = False

    if key == 'a':
        keyboard.release(key)

    key = 'd'
    for i in range(100):
        keyboard.press(key)

    #print("key pressed")

def jump():

    global key
    global space_pressed 

    # if some other key is pressed release it
    if key != None:
        keyboard.release(key)

    keyboard.press(Key.space)

    space_pressed = True
    #print("Space pressed")

