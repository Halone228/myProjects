from googletrans import Translator#!!! pip3 install googletrans==3.1.0a0 !!!!
import tkinter
import pyautogui
import keyboard
translatorr = Translator()
while True:
    c = tkinter.Tk()
    c.withdraw()
    keyboard.wait("q")
    clip = c.clipboard_get()
    print(clip)
    per = translatorr.translate(clip,dest="ru",src='en')
    print(per.text)
    c.update()
    c.destroy()
    pyautogui.alert(per.text,title = "Перевод")
    