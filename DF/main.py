import cv2 as cv
import pyautogui as pg


#Main
def main(img_df, img_atk, img_choose_queue, img_march_status_out, img_march_status_in):
    pg.click(wait_img(img_df, Confidence = 0.68, Attempt = 15, wait=0.4, comment='Step 1'))                                 #Dark Force
    pg.click(wait_img(img_atk, Confidence = 0.50, Attempt = 30, wait=0.8, type_continue=True, comment='Step 2'))            #Attack One time
    pg.click(wait_img(img_choose_queue, Confidence = 0.6, Attempt = 30, wait=0.8, type_continue=True, comment='Step 3', step='df'))   #Choose Diana March
    pg.click(680, 350)                                                                                                      #Press March
    verify_march_out(img_march_status_out)                                                                                  #Verify March
    wait_march_return(img_march_status_out, img_march_status_in)
    main(df_lvl_2, attack_x1, queue_1, march_status_out, march_status_returning)


#Functions
def verify_march_out(img):
    pg.sleep(5)
    march_is_out = pg.locateCenterOnScreen(img, confidence = 0.65)
    if march_is_out != None:
        print('March is set out')
    else:
        raise Exception('March Problem')
    
def wait_march_return(img_march_out, img_march_returning):
    while pg.locateCenterOnScreen(img_march_out, confidence = 0.65) != None:
        pg.sleep(1)
    pg.sleep(0.5)
    print('March is returning')
    while pg.locateCenterOnScreen(img_march_returning, confidence = 0.65) != None:
        pg.sleep(1)
    print('March returned')
    

def focus_on_df(coordinates):
    pass


def recover_vit(coord):
    for i in range(0,3):
        pg.click(coord)
        pg.sleep(0.25)
    pg.sleep(0.8)
    pg.click(844,283)
    pg.sleep(2)
    main(df_lvl_2, attack_x1, queue_1, march_status_out, march_status_returning)
        

def wait_img(img, Confidence=0.65, Attempt=40, wait=0.5, type_continue=True, comment=None, step=None):
    global vit_1, vit_1_coord
    coord_img  = None
    attempt = 0
    while coord_img == None and attempt < Attempt:
        pg.sleep(0.25)
        coord_img = pg.locateCenterOnScreen(img, confidence = Confidence)
        attempt += 1
    pg.sleep(wait)
    vit_1_coord = pg.locateCenterOnScreen(vit_1, confidence=0.63)
    if type_continue == False and coord_img == None:
        raise Exception("Image Not found")
    elif step == 'df' and coord_img == None and vit_1_coord != None:
        recover_vit(vit_1_coord)
    else:
        print(comment)
        return coord_img


#Images
df_lvl_2 = cv.imread('D://Data//temp//DF//1_DF_lvl1.png')
attack_x1 = cv.imread('D://Data//temp//DF//2_Attack_x5.png')
#other_case = cv.imread('D://Data//temp//DF//find_other.png')
queue_1 = cv.imread('D://Data//temp//DF//3_March_1.png')
march_status_out = cv.imread('D://Data//temp//DF//4_Attacking2.png')
march_status_returning = cv.imread('D://Data//temp//DF//5_Returning2.png')
vit_1 = cv.imread('D://Data//temp//DF//vit_1.png')
vit_1_coord = None

#main(df_lvl_2, attack_x1, queue_1, march_status_out, march_status_returning)
print('Over')
