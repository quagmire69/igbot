import sys, os
import random
import time
import argparse

from getpass import getpass
from yaml import load

try:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from igbot import banner
    from igbot import core

except Exception as e:
    print(' e:', e)

def main():
    # load data
    data = open('config.yml').read()
    data = load(data)

    USER = data['USER']
    TAGS = data['TAGS']

    # set user data
    username = USER['username'] if USER['username'] else input(" % username: ")
    password = USER['password'] if USER['password'] else getpass(prompt=" % password: ")

    # run
    if TAGS['tags']:
        ig = core.IGBot(username, password)
        ig.login()
        [ig.hashtag(tag, TAGS['like']) for tag in TAGS['tags']]
        ig.close_browser()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version')
    args = parser.parse_args()
    
    banner.print_banner()
    main()
