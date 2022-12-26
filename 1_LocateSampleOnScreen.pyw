import pyautogui as pg
import cv2 as cv

img = cv.imread('D://Data//temp//Sample.png')

pos = pg.locateCenterOnScreen(img, confidence = 0.7)

pg.moveTo(pos)

pg.write('Continue, Sir')
