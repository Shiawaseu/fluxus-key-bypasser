# Ive used threading :)

import subprocess
state = True
def install(package_name):
    try:
        subprocess.run(["pip", "install", package_name], check=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(f"Package {package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
print("Checking for missing packages")
try: 
    import requests
except ImportError:
    print("Installing requests ... ")
    install("requests")
    print("Installed requests!")
    import requests
try: 
    import keyboard
except ImportError:
    print("Installing keyboard ... ")
    install("keyboard")
    import keyboard
    print("Installed keyboard!")
try: 
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing BeautifulSoup4 ... ")
    install("beautifulsoup4")
    print("Installed BeautifulSoup4!")
    from bs4 import BeautifulSoup
print("Done!\n")
import threading as thread
import time
THREAD = True
COMMON_COOKIE = "Anti-Bypass=BypassersKHTTP_VERSION5069e4e61337c2fbea2368f9da1a07725f2a65bb1eab2d8de6dc9cf83e7a683e; .pipe=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJLMGc4SjNsRmY1TW43UWw4bVh5bytpNnVBeGh4aWFSYTU2bldDZEcxQnlNPSIsImUiOjE2ODkyNTAyODEsImlzc3VlZCI6MTY4OTI0NjY4MS44MzksInNhbHQiOiJzYWx0eSIsImNvbm5lY3RvciI6LTF9.tHnUGnosgCctAafGTgta4F1_1KQezhvdIATrj9YwQU0"
COMMON_HEADER = {
    'Referer': 'https://linkvertise.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def req(url, headers):
    if THREAD == True:
        return requests.get(url, headers=headers)
    return False

def bypass(hwid):
    if THREAD == True:
        start_url = f"https://flux.li/windows/start.php?HWID={hwid}"
        print("Bypassing. Please be patient!")
        if req(start_url, headers=COMMON_HEADER) == False: return h()

        if req(f"https://flux.li/windows/start.php?7b20bcc1dfe26db966bb84f159da392f=false&HWID={hwid}",
                     headers={'Referer': start_url, 'Cookie': COMMON_COOKIE}) == False: return h()
        if req("https://fluxteam.net/windows/checkpoint/check1.php", headers=COMMON_HEADER) == False: return h()
        if req("https://fluxteam.net/windows/checkpoint/check2.php", headers=COMMON_HEADER) == False: return h()
        response = req("https://fluxteam.net/windows/checkpoint/main.php", headers=COMMON_HEADER)
        if response == False: return h()
        parsed = BeautifulSoup(response.content, 'html.parser')
        key = parsed.select("body > main > code:nth-child(5)")[0].text.strip()
        print("Fluxus key has been activated! \nKey: " + key + '\n')
        input("Fun fact: Fluxus key is always static, it rarely gets changed. \nIf you dont get to see a key, its very likely patched. ")
        exit()

def h():
    global state
    try:
        with open("hwid.txt", "r+") as f:
            hwid = f.readline().strip()
            if not hwid:
                state = False
                hwid = input("Enter HWID: ")
                f.seek(0)
                f.write(hwid)
                state = True
    except FileNotFoundError:
        with open("hwid.txt", "w") as f:
            state = False
            hwid = input("Enter HWID: ")
            f.write(hwid)
            state = True
    bypass(hwid)

def wipe():
    if state == True:
        global THREAD
        with open("hwid.txt", "w") as f:
                    f.write("")
        THREAD = False
        print("Wiped HWID, Restarting")
        time.sleep(1)
        THREAD = True
        h()

if __name__ == "__main__":
    keyboard.add_hotkey("c", wipe)
    print("PRESS 'C' TO WIPE OUT THE HWID SO YOU CAN USE ANOTHER ONE (only works while bypassing old hwid lol)")
    h()
    t1 = thread.Thread(target=bypass)
