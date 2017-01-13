import win32gui
import time
from  Click_around_base import click_around

x = click_around()
w = win32gui
#Cisco AnyConnect | Auburn Hills
#Disclaimer
login_window = "Cisco AnyConnect | Auburn Hills"

while login_window != w.GetWindowText(w.GetForegroundWindow()):
    x.left_click(1350, 860)  # check if connection possible
    time.sleep(1)