import requests
from pprint import pprint


url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)

all_hero = resp.json()
neme_hero = ['Hulk', 'Captain America', 'Thanos']

def find_smartest(names):
    desired_hero = {}
    for hero in all_hero:
        if hero['name'] in names:
            name = hero['name']
            desired_hero[name] = hero['powerstats']['intelligence']
    smart_hero = (max(desired_hero, key=desired_hero.get))
    return smart_hero
    # for hero in all_hero:
    #     if hero['name'] == smart_hero:
    #         return hero

pprint(find_smartest(neme_hero))