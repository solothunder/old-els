from threading import Event
import platform
import os

# 下準備 >>>>↓↓↓↓↓↓
# バージョン
elsversion = "0.6"
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

if osprat == "Windows" :
 print("Your Execution Operating System (OS) is" , osprat , "System")


Event().wait(delayt)

print('ELS Start')
Event().wait(delayt)

# （ここまで）までマニュアルパス（手動）
print('-------------------- \nNetWork')
Event().wait(delay)
netkekka = "Manual Pass | \n--------------------"
print(netkekka)
#  (ここまで)

# ファイル確認（pathの変数のところにファイル名（パスも）書いてね）
print('-------------------- \nFile')
path = ['addfiles/a.txt', 'addfiles/b.txt', 'addfiles/c.txt']
for pathcount in path:

 is_file = os.path.isfile(pathcount)
 
 if is_file:
    filekekka = (f"{pathcount} OK |")
    print(f"{pathcount} OK |")
    Event().wait(delayaa)
else:
    filekekka = (f"{pathcount} Caution |")
    print(filekekka)
    Event().wait(delayaa)

print('--------------------')

def yes_no_input():
    while True:
        choice = input("Start? (Please respond with 'yes' or 'no') [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('OK Start')
        Event().wait(delay)
          