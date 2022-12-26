import pyautogui as pg
import cv2 as cv
from PIL import ImageGrab
from sys import setrecursionlimit
"""Now compare the list and find the right most or left most coordinare
of flag and move only that much."""

setrecursionlimit(10**6)


def wait_for_img_load(cv_image, Confidence=0.85):
    coord_on_screen = None
    attempts = 1
    while coord_on_screen == None:
        coord_on_screen = pg.locateCenterOnScreen(cv_image, confidence = Confidence)
        pg.sleep(0.15)
        if attempts == 30:
            print('Attempts reached')
            pg.click(pg.moveRel(200,50))
        attempts += 1
    return coord_on_screen


def send_location(List):
    for i1, i2 in List:
        pg.click(i1, i2)
        pg.sleep(1)
        pos1 = wait_for_img_load(step1)
        pg.click(pos1)
        pos2 = wait_for_img_load(step2)
        pg.click(pos2)
        pos3 = wait_for_img_load(step3)
        pg.click(pos3)
        pg.sleep(0.8)
        pg.click(50,400)
        pg.sleep(2.5)


def process_list_left(List):
    new = []
    for i1, i2, i3, i4 in List:
        new.append((i1-18, i2+14))
    lis, aapl, spec = new.copy(), 0, []
    while len(new) != 0:
        x, y = new[0]
        spec.append((x, y))
        aapl +=1
        for x1, y1 in lis:
            if abs(x1-x) < 3 and abs(y1-y) < 3:
                new.remove((x1, y1))
    return spec
    

def process_list_right(List):
    new = []
    for i1, i2, i3, i4 in List:
        new.append((i1, i2))
    lis, aapl, spec = new.copy(), 0, []
    while len(new) != 0:
        x, y = new[0]
        spec.append((x, y))
        aapl +=1
        for x1, y1 in lis:
            if abs(x1-x) < 4 and abs(y1-y) < 4:
                new.remove((x1, y1))
    return spec


def drag_up():
    pg.mouseDown(50, 85, button='left')
    pg.moveTo(50, 756, 0.15)
    pg.sleep(0.05)
    pg.mouseDown(50, 755, button='left')
    pg.sleep(0.1)
    pg.mouseUp(50, 755, button='left')
    pg.sleep(1)


def full_screen_left():
    pg.mouseDown(1200, 700, button='left')
    pg.moveTo(201, 700, 0.15)
    pg.sleep(0.05)
    pg.mouseDown(200, 700, button='left')
    pg.sleep(0.1)
    pg.mouseUp(200, 700, button='left')
    pg.sleep(1)


def full_screen_right():
    pg.mouseDown(200, 700, button='left')
    pg.moveTo(1200, 740, 0.15)
    pg.sleep(0.05)
    pg.mouseDown(1200, 740, button='left')
    pg.sleep(0.1)
    pg.mouseUp(1200, 740, button='left')
    pg.sleep(1)


def mouse_drag_left():
    pg.mouseDown(750, 500, button='left')
    pg.moveRel(-100, 0, 0.1)
    pg.mouseUp(650, 500, button='left')

    
def mouse_drag_right():
    pg.mouseDown(750, 500, button='left')
    pg.moveRel(100, 0, 0.1)
    pg.mouseUp(850, 500, button='left')

    
def drag_left():
    global img1, img2
    img1 = ImageGrab.grab(bbox=(645,725,670,730))
    mouse_drag_left()
    FindOnScreen = pg.locateAllOnScreen(img, confidence = 0.65)
    FindOnScreen = list(FindOnScreen)
    if len(FindOnScreen) != 0:
        pg.sleep(1.5)
        FindOnScreen = pg.locateAllOnScreen(img, confidence = 0.65)
        lis = process_list_left(FindOnScreen)
        send_location(lis)
        full_screen_left()
        drag_left()
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
    FindOnScreen = pg.locateAllOnScreen(img, confidence = 0.6)
    FindOnScreen = list(FindOnScreen)
    if len(FindOnScreen) != 0:
        pg.sleep(1.5)
        FindOnScreen = pg.locateAllOnScreen(img, confidence = 0.6)
        lis = process_list_right(FindOnScreen)
        send_location(lis)
        full_screen_right()
        drag_right()
    else:
        img2 = ImageGrab.grab(bbox=(645,725,670,730))
        if img1 == img2:
            drag_up()
            drag_left()
        else:
            drag_right()


img, img1, img2 = cv.imread('KoreaFlagMinZoom.png'), None, None
step1, step2, step3 = cv.imread('Step1.png'), cv.imread('Step2.png'), cv.imread('Step3.png')

pg.moveTo(900,500)

drag_left()

print('Process Over!')
