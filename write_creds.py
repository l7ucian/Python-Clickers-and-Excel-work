from  Click_around_base import click_around
import time,ctypes
import win32con, win32com.client

password = ""
x = click_around()
the_line = ""

ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt
assert isinstance(ctypes.windll.user32, object)
ctypes.windll.user32.keybd_event(0x09, 0, 0, 0)  # Tab
time.sleep(1)
ctypes.windll.user32.keybd_event(0x09, 0, 0x0002, 0) #~Tab
ctypes.windll.user32.keybd_event(0x12, 0, 0x0002, 0) #~Alt

with open('D:/Un_work_related/connect_log.txt', encoding='utf-8') as log_file:
    while "" not in the_line:            # line that shows that one is ready to input pass and login
        for line in log_file:
            the_line = line
print(the_line)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{ENTER}", 0)
x.write_mambo_jambo(password)

