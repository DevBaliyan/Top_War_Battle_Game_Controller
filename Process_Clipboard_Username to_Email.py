import csv
import pyperclip as pc
import ctypes
#from pyautogui import write, sleep


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


file = open('D://Email_to_Username.csv')
csv_reader = csv.reader(file)


list_username = []
list_mail = []
list_copied_usernames = []

for i in csv_reader:
    list_username.append(i[-1])
    list_mail.append(i[0])


pc.copy('')
n, l = 0, 0

while True:
    get_clipboard = pc.waitForPaste()
    l += 0
    if get_clipboard in list_username:
        index_username = list_username.index(get_clipboard)
        print('Found at -', index_username)
    else:
        #sleep(2)
        #write('Continue, Sir')
        pc.copy('')
        continue
    mail = list_mail[index_username]
    if get_clipboard not in list_copied_usernames:
        n += 1
        print(n, get_clipboard, mail)
        list_copied_usernames.append(get_clipboard)
    pc.copy('')
    #sleep(1.8)
    #write('Continue, Sir')
    #Mbox(get_clipboard, mail, 1)
