import pyautogui as pg
import cv2 as cv


def delete(pos):
    #pg.click(pos)  #Aquaman Exclusive
    #pg.sleep(0.1)  #Aquaman Exclusive
    pg.mouseDown(pos)
    pg.sleep(0.3)
    del_icon = waitDelIcon()
    pg.mouseUp()
    #pg.sleep(0.1)
    pg.click(del_icon)
    ok_button = waitOkButton()
    pg.click(ok_button)


def waitDelIcon():
    del_icon_pos = None
    attempts = 1
    while del_icon_pos == None:
        del_icon_pos = pg.locateCenterOnScreen(del_icon_img, confidence = 0.65)
        #x += 5
        pg.sleep(0.05)
        if attempts == 30:
            print('Attempts reached')
            quit()
        attempts += 1
    return del_icon_pos


def waitOkButton():
    ok_button_pos = None
    while ok_button_pos == None:
        ok_button_pos = pg.locateCenterOnScreen(ok_img, confidence = 0.90)
        pg.sleep(0.05)
    return ok_button_pos


barracks_img = cv.imread('D://Data//temp//Barracks_lvl80.png')
del_icon_img = cv.imread('D://Data//temp//Delete_Icon.png')
ok_img = cv.imread('D://Data//temp//ok.png')

obj = pg.locateAllOnScreen(barracks_img, confidence = 0.63)
new = []


for i1, i2, i3, i4 in obj:
    if i2 < 690 and i2 > 120 and i1 < 1250 and i1 > 70:   #Permananet
    #if i2 < 470 and i2 > 170 and i1 < 800 and i1 > 85:
        new.append((i1+19, i2+17))
    print(i1, i2)

lis = new.copy()
aapl = 0
spec = []

while len(new) != 0:
    x, y = new[0]
    spec.append((x, y))
    aapl +=1
    for x1, y1 in lis:
        if abs(x1-x) < 3 and abs(y1-y) < 3:
            new.remove((x1, y1))


print(len(lis), len(spec), spec)


for i in spec:
    delete(i)
    pg.sleep(0.40)


