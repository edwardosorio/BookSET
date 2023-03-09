# BookSET - Bookmarks Social Engineer Tool

A simple script for Post-Exploitation - by @_mrpack

This script was generated to modify all URLs in BookMarks from some web browsers like Google Chrome, Brave and Edge.

This script can be used to capture some credentials with Phishing sites or just redirect the "victim" to your EvilServer.


# 🔴: How it works!

Ok... first of all we need to install some libraries:

```bash
pip install -r requirements.txt

```
thats it :D !!

## Help !

if you need to know the parameters from the script pls type:

```bash
python bookSET.py -h


 ____              _     ____  _____ _____
| __ )  ___   ___ | | __/ ___|| ____|_   _|
|  _ \ / _ \ / _ \| |/ /\___ \|  _|   | |
| |_) | (_) | (_) |   <  ___) | |___  | |
|____/ \___/ \___/|_|\_\|____/|_____| |_|


just a simple post-exploitation tool :)

usage: bookSET.py [-h] [-recon] [-replace]

Get and Replace all Urls from Google Chrome BookMarks

optional arguments:
  -h, --help  show this help message and exit
  -recon      Get all URLs Bookmarks
  -replace    Replace URLs Bookmarks


```


## [+] Recon Mode 

If you want to know what BookMarks the target has, then we just need to execute the following command line:
```bash
python bookSET.py -recon

```

and the output should be something like this:

```bash

 ____              _     ____  _____ _____
| __ )  ___   ___ | | __/ ___|| ____|_   _|
|  _ \ / _ \ / _ \| |/ /\___ \|  _|   | |
| |_) | (_) | (_) |   <  ___) | |___  | |
|____/ \___/ \___/|_|\_\|____/|_____| |_|

 
[+] Getting Urls from BookMarks:
 
 - https://www.facebook.com
 - https://www.bank.com
 - https://www.twitter.com
 - https://www.instagram.com
 - https://intranet.companie.org

[+] Total of BookMarks identified : [5]

```

## [+] Replace Mode

Now that we know all the BookMark that the target has, we can check all the URLs and just make a "fake website"  for each URL that we want ;) :

```bash
python bookSET.py -replace

```

and the output should be something like this:

```bash

 ____              _     ____  _____ _____
| __ )  ___   ___ | | __/ ___|| ____|_   _|
|  _ \ / _ \ / _ \| |/ /\___ \|  _|   | |
| |_) | (_) | (_) |   <  ___) | |___  | |
|____/ \___/ \___/|_|\_\|____/|_____| |_|


just a simple post-exploitation tool :)

[+] URLs modified:

     [-] https://www.fakebank.com/
     [-] https://intranet.fakecompanie.org/

[+] Total of BookMarks replaced : [2]


```

## [+] bookmarks.json file content

The content of "bookmarks.json" it's easy to understand, the "current_url" it's the URL that we want to change and replace it with "new_url" instead.

```bash

{
    "bookmark_bar": [
      {
        "current_url": "https://www.bank.com/",
        "new_url": "https://www.fakebank.com/"
      },
      {
        "current_url": "https://intranet.companie.org/",
        "new_url": "https://intranet.fakecompanie.org/"
      }
    ]
  }
  
  ```

NOTE: This script was tested for the following Web Browsers:

- Google Chrome
- Edge
- Brave

You just need to change the Browser Path
