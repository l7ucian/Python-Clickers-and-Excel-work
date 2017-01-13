import win32api, win32con, win32com.client
import glob,os

def double_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def left_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def write_mambo_jambo():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys("{M}", 0)
    shell.SendKeys("{a}", 0)
    shell.SendKeys("{f}", 0)
    shell.SendKeys("{i}", 0)
    shell.SendKeys("{a}", 0)
    shell.SendKeys("{ENTER}", 0)

os.chdir("D:\\")
for file in glob.glob("*.pdf"):
    print(file)
os.system("start "+"C++InternationalStandard.pdf")
#left_click(560,470)
#write_mambo_jambo()
