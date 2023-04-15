import string
import requests

with open('key.txt', 'r') as file:
    key = file.read().strip(string.whitespace)

def on():
    requests.get(f'https://maker.ifttt.com/trigger/plugon/json/with/key/{key}')

def off():
    requests.get(f'https://maker.ifttt.com/trigger/plugoff/json/with/key/{key}')