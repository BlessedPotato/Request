#Самый умный супергерой

import requests
import json


url = 'https://akabab.github.io/superhero-api/api/all.json'
responce = requests.get(url)

def most_intelligent_hero(name):

    for list_ in responce.json():
        if list_.get('name') == name:
            x = list_['powerstats']
            y = x['intelligence']

            return y

heroes_list = []

heroes_list.append(most_intelligent_hero('Hulk'))
heroes_list.append(most_intelligent_hero('Captain America'))
heroes_list.append(most_intelligent_hero('Thanos'))

print(heroes_list)












