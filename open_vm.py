from  Click_around_base import click_around
import time, win32gui

password = ""                 #your password here
x = click_around()
w = win32gui

client_window = ""            #your window name here
login = "Login"
# x.left_click(880, 450)  # click to check if connection possible
# time.sleep(1)
# print(w.GetWindowText(w.GetForegroundWindow()))

x.double_click(120,700) #open app

while client_window != w.GetWindowText(w.GetForegroundWindow()):
    x.left_click(880, 180)  # click to check if connection possible
    time.sleep(1)

x.double_click(550,300) #open desired vm

# while disclaimer_window != w.GetWindowText(w.GetForegroundWindow()):
#     x.left_click(880, 380)  # click to check if connection possible
#     time.sleep(1)

x.left_click(1050,640)

while login != w.GetWindowText(w.GetForegroundWindow()):
    time.sleep(1)
    x.left_click(880, 450)  # click to check if connection possible


x.write_mambo_jambo(password)

while client_window != w.GetWindowText(w.GetForegroundWindow()):
    x.left_click(880, 180)  # click to check if connection possible
    time.sleep(1)

x.double_click(550,300)
