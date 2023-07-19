'''

 / Github: https://github.com/MEMEZNUT999/fluxus-key-bypasser

 / V2 version, runnning into errors? Make an issue!

'''
import sys
import time
from seleniumwire import webdriver
from seleniumwire.utils import decode
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
from fake_useragent import UserAgent

# colorama for windows, will not affect other platforms
init()

def getkey(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    code_elements = soup.find_all('code')
    if len(code_elements) > 1:
        return code_elements[1].text.strip()
    return None

def readhwid(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def writehwid(filename, hwid):
    with open(filename, 'w') as file:
        file.write(hwid)

def gethwid():
    filename = "savedhwid.bypass"

    hwid = readhwid(filename)
    if hwid is not None:
        print(Fore.GREEN + "[LOG] HWID found in the file. Using that.")
        return hwid
    else:
        print(Fore.YELLOW + "[WARN] No HWID found in the file.")
        hwid = input("[PROMPT] Enter your HWID: ")
        writehwid(filename, hwid)
        print(Fore.GREEN + "[LOG] HWID saved to the file. Running program now.")
        return hwid


def main():
    print(Fore.CYAN + "[*] Please support me by starring the repo!")
    time.sleep(1)
    hwid = gethwid()
    print(Fore.WHITE + "[!] Program is starting, if this takes longer than 1 minute, restart.")
    print(Style.RESET_ALL)
    base_url = f"https://flux.li/windows/start.php?HWID={hwid}"
    UA = UserAgent()
    agent = UA.random
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # https://www.selenium.dev/blog/2023/headless-is-going-away/
    options.add_argument(f"user-agent={agent}")
    options.add_argument("window-size=1400,600")
    options.add_argument("log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(base_url)
        time.sleep(5)
        driver.header_overrides = {'Referer': base_url}
        driver.get(f"{base_url}&7b20bcc1dfe26db966bb84f159da392f=false")
        driver.header_overrides = {'Referer': 'https://linkvertise.com'}
        driver.get("https://fluxteam.net/windows/checkpoint/check1.php")
        time.sleep(3) 
        driver.get("https://fluxteam.net/windows/checkpoint/check2.php")
        time.sleep(3) 
        driver.get("https://fluxteam.net/windows/checkpoint/main.php")
        for request in driver.requests:
            if request.url == "https://fluxteam.net/windows/checkpoint/main.php":
                body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                key = getkey(body)
                print(Fore.GREEN + f"[LOG] Your key is: {key}")

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
