import subprocess
import webbrowser

# open google site in defalt browser
webbrowser.open(
    "https://www.google.com")


# create a text file and write and wread
file = open('test1.txt', "w")
file.write("Helloa!!!")
''' if 'a' in witch run helloa stick after eatch
    other but when use "w" by one hundred run times just write one Helloa!'''
file = open('test1.txt', "r")
print(file.read())

'''
#"x" - Create - will create a file, returns an error if the file exist

#"a" - Append - will create a file if the specified file does not exist

#"w" - Write - will create a file if the specified file does not exist
'''
# open some file in drive C:
subprocess.call(
    'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe')

# open some file in drive D:
subprocess.call(
    'E:\\code\\python\\learning\\work-desc-app\\content.txt', shell=True)
