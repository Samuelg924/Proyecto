from constants import *
from models import *

#first,define pokemon with its stats
pokemon1 = Pokemon("lucario",100,"struggle","steel")
pokemon2 = Pokemon("charizard",100,"fire","flying")
pokemon1.current_hp = 70
pokemon2.curretn_hp = 78


#stats
pokemon1.stats = {
    HP: 70,
    ATTACK: 145,
    DEFENSE: 88,
    SPATTACK: 150,
    SPDEFENSE: 70,
    SPEED: 112,
    }


pokemon2.stats = {
    HP: 78,
    ATTACK: 95,
    DEFENSE: 80,
    SPATTACK: 110,
    SPDEFENSE: 85,
    SPEED: 100,
    }

#Attacks
pokemon1.attacks = [Attack("Dark Pulse","normal","physical",15,80,100)]

