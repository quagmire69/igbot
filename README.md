# igbot
Minimal Instagram bot

![status](https://img.shields.io/badge/status-Building-red.svg?style=flat-square) 
![version](https://img.shields.io/badge/version-31.01.19-lightgrey.svg?style=flat-square)

---
## Installing
#### Prerequisites
+ selenium
+ pyyaml

```
sudo -H pip3 install -r requirements.txt
```

**Selenium** requires a driver to interface with the chosen browser. Firefox, for example, requires [geckodriver](https://github.com/mozilla/geckodriver/releases), which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error `selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.`

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

| Browser  |                                                                       |
| -------- | --------------------------------------------------------------------- |
| Chrome:  | https://sites.google.com/a/chromium.org/chromedriver/downloads        |
| Edge:    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Firefox: | https://github.com/mozilla/geckodriver/releases                       |
| Safari:  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          |


#### Download
```
git clone https://github.com/decoxviii/igbot.git
```

---
## Running the tests
All the tests were done in **Ubuntu 18.04.1**

1. Set tags and number likes `vim config.yml`:

```yml
# DATA

USER:
    username: # your username
    password: # your password

TAGS:
    # I like <num> photos
    like: 100
    
    # List tags
    tags:
        - 'foggy'
        - 'trees'
        - 'niebla'
```
2. Run igbot:
```
python3 bin/igbot.py
```
---
## Author
 + **decoxviii** 

## License
This project is licensed under the [GPL-3.0](https://github.com/decoxviii/igbot/blob/master/LICENSE) License

