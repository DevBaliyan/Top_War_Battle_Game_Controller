import pyautogui as pg
import cv2 as cv
from PIL import ImageGrab
from sys import setrecursionlimit

setrecursionlimit(10**6)

def drag_up():
    pg.mouseDown(50, 100, button='left')
    pg.moveTo(50, 741, 0.15)
    pg.sleep(0.05)
    pg.mouseDown(50, 740, button='left')
    pg.sleep(0.1)
    pg.mouseUp(50, 740, button='left')
    pg.sleep(1.2)


def mouse_drag_left():
    pg.mouseDown(1260, 500, button='left')
    pg.moveRel(-100, 0, 0.1)
    pg.mouseUp(1160, 500, button='left')

    
def mouse_drag_right():
    pg.mouseDown(100, 500, button='left')
    pg.moveRel(100, 0, 0.1)
    pg.mouseUp(200, 500, button='left')

    
def drag_left():
    global img1, img2
    img1 = ImageGrab.grab(bbox=(645,725,670,730))
    mouse_drag_left()
    FoundOnScreen = pg.locateCenterOnScreen(img, confidence = 0.6)
    if FoundOnScreen != None:
        print('Found')
        pg.hotkey('ctrl', 'shift', '`')
    else:
        img2 = ImageGrab.grab(bbox=(645,725,670,730))
        if img1 == img2:
            drag_up()
            drag_right()
        else:
            drag_left()


def drag_right():
    global img1, img2
    img1 = ImageGrab.grab(bbox=(645,725,670,730))
    mouse_drag_right()
    FoundOnScreen = pg.locateCenterOnScreen(img, confidence = 0.6)
    if FoundOnScreen != None:
        print('Found')
        pg.hotkey('ctrl', 'shift', '`')
    else:
        img2 = ImageGrab.grab(bbox=(645,725,670,730))
        if img1 == img2:
            drag_up()
            drag_left()
        else:
            drag_right()


img, img1, img2 = cv.imread('sample-base-min.png'), None, None
pg.moveTo(900,500)


drag_left()

print('Process Over!')
