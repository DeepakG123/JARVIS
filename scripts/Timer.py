from threading import Timer
import ctypes
from sys import platform
import subprocess
 # time_stop = input("Stop time? ")
    # if(time_stop != ""):
    #     t.cancel()
    #     print("Timer interrupted")
#t.cancel() stops timer


if platform == "win32":
    def time_over():
        print("Time is up")
        ctypes.windll.user32.MessageBoxW(0, "Timer is Up", "Attention", 1)


elif platform == "darwin":
    def time_over():
        print("Time is up")



def timer():
    time = int(input('Set timer to: '))
    try:
        t = Timer(time, time_over)
        t.start()
    except Exception as e:
        print(e)



# #----------------Main Method------------
# timer()
