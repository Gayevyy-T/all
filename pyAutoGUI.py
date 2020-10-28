import pyautogui as p
import time

#screenWidth, screenHeight = pyautogui.size()
#currentMouseX, currentMouseY = pyautogui.position()
        #x - prawo, y = nuz
#pyautogui.moveTo(0, 100)
p.click()
for x in range(1,5):
    time.sleep(3)   #czekaje 3 sec
    p.typewrite('hello world')
    p.press('enter')
    p.press('enter')
print('done')

