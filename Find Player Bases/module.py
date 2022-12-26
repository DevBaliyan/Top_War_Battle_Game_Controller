def wait_for_img_load(cv_image, Confidence=0.85):
    coord_on_screen = None
    attempts = 1
    while coord_on_screen == None:
        coord_on_screen = pg.locateCenterOnScreen(cv_image, confidence = Confidence)
        #x += 5
        pg.sleep(0.15)
        if attempts == 30:
            print('Attempts reached')
            quit()
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
        pg.sleep(3)
