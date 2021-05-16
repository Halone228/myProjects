from tkinter import Button
import keyboard
import time
import pyautogui as pa
iter = int(input("Кол-во повторений: "))
keyboard.wait('esc')
pa.moveTo(668, 707)
for i in range(iter):
    pa.click()
    keyboard.press_and_release('ctrl + v')
    keyboard.press_and_release('enter')
    time.sleep(0.2)
    if i in [x*20 for x in range(1,10001)]:
        pa.moveTo(123, 50)
        pa.click()
        time.sleep(10)
        pa.moveTo(329, 234)
        time.sleep(1.5)
        pa.click()
        pa.moveTo(668, 707)
pa.alert("Все готово",title="Complete", button='Закрыть нахуй')
