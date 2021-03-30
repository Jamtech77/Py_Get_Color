import pyautogui as pygui
import time
import threading

pygui.FAILSAFE = True

pause_flag = 0
def wait_for_input():
    global pause_flag
    while 1:
        pause_flag = int(input())

input_thread = threading.Thread(target=wait_for_input)
input_thread.start()

while 1:
    if pause_flag == 0:
        curPOS = pygui.position()
        im = pygui.screenshot()
        pix = im.getpixel((curPOS[0], curPOS[1]))
        print(pix)
        time.sleep(0.5)
