import pyautogui as pg
import cv2 as cv
import os

build_img = cv.imread('D://Data//temp//Build.png')
barracks_build_img = cv.imread('D://Data//temp//Unsell_Barr.png')
barracks_build_img_selected = cv.imread('D://Data//temp//Barracks_Build.png')
stop_img = cv.imread('D://Data//temp//Check.png')
click_after_completion = cv.imread('D://Data//temp//Sample.png')


build = pg.locateCenterOnScreen(build_img, confidence=0.9)
pg.click(build)
pg.sleep(0.8)
check_ = pg.locateCenterOnScreen(barracks_build_img, confidence=0.9)

while check_ == None:
    check_ = pg.locateCenterOnScreen(barracks_build_img, confidence=0.9)
    pg.sleep(0.4)

pg.click(check_)


def build(click_pos):
    global trial
    pg.click(click_pos)
    pg.sleep(0.185)
    trial += 1
    print(trial)
    if pg.locateCenterOnScreen(stop_img, confidence = 0.6) != None:
        trail = 0
        build(click_pos)
        pg.sleep(0.38)
    elif trial < 18:
        build(click_pos)
        pg.sleep(0.6)
    elif trial == 18:
        pg.sleep(1.1)
        cont = pg.locateCenterOnScreen(stop_img, confidence = 0.6)
        if cont != None:
            trial = 0
            build(click_pos)
        else:
            pg.moveTo(pg.locateCenterOnScreen(click_after_completion, confidence = 0.65))
            os.startfile("C://Users//baliy//AppData//Local//Programs//Python//Python39//TopWar//Stop_Python//End_Python_Processes.vbs")

trial = 0

build(pg.locateCenterOnScreen(barracks_build_img_selected, confidence = 0.8))        
