import pyautogui, time

duration = input("How long?: ")
count = 0

while int(duration) != count:
    pyautogui.click()
    time.sleep(60)
    count += 1
pyautogui.click()
print("The time has finished!!!")