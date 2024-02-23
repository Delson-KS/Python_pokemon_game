import random
import csv
from functions.Pokedex import Pokemon
def menu():
    trainer_name=input("Welcome to pokemon battle\n 1.You're name: ")
    trainer_pokemon=random.randint(1,9)
    print("You're Pokemon: ",poke_choose(trainer_pokemon))
    opp_pokemon=random.randint(1,9)
    print("Opponent Pokemon's is", poke_choose(opp_pokemon))
    pokemon1=pokemon(trainer_pokemon)
    pokemon2=pokemon(opp_pokemon)
    pokemon1.fight(pokemon2)

def pokemon(id):
    if id == 1:
        pokemon = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})
    if id==2:
        pokemon = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})
    if id == 3:
        pokemon = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK': 8, 'DEFENSE': 12})
    if id==4:
        pokemon = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],
                             {'ATTACK': 4, 'DEFENSE': 2})
    if id==5:
        pokemon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],
                             {'ATTACK': 6, 'DEFENSE': 5})
    if id==6:
        pokemon = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],
                            {'ATTACK': 12, 'DEFENSE': 8})
    if id==7:
        pokemon = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],
                           {'ATTACK': 3, 'DEFENSE': 3})
    if id==8:
        pokemon = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],
                            {'ATTACK': 5, 'DEFENSE': 5})
    if id==9:
        pokemon = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],
                            {'ATTACK': 10, 'DEFENSE': 10})
    return pokemon

def poke_choose(id):
    with open('pokemon.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if int(row['id']) == id:
                return row['name']

