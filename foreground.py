import win32gui, win32com.client
import time, ctypes

time.sleep(4)
w = win32gui

ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt
ctypes.windll.user32.keybd_event(0x09, 0, 0, 0)  # Tab



