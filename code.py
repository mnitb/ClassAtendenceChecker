#20/09/2021

#initializing libraries

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os,time
from datetime import datetime
#banner

banner = '''
_____                _____                            _____                    _____                    _____                _____                    _____          
         /\    \              |\    \                          /\    \                  /\    \                  /\    \              /\    \                  /\    \         
        /::\    \             |:\____\                        /::\____\                /::\____\                /::\    \            /::\    \                /::\    \        
       /::::\    \            |::|   |                       /::::|   |               /::::|   |                \:::\    \           \:::\    \              /::::\    \       
      /::::::\    \           |::|   |                      /:::::|   |              /:::::|   |                 \:::\    \           \:::\    \            /::::::\    \      
     /:::/\:::\    \          |::|   |                     /::::::|   |             /::::::|   |                  \:::\    \           \:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \         |::|   |                    /:::/|::|   |            /:::/|::|   |                   \:::\    \           \:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \        |::|   |                   /:::/ |::|   |           /:::/ |::|   |                   /::::\    \          /::::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \       |::|___|______            /:::/  |::|___|______    /:::/  |::|   | _____    ____    /::::::\    \        /::::::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\ ___\      /::::::::\    \          /:::/   |::::::::\    \  /:::/   |::|   |/\    \  /\   \  /:::/\:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\ ___\ 
/:::/__\:::\   \:::|    |    /::::::::::\____\        /:::/    |:::::::::\____\/:: /    |::|   /::\____\/::\   \/:::/  \:::\____\    /:::/  \:::\____\/:::/__\:::\   \:::|    |
\:::\   \:::\  /:::|____|   /:::/~~~~/~~              \::/    / ~~~~~/:::/    /\::/    /|::|  /:::/    /\:::\  /:::/    \::/    /   /:::/    \::/    /\:::\   \:::\  /:::|____|
 \:::\   \:::\/:::/    /   /:::/    /                  \/____/      /:::/    /  \/____/ |::| /:::/    /  \:::\/:::/    / \/____/   /:::/    / \/____/  \:::\   \:::\/:::/    / 
  \:::\   \::::::/    /   /:::/    /                               /:::/    /           |::|/:::/    /    \::::::/    /           /:::/    /            \:::\   \::::::/    /  
   \:::\   \::::/    /   /:::/    /                               /:::/    /            |::::::/    /      \::::/____/           /:::/    /              \:::\   \::::/    /   
    \:::\  /:::/    /    \::/    /                               /:::/    /             |:::::/    /        \:::\    \           \::/    /                \:::\  /:::/    /    
     \:::\/:::/    /      \/____/                               /:::/    /              |::::/    /          \:::\    \           \/____/                  \:::\/:::/    /     
      \::::::/    /                                            /:::/    /               /:::/    /            \:::\    \                                    \::::::/    /      
       \::::/    /                                            /:::/    /               /:::/    /              \:::\____\                                    \::::/    /       
        \::/____/                                             \::/    /                \::/    /                \::/    /                                     \::/____/        
         ~~                                                    \/____/                  \/____/                  \/____/                                       ~~              
                                                                                                                                                                               
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
length=175
#user listing 
list1=[]
with open("list.txt", 'rb') as f:
    while True:
        line = f.readline()
        if not line:
            break
        list1.append(line.decode("utf-8")[:-2])

#os.system('mode 176,60')



#initialize variables

options = Options()
options.add_argument('--log-level=3')
options.add_argument("--mute-audio")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome( executable_path=r"chromedriver.exe",options=options)
f = open("alt.txt", "r")
username,password=f.read().split()
max = 0
neo = ""

#auto login procedure
sleepDelay = 2  # increase if you have a slow internet connection
timeOutDelay = 30
def wait_and_find_ele_by_id(html_id, timeout=timeOutDelay):
    time.sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = driver.find_element_by_id(html_id)
        except:
            time.sleep(sleepDelay)
        else:
            return ele


def wait_and_find_ele_by_link_text(text, timeout=timeOutDelay):
    time.sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = driver.find_element_by_link_text(text)
        except:
            time.sleep(sleepDelay)
        else:
            return ele





def login():
    wait_and_find_ele_by_id('i0116').send_keys(username)  # enter username
    wait_and_find_ele_by_id('idSIButton9').click()  # click next
    wait_and_find_ele_by_id('i0118').send_keys(password)  # enter password
    wait_and_find_ele_by_id('idSIButton9').click()  # click next
    wait_and_find_ele_by_id('idSIButton9').click()  # click yes to stay signed in
    web_ele = wait_and_find_ele_by_link_text('Use the web app instead', 5)
    if web_ele is not None:
        web_ele.click()

#main
    
driver.get('https://teams.microsoft.com')
time.sleep(sleepDelay)
login()
os.system('cls')
print(banner)

#main loop
while True:
    if input() == "":
        mid=datetime.now()
        print((int(length/2-len(str(mid))/2))*" ",end='')
        print(mid)
        f=driver.page_source
        doc = BeautifulSoup(f,"html.parser")
        name = doc.find_all(attrs={'data-tid': True})
        attended = []
        missed = []
        strangers=[]
        for i in range(len(name)):
            try:
                tg = name[i]
                tg1 = tg.attrs['data-tid']
                if ('participantsInCall-') in tg1:
                    person = tg1[19:len(tg1)]
                    if person in list1:
                        attended.append(person)
                    else:
                        strangers.append(person)
                elif "attendeesInMeeting-" in tg1:
                    person = tg1[19:len(tg1)]
                    if person in list1:
                        attended.append(person)
                    else:
                        strangers.append(person)
            except:
                pass
        atd=[]
        for i in list1:
            if i not in attended:
                missed.append(i)
            else:
                atd.append(i)
        if "Nguyen Viet Anh" in attended:
            attended.insert(attended.index("Nguyen Viet Anh"), "Nguyen Duc Anh")
        else:
            missed.insert(missed.index("Nguyen Viet Anh"), "Nguyen Duc Anh")
        print('--------------------------------------------------------------------------những người có trong lớp là-----------------------------------------------------------------------')
        for i in atd:
            print((int(length/2-len(i)/2))*" ",end='')
            print(i)
        print('-----------------------------------------------------------------------những người không có trong lớp là--------------------------------------------------------------------')
        print()
        for i in missed:
            print((int(length/2-len(i)/2))*" ",end='')
            print(i)
        print("")
        print('\nSố người không có trong lớp là: ', len(missed),'\n')
        print("-"*length)
        print('----------------------------------------------------------------------những người không phải học sinh là--------------------------------------------------------------------')
        if len(strangers)!=0:
            for i in strangers:
                print((int(length/2-len(i)/2))*" ",end='')
                print(i)
        else:
            print("không có")
    else:
        os.system('cls')
        print(banner)





