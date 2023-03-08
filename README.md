# BookSET
A simple script for Post-Exploitation - Red Team

This script was generated to modify all URLs in BookMarks from Google Chrome, this script can be use for capture some credentials with Phishing sites or just redirect the victim to your EvilServer.


# 🔴: How it works!

## [+] Recon Mode 
If we want to know what BookMarks the target has, then we just need to execute the following commandline:
```bash
python bookSET.py -recon

```

and the output should be something like this:

```bash

 /$$                           /$$        /$$$$$$  /$$$$$$$$ /$$$$$$$$
| $$                          | $$       /$$__  $$| $$_____/|__  $$__/
| $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$| $$  \__/| $$         | $$   
| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/|  $$$$$$ | $$$$$      | $$   
| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/  \____  $$| $$__/      | $$   
| $$  | $$| $$  | $$| $$  | $$| $$_  $$  /$$  \ $$| $$         | $$   
| $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$$$$$$$   | $$   
|_______/  \______/  \______/ |__/  \__/ \______/ |________/   |__/   
                                                                      
 
[+] Getting Urls from BookMarks
 
 - https://www.facebook.com
 - https://www.bank.com
 - https://www.twitter.com
 - https://www.instagram.com
 - https://intranet.companie.org

[+] Total of BookMarks identified : 5

```

## [+] Replace Mode

Now that we know all the BookMark that the target has, we can check all the urls and just make a "fake website" ;) :

```bash
python bookSET.py -replace

```

and the output should be something like this:

```bash

 /$$                           /$$        /$$$$$$  /$$$$$$$$ /$$$$$$$$
| $$                          | $$       /$$__  $$| $$_____/|__  $$__/
| $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$| $$  \__/| $$         | $$   
| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/|  $$$$$$ | $$$$$      | $$   
| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/  \____  $$| $$__/      | $$   
| $$  | $$| $$  | $$| $$  | $$| $$_  $$  /$$  \ $$| $$         | $$   
| $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$$$$$$$   | $$   
|_______/  \______/  \______/ |__/  \__/ \______/ |________/   |__/   
                                                                      
 
[+] Replacing the Urls from BookMarks...

[+] Done!

[+] Total of BookMarks replaced : 5

```



