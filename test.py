import threading
import subprocess

def thread_second():
    subprocess.call(["python", "scripts/Timer.py"])

processThread = threading.Thread(target=thread_second)
processThread.start()

print("timer runnning in background")