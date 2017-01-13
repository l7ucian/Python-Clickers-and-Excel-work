from  Click_around_base import click_around
import time, win32gui

conti_password = "Conti2Pass"
#login_window = "Cisco AnyConnect | Auburn Hills"
login_window = "Cisco AnyConnect | Frankfurt"

w = win32gui
x = click_around()

x.double_click(120,750)  #open cisco
time.sleep(2)
x.left_click(1810,955)   #good connect to vpn coordinates
while login_window != w.GetWindowText(w.GetForegroundWindow()):
    x.left_click(1350, 860)  # click to check if connection possible
    time.sleep(1)
x.left_click(1350,910)   #good passwird to connect to vpn coordinates
x.write_mambo_jambo(conti_password)

