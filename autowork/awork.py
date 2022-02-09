# -- coding: utf-8 --
import pyautogui as pa
import time


help_pos = pa.locateCenterOnScreen('D:\\workspace\\MyProject\\autowork\\help.png')
print(help_pos)
# goto_help_pos = pa.center(help_pos)

pa.moveTo(help_pos, duration=1)
pa.click()
pa.moveTo(pa.locateCenterOnScreen('D:\\workspace\\MyProject\\autowork\\about.png'))
pa.click()



# size = pa.size()
# print(size)

# mouse_position = pa.position()
# print(mouse_position)
#
# print(pa.onScreen(100, 100))
#
# pa.moveTo(10, 100, duration=0.5)
#
# pa.moveTo(size.width / 2, size.height / 2, duration = 2)
#
# last_position = pa.position()
#
# while True:
#     new_position = pa.position()
#     if new_position != last_position:
#         print(new_position)
#         last_position = new_position



