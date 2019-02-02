# igbot
Minimal Instagram bot

![status](https://img.shields.io/badge/status-stagnant-red.svg?style=flat-square) 
![version](https://img.shields.io/badge/version-31.01.19-lightgrey.svg?style=flat-square)

---
## Installing
#### Download
```
git clone https://github.com/decoxviii/igbot.git ; cd igbot
```

#### Prerequisites
+ selenium
+ pyyaml
+ Firefox Browser

```
# for install selenium and pyyaml
sudo -H pip3 install -r requirements.txt
```

**Selenium** requieres a driver ([geckodriver](https://github.com/mozilla/geckodriver/releases)) to interface with browser Firefox, which needs to be installed before the below tests can be run. Make sure it's in your PATH, e. g., place it in `/usr/bin/` or `/usr/local/bin/`.

```
sudo mv geckodriver /usr/bin/
```

Failure to observe this step will give you an error `selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.`

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

