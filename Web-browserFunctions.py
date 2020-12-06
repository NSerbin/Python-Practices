#!/usr/bin/env python3

#Check adress in google Maps from clipboard
import webbrowser as w
import sys
import pyperclip as p

def adressChecker():
    sys.argv
    if len(sys.argv) > 1:
        adress = ' '.join(sys.argv[1:])
    else:
        adress = p.paste()
    w.open(f"https://www.google.com.ar/maps/place/{adress}")

adressChecker()
