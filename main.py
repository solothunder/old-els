import configparser
import ctypes
import os
import platform
import socket
import subprocess
import sys
import shutil
from threading import Event

# 設定ファイル系
inifile = configparser.ConfigParser()
inifile.read(r'./config/config.ini', 'UTF-8')

# 遅延関数化
def wait(time):
    Event().wait(int(time))

def check_platform():
    if platform.system() == "Windows":
        # Windowsだったら解像度出すよー
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print ("Screensize", screensize,"\n")
        wait(1)
    else:
        pass

# 残り容量確認
def check_remaning_capacity():
    print('-------------------- \nHDD - SSD Check')
    total, used, free = shutil.disk_usage("/")
    print("Total: %d GB" % (total // (230)))
    print("Used: %d GB" % (used // (230)))
    print("Free: %d GB" % (free // (2**30)),"\n")

# Pingでインターネットつながってるか？
def check_ping(host_moji,count_count):
    print('-------------------- \nNetWork')
    if inifile.get('switch', 'net') == "1":
        wait(1)
        print(host_moji)
        print("...")
        if platform.system() == "Windows":
            res = subprocess.run(["ping",host_moji,"-n",count_count, "-w", "300"],stdout=subprocess.PIPE)
        else:
            res = subprocess.run(["ping",host_moji,"-c",count_count],stdout=subprocess.PIPE)
        if res.returncode == 0 :
            print("OK |")
            wait(1.7)
        else:
            print("Error (Stops the program after 15 seconds) |")
            wait(15)
            sys.exit()
        print("--------------------")
    if inifile.get('switch', 'net') == "2":
        netkekka = "Manual Pass | \n--------------------"
        print(netkekka)
    if inifile.get('switch', 'net') == "2":
        netkekka = "Manual Pass | \n--------------------"
        print(netkekka)
    if inifile.get('switch', 'net') == "0":
        pass

# プライベートIP　確認
def check_private_ip(host, port):
    if inifile.get('switch', 'netip') == "1":
        print("IP (Private)")
        wait(0.3)
        print("...")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host, int(port)))
        print(s.getsockname()[0])
        wait(1.7)
    else:
        pass

# ファイル確認
def check_file_isfile(path):
    is_file = os.path.isfile(str(path))
    if is_file:
        print(f"{str(path)}")
        wait(0.3)
        print("...")
        wait(0.3)
        print("OK |")
    else:
        print(f"{str(path)}")
        wait(0.3)
        print("..........")
        wait(0.3)
        print("Error (Stops the program after 15 seconds) |")
        wait(15)
        sys.exit()

def yes_no_input():
    while True:
        choice = input("Continue? (Please respond with 'yes' or 'no') [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            sys.exit()

elsversion = "2.1.5"
wait(1)
print("ELS (Error Logs System) Python Edition  Version",elsversion)
wait(1)



# 残り容量確認
check_remaning_capacity()

wait(1.7)
print('ELS Start')
wait(1.7)

# Pingでインターネットつながってるか？
check_ping(inifile.get('settings', 'pinghost'),inifile.get('settings', 'pingtime'))

# プライベートIP　確認
check_private_ip(inifile.get('settings', 'iptesthost'), inifile.get('settings', 'iptestport'))

# ファイル確認（pathの変数のところにファイル名（パスも）書いてね）
path = ['addfiles/a.txt', 'addfiles/b.txt', 'addfiles/c.txt']
if inifile.get('switch', 'file') == "1":
    print('-------------------- \nFile')
    for pathcount in path:
        check_file_isfile(pathcount)
    print('--------------------')
else:
    pass

if __name__ == '__main__':
    if yes_no_input():
        # 起動時のコメント
        print(inifile.get('advanced', 'startprint'))
        wait(1)
        # res = subprocess.run(".\users\user\document\lllll.exe", stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
