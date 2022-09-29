from threading import Event
import platform
import os
import sys
import subprocess
import datetime
import socket
import shutil
import ctypes
# 下準備 >>>>↓↓↓↓↓↓
# バージョン
elsversion = "1.3"
# 遅延速度
delay = 1
delayt = 1.7
delayaa = 0.3

Event().wait(delay)

# バージョン出力（ELS (Error Logs System) Python Version O.O）

print("ELS (Error Logs System) Python Edition  Version", elsversion)
Event().wait(delay)

# OS判別
osprat = platform.system()
print("Your Execution Operating System (OS) is" , osprat , "System")
# Windowsだったら解像度出すよー
if osprat == "Windows":
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print ("Screensize", screensize,"\n")
    Event().wait(delay)

dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y/%m/%d %H:%M:%S'))

# 残り容量確認
print('-------------------- \nHDD - SSD Check')
total, used, free = shutil.disk_usage("/")

print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)),"\n")

Event().wait(delayt)
print('ELS Start')
Event().wait(delayt)

# Pingでインターネットつながってるか？
print('-------------------- \nNetWork')
Event().wait(delay)
host = "google.com"
print("google.com")
print("...")
res = subprocess.run(["ping",host,"-n","8", "-w", "300"],stdout=subprocess.PIPE)
# netkekka = "Manual Pass | \n--------------------"
# print(netkekka)
if res.returncode == 0 :
    print("OK |")
else:
    print("Error (Stops the program after 15 seconds) |")
    Event().wait("15")
    sys.exit()
print("-----------------------------")

# プライベートIP　確認
print("IP (Private)")
Event().wait(delayaa)
print("...")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])

Event().wait(delay)

# ファイル確認（pathの変数のところにファイル名（パスも）書いてね）
print('-------------------- \nFile')
path = ['addfiles/a.txt', 'addfiles/b.txt', 'addfiles/c.txt']
for pathcount in path: 
    is_file = os.path.isfile(pathcount)
    if is_file:
        print(f"{pathcount}")
        Event().wait(delayaa)
        print("...")
        Event().wait(delayaa)
        print("OK |")
    else:
        print(f"{pathcount}")
        Event().wait(delayaa)
        print("..........")
        Event().wait(delayaa)
        print("Error (Stops the program after 15 seconds) |")
        Event().wait("15")
        sys.exit()


print('--------------------')

def yes_no_input():
    while True:
        choice = input("Start? (Please respond with 'yes' or 'no') [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            sys.exit()


if __name__ == '__main__':
    if yes_no_input():
        print('OK Start')
        Event().wait(delay)
        # res = subprocess.run(".\users\user\document\lllll.exe", stdout=subprocess.PIPE, shell=True, encoding="shift-jis")