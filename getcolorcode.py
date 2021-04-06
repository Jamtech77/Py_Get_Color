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
    if pause_flag < 2:
        curPOS = pygui.position()
        im = pygui.screenshot()
        pix = im.getpixel((curPOS[0], curPOS[1]))

        output = ''

        if pause_flag == 1:
            # print(hex(pix[0]).replace('0x', ''), hex(pix[1]).replace('0x', ''), hex(pix[2]).replace('0x', ''))
            print(pix)
        else:
            for color in pix:
                color_hex = hex(color).replace('0x', '') + ' '
                if color < 16:
                    color_hex = '0' + color_hex
                output += color_hex

            print(output)

        time.sleep(0.1)

        
