import os
import pyautogui  # yee GUI kaam aata hai click karne ka
import keyboard  # for writing and press
from time import sleep   # thoda kaam ko dehere karne ka

os.startfile("D:\DESKTOP APPS\Sublime Text\sublime_text.exe")   # location ke konsa app kholna hai

sleep(2)
pyautogui.click(x=30, y=206)  # isme location hai display ke coordinates
pyautogui.click(x=45, y=231)
pyautogui.click(x=161, y=286)

sleep(3)
keyboard.write("Hii My name is Saurabh From Farasawani \n IM currently stayinng to My Didi Homes \n \n") #isme likhenge ki karna
keyboard.write("Im very excited to go home on wedding ")