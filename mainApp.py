import subprocess
import webbrowser

# mize kar

webbrowser.open(
    "https://plainproxies.com/")


subprocess.Popen(r'explorer /select,"E:\code\python\learning\1-learning"')

subprocess.call(
    "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", shell=True)


# for compile python code to exe file :
# first pip install pyinstaller in cmd
# seconde E:\code\python\learning\work-desc-app>pyinstaller --onefile -w mainApp.py
# notice you should run above code after cd in your app directory
