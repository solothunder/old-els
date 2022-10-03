import configparser
import ctypes
import os
import platform
import socket
import subprocess
import sys
from threading import Event
import time
import ctypes

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
    if platform.system() == "Windows":
        if is_file:
            ENABLE_PROCESSED_OUTPUT = 0x0001
            ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING

            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            kernel32.SetConsoleMode(handle, MODE)
            GREEN = "\033[32m"
            RED = '\033[31m'
            END = '\033[0m'
            print("\r",pathcount,GREEN + " ... OK" + END, end="")
            time.sleep(0.5)
        else:
            print("\r",pathcount,RED + " .......... Error (Stops the program after 15 seconds" + END, end="")
            wait(15)
            sys.exit()
    else:
        if is_file:
            print("\r{0} ... OK".format(pathcount), end="")
            time.sleep(0.5)
        else:
            print("\r{0} ... Error (Stops the program after 15 seconds)".format(pathcount), end="")
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
    print('\n--------------------')
else:
    pass

if __name__ == '__main__':
    if yes_no_input():
        # 起動時のコメント
        print(inifile.get('advanced', 'startprint'))
        wait(1)
        # res = subprocess.run(".\users\user\document\lllll.exe", stdout=subprocess.PIPE, shell=True, encoding="shift-jis")