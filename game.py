#imports
import os, time, sys, random
from time import sleep
from random import choice, randint

n = ""

def extTxt(txt):
  for char in txt:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.015)


#players "country"
class Place:
  def __init__(self, name, wood, food, stone, coal, money, trees, stoneMines, coalMines, rivers, boats, civilianTents, civilians, armyTents, soldiers, market, bank):
    self.name = name
    self.wood = wood
    self.food = food
    self.stone = stone
    self.coal = coal
    self.money = money
    self.trees = trees
    self.stoneMines = stoneMines
    self.coalMines = coalMines
    self.rivers = rivers
    self.boats = boats
    self.civilianTents = civilianTents
    self.civilians = civilians
    self.armyTents = armyTents
    self.soldiers = soldiers
    self.market = market
    self.bank = bank


#trees
class Tree:
  def __init__(self, cost, dropRate, dropWorth):
    self.cost = cost
    self.dropRate = dropRate
    self.dropWorth = dropWorth

#mines
class Mine:
  def __init__(self, cost, dropRate, dropWorth, dropName):
    self.cost = cost
    self.dropRate = dropRate
    self.dropWorth = dropWorth
    self.dropName = dropName

#rivers
class River:
  def __init__(self, cost, bCost, dropRate, dropWorth):
    self.cost = cost
    self.bCost = bCost
    self.dropRate = dropRate
    self.dropWorth = dropWorth

#civilian tent
class Civil:
  def __init__(self, maxPop, civilCost, cost, woodCost):
    self.maxPop = maxPop
    self.civilCost = civilCost
    self.cost = cost
    self.woodCost = woodCost

#army tent
class Army:
  def __init__(self, maxSize, soldierCost, cost, woodCost, stoneCost, coalCost):
    self.maxSize = maxSize
    self.soldierCost = soldierCost
    self.cost = cost
    self.woodCost = woodCost
    self.stoneCost = stoneCost
    self.coalCost = coalCost

#Market
class Market:
  def __init__(self, lvl, workers, maxWorkers, cost, woodCost, stoneCost, coalCost):
    self.lvl = lvl
    self.workers = workers
    self.maxWorkers = maxWorkers
    self.cost = cost
    self.woodCost = woodCost
    self.stoneCost = stoneCost
    self.coalCost = coalCost
    
class Bank:
  def __init__(self, storedMoney, cost):
    self.storedMoney = storedMoney
    self.cost = cost

class Weapon:
  def __init__(self, name, cost, damage, type_, marketLvl):
    self.name = name
    self.cost = cost
    self.damage = damage
    self.type_ = type_
    self.marketLvl = marketLvl


#maps
map1 = r"""  
    ________
   /       /
  |__      \
     |      \
     |____--/"""

map2 = r"""
    _____
  /      \
 /        |
 |        \
 \         |
  |___     --\
      \______/
"""

map3 = r"""
      ___-__
 __-_/      \ \___
/              \
|              \
|             \_
\_-___-___      ) 
          \__-_/
"""

map4 = r"""
  _-^-__________
 (      ______  \
 (_____/      |__)"""

map5 = r""" 
   / \       / \
  /   \     /   \
 /     \/\/      \
/                 \
|  /\   _ _   /\  |
\_/  \__| |__/  \_/""" 

maps = [map1, map2, map3, map4, map5]


#things made by classes
place = Place("", 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0)
enemy1 = Place("The Republics of Barcondonia", 100, 100, 100, 100, 1000, 10, 10, 10, 1, 10, 5, 50, 1, 10, 0, 0)
enemy2 = Place("The Federation of Sovereign States", 200, 200, 200, 200, 2000, 20, 20, 20, 1, 20, 10, 100, 1, 50, 0, 0)
enemy3 = Place("The United Nations of the Greater Northern Distric", 300, 300, 300, 300, 3000, 30, 30, 30, 1, 30, 15, 150, 1, 100, 0, 0)
devPlace = Place("The Republic of Developers(Hard)",300, 200, 200, 200, 160000, 100, 200, 200, 1, 20, 10, 20, 10, 180000, 0, 0)
#name, wood, food, stone, coal, money, trees, stoneMines, coalMines, rivers, boats, civilianTents, civilians, armyTents, soldiers, market, bank
enemyChance = randint(1, 9)
wins = 0
enemyPos = [enemy1, enemy2, enemy3]
placemap = maps[random.randint(0, len(maps) - 1)]

tree1 = Tree(100, 5, 25)
#cost, dropRate, dropWorth
mineStone = Mine(200, 3, 50, "Stone")
mineCoal = Mine(1000, 2, 75, "Coal")
#cost, dropRate, dropWorth, dropName
river1 = River(500, 50, 4, 10)
#cost, bCost, dropRate, dropWorth

civilTent = Civil(1, 25, 100, 20)
#maxPop, civilCost, cost, woodCost
armyTent = Army(100, 100, 1000, 50, 20, 5)
#maxSize, soldierCost, cost, woodCost, stoneCost, coalCost

market = Market(1, 0, 10, 100, 20, 20, 5)
#lvl, workers, maxWorkers, cost, woodCost, stoneCost, coalCost

bank = Bank(0, 5000)
#storedMoney

rifle = Weapon("Rifle", 50, 2, "Gun", 1)
dagger = Weapon("Dagger", 75, False,"Knife", 1)

#game
def homeScreen():
   print("""
  _____                  _ _      
 |  __ \                | | |     
 | |  | | ___   ___   __| | | ___ 
 | |  | |/ _ \ / _ \ / _` | |/ _ \      
 | |__| | (_) | (_) | (_| | |  __/                                
 |_____/ \___/_\___/ \__,_|_|\___|                
 \ \        / /                             ---------------+---------------
  \ \  /\  / /_ _ _ __ ___                            __ /^^[___
   \ \/  \/ / _` | '__/ __|                         /|^+----+   |#___________//  
    \  /\  / (_| | |  \__ \                        ( -+ |____|    ___________      
     \/  \/ \__,_|_|  |___/                          ==_________--'          \
      """)
   print('Hello there welcome to doodlewars\n(1) Play\n(2) Credits')
   CreditGoer = input('\n>>> ')
   if CreditGoer == '1':
      os.system("clear")
      name = input("What is your place called?\n\n>>> ")
      place.name = name
      os.system('clear')
      mainMenu()
   if CreditGoer == '2':
     os.system('clear')
     credits()


def credits():
     print('tankerguy1917\nFunky(youtube.com/c/TheRealDunk)\nIntelDS\nFloCal35\nIntellectualGuy\n(1) Go Back')
     GoBackToHome = input('\n>>> ')
     if GoBackToHome == '1':
       os.system('clear')
       homeScreen()





def mainMenu():
  print(f"""
  place map
  {placemap}
  Place name: {place.name}
  Money: ${place.money}

  Civilians: {place.civilians}/{civilTent.maxPop}
  Soldiers: {place.soldiers}/{armyTent.maxSize}

  Trees: {place.trees}
  Stone Mines: {place.stoneMines}
  Coal Mines: {place.coalMines}
  Rivers: {place.rivers}
  Boats: {place.boats}

  Wood: {place.wood}
  Stone: {place.stone}
  Coal: {place.coal}
  Food: {place.food}

  (1) Buy Resources
  (2) Sell Resources
  (3) Collect Resources
  (4) Check Buildings (not finished)
  (5) Fight a War
  (6) Pet A Dog
  
  What do you want to do?
  """)
  toDo = input("\n>>> ")
  if toDo == "1":
    os.system("clear")
    buyMenu()
  elif toDo == "2":
    os.system("clear")
    sellMenu()
  elif toDo == "3":
    os.system("clear")
    cResources()
  elif toDo == "4":
    os.system("clear")
    cBuildings()
  elif toDo == "5":
    os.system("clear")
    war()
  elif toDo == '6':
    os.system('clear')
    dog()
  else:
    os.system("clear")
    mainMenu()


def buyMenu():
  if place.money >= 50:
    print(f"""
    Money: {place.money}
    Wood: {place.wood}
    Stone: {place.stone}
    Coal: {place.coal}

    (1) Tree: ${tree1.cost}
    (2) Stone Mine: ${mineStone.cost}
    (3) Coal Mine: ${mineCoal.cost}

    (4) River: ${river1.cost}
    (5) Boat: ${river1.bCost}

    (6) Civilian Tent: ${civilTent.cost} and {civilTent.woodCost} wood
    (7) Civilian: ${civilTent.civilCost}
    (8) Army Tent: ${armyTent.cost} and {armyTent.woodCost} wood, {armyTent.stoneCost} stone, and {armyTent.coalCost} coal
    (9) Soldier: ${armyTent.soldierCost}
    (10) Market: ${market.cost} and {market.woodCost} wood, {market.stoneCost} stone, and {market.coalCost} coal
    (11) Bank: ${bank.cost}
    (12) Go Back

    What do you want to buy?
    
    """)
    whatBuy = input("\n>>> ")

    if whatBuy == "1":
      if place.money >= tree1.cost:
        place.trees += 1
        place.money -= tree1.cost
        extTxt("You bought a Tree.")
        sleep(1)
        os.system("clear")
        buyMenu()
      else:
        extTxt("Sorry, you can't afford that.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "2":
      if place.money >= mineStone.cost:
        place.stoneMines += 1
        place.money -= mineStone.cost
        extTxt("You bought a Stone Mine.")
        sleep(1)
        os.system("clear")
        buyMenu()
      else:
        extTxt("Sorry, you can't afford that.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "3":
      if place.money >= mineCoal.cost:
        place.coalMines += 1
        place.money -= mineCoal.cost
        extTxt("You bought a Coal Mine.")
        sleep(1)
        os.system("clear")
        buyMenu()
      else:
        extTxt("Sorry, you can't afford that.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "4":
      if place.rivers == 0:
        if place.money >= river1.cost:
          place.rivers += 1
          place.money -= river1.cost
          extTxt("You bought a River.")
          sleep(1)
          os.system("clear")
          buyMenu()
        else:
          extTxt("Sorry, you can't afford that.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("You already have a river.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "5":
      if place.rivers >= 1:
        if place.money >= river1.bCost:
          place.boats += 1
          place.money -= river1.bCost
          extTxt("You bought a Boat.")
          sleep(1)
          os.system("clear")
          buyMenu()
        else:
          extTxt("Sorry, you can't afford that.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("You need a River to buy Boats.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "6":
      if place.money >= civilTent.cost:
        if place.wood >= civilTent.woodCost:
          place.civilianTents += 1
          civilTent.maxPop += 10
          place.money -= civilTent.cost
          place.wood -= civilTent.woodCost
          extTxt("You bought a Civilian Tent")
          sleep(1)
          os.system("clear")
          buyMenu()
        else:
          extTxt("Sorry, you don't have enough wood to buy that.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("Sorry, you can't afford that")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "7":
      if place.civilianTents >= 1:
        if place.civilians < civilTent.maxPop:
          if place.money >= civilTent.civilCost:
            place.civilians += 1
            place.money -= civilTent.civilCost
            extTxt(f"A Civilian immigrated to {place.name}")
            sleep(1)
            os.system("clear")
            buyMenu()
          else:
            extTxt("Sorry, you can't afford to immigrate any Civilians.")
            sleep(1)
            os.system("clear")
            buyMenu()
        else:
          extTxt("Sorry, you population is at its maximun.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("Sorry, you need a Civilian Tent before Civilians can immigrate to your place.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "8":
      if place.money >= armyTent.cost:
        if place.wood >= armyTent.woodCost:
          if place.stone >= armyTent.stoneCost:
            if place.coal >= armyTent.coalCost:
              place.armyTents += 1
              armyTent.maxSize += 10
              place.money -= armyTent.cost
              place.wood -= armyTent.woodCost
              place.stone -= armyTent.stoneCost
              place.coal -= armyTent.coalCost
              extTxt("You bought and Army Tent")
              sleep(1)
              os.system("clear")
              buyMenu()
            else:
              extTxt("Sorry, you don't have enough coal to buy that.")
              sleep(1)
              os.system("clear")
              buyMenu()
          else:
            extTxt("Sorry, you don't have enough stone to buy that.")
            sleep(1)
            os.system("clear")
            buyMenu()
        else:
          extTxt("Sorry, you don't have enough wood to buy that.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("Sorry, you can't afford that.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "9":
      if place.armyTents >= 1:
        if place.soldiers < armyTent.maxsize:
          if place.money >= armyTent.soldierCost:
            place.soldier += 1
            place.money -= armyTent.soldierCost
            extTxt(f"A Soldier was recruited to protect {place.name}.")
            sleep(1)
            os.system("clear")
            buyMenu()
          else:
            extTxt("Sorry, you do not have enough money to equip a Soldier.")
            sleep(1)
            os.system("clear")
            buyMenu()
        else:
          extTxt("Sorry, you can't fit any more soldiers into your ranks.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("Sorry, you need an Army Tent before you can recruit Soldiers.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "10":
      if place.market == 0:
        if place.money >= market.cost:
          if place.wood >= market.woodCost:
            if place.stone >= market.stoneCost:
              if place.coal >= market.coalCost:
                extTxt("You bought a Market.")
                place.market += 1
                place.money -= market.cost
                place.wood -= market.woodCost
                place.stone -= market.stoneCost
                place.coal -= market.coalCost
                sleep(1)
                os.system("clear")
                buyMenu()
              else:
                extTxt("You don't have enough Coal to buy that.")
                sleep(1)
                os.system("clear")
                buyMenu()
            else:
              extTxt("You don't have enough Stone to buy that.")
              sleep(1)
              os.system("clear")
              buyMenu()
          else:
            extTxt("You don't have enough Wood to buy that.")
            sleep(1)
            os.system("clear")
            buyMenu()
        else:
          extTxt("You don't have enough money to buy that.")
          sleep(1)
          os.system("clear")
          buyMenu()
      else:
        extTxt("You already have a Market")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "11":
      if place.money >= bank.cost:
        extTxt("You bought a Bank")
        place.bank += 1
        place.money -= bank.cost
        sleep(1)
        os.system("clear")
        buyMenu()
      else:
        extTxt("You don't have enough money to buy a Bank.")
        sleep(1)
        os.system("clear")
        buyMenu()

    elif whatBuy == "12":
      os.system("clear")
      mainMenu()

    else:
      os.system("clear")
      buyMenu()
  else:
    extTxt("You can't afford anything.")
    sleep(1)
    os.system("clear")
    mainMenu()



def sellMenu():
  print(f"""
  Wood: {place.wood}
  Stone: {place.stone}
  Coal: {place.coal}
  Food: {place.food}

  (1) Wood: ${tree1.dropWorth}
  (2) Stone: ${mineStone.dropWorth}
  (3) Coal: ${mineCoal.dropWorth}
  (4) Food: ${river1.dropWorth}
  (5) Sell All
  (6) Go Back

  What do you want to sell?
  """)
  whatSell = input("\n>>> ")

  if whatSell == "1":
    extTxt(f"How much do you want to sell. 1 to {place.wood}.")
    sellWood = int(input("\n>>> "))
    if sellWood <= place.wood:
      place.money += tree1.dropWorth * sellWood
      place.wood -= sellWood
      extTxt(f"You got ${tree1.dropWorth * sellWood}.")
      sleep(1)
      os.system("clear")
      sellMenu()
    else:
      extTxt("You don't have that much Wood to sell.")
      sleep(1)
      os.system("clear")
      sellMenu()

  elif whatSell == "2":
    extTxt(f"How much do you want to sell. 1 to {place.stone}.")
    sellStone = int(input("\n>>> "))
    if sellStone <= place.stone:
      place.money += mineStone.dropWorth * sellStone
      place.stone -= sellStone
      extTxt(f"You got ${mineStone.dropWorth * sellStone}.")
      sleep(1)
      os.system("clear")
      sellMenu()
    else:
      extTxt("You don't have that much Stone to sell.")
      sleep(1)
      os.system("clear")
      sellMenu()

  elif whatSell == "3":
    extTxt(f"How much do you want to sell. 1 to {place.coal}.")
    sellCoal = int(input("\n>>> "))
    if sellCoal <= place.coal:
      place.money += mineCoal.dropWorth * sellCoal
      place.coal -= sellCoal
      extTxt(f"You got ${mineCoal.dropWorth * sellCoal}.")
      sleep(1)
      os.system("clear")
      sellMenu()
    else:
      extTxt("You don't have that much wood to sell.")
      sleep(1)
      os.system("clear")
      sellMenu()

  elif whatSell == "4":    
    extTxt(f"How much do you want to sell. 1 to {place.food}.")
    sellFood = int(input("\n>>> "))
    if sellFood <= place.food:
      place.money += river1.dropWorth * sellFood
      place.food -= sellFood
      extTxt(f"You got ${river1.dropWorth * sellFood}.")
      sleep(1)
      os.system("clear")
      sellMenu()
    else:
      extTxt("You don't have that much wood to sell.")
      sleep(1)
      os.system("clear")
      sellMenu()

    
  elif whatSell == "5":
    print(f"""
    You sold all of your resources and got ${(place.wood * tree1.dropWorth) + (place.stone * mineStone.dropWorth) + (place.coal * mineCoal.dropWorth) + (place.food * river1.dropWorth)}
    """)
    place.money += (place.wood * tree1.dropWorth) + (place.stone * mineStone.dropWorth) + (place.coal * mineCoal.dropWorth) + (place.food * river1.dropWorth)
    place.wood -= place.wood
    place.stone -= place.stone
    place.coal -= place.coal
    place.food -= place.food
    sleep(2)
    os.system("clear")
    mainMenu()
  
  elif whatSell == "6":
    os.system("clear")
    mainMenu()

  else:
    os.system("clear")
    sellMenu()


def cResources():
  print(f"""
  You collected
  {tree1.dropRate * place.trees} wood
  {mineStone.dropRate * place.stoneMines} stone
  {mineCoal.dropRate * place.coalMines} coal
  {river1.dropRate * place.boats} food

  Press enter to continue
  """)
  ranvar = input("\n>>> ")
  if ranvar == "":
    place.wood += tree1.dropRate * place.trees
    place.stone += mineStone.dropRate * place.stoneMines
    place.coal += mineCoal.dropRate * place.coalMines
    place.food += river1.dropRate * place.boats
    #for x in market.lvl:
      #x += 50
      #for x in  market.workers :
        #place.money += x
    natural_disaster()
  else:
    place.wood += tree1.dropRate * place.trees
    place.stone += mineStone.dropRate * place.stoneMines
    place.coal += mineCoal.dropRate * place.coalMines
    place.food += river1.dropRate * place.boats
    natural_disaster()



def war():
  print(f"""
  (1) {enemy1.name}
  (2) {enemy2.name}
  (3) {enemy3.name}
  (4) {devPlace.name}
  (5) Back

  Who do you want to go to war with?
  """)
  fight = input("\n>>> ")

  if fight == "1":
    os.system("clear")
    extTxt("Determining the winner.")
    sleep(2)
    ab = enemy1.soldiers
    an = place.soldiers
    enemy1.soldiers -= an
    place.soldiers -= ab
    if place.soldiers > enemy1.soldiers:
      print(f"""
      You won!
      You got ${round((enemy1.money / 3),0)} for winning.
      """)
      place.money += enemy1.money / 3
      round(place.money,0)
      sleep(2)
      enemy1.soldiers += ab
      mainMenu()
    elif place.soldiers < enemy1.soldiers:
      print(f"""
      You lost
      You lost ${round((place.money / 3),0)}
      """)
      place.money -= place.money / 3
      round(place.money,0)
      sleep(2)
      os.system("clear")
      enemy1.soldiers += ab
      mainMenu()

  elif fight == "2":
    os.system("clear")
    extTxt("Determining the winner.")
    sleep(2)
    bb = enemy2.soldiers
    bn = place.soldiers
    enemy2.soldiers -= bn
    place.soldiers -= bb
    if place.soldiers > enemy2.soldiers:
      print(f"""
      You won!
      You got ${round((enemy2.money / 3),0)} for winning.
      """)
      place.money += enemy2.money / 3
      round(place.money,0)
      sleep(2)
      os.system("clear")
      enemy2.soldiers += bn
      mainMenu()
    elif place.soldiers < enemy2.soldiers:
      print(f"""
      You lost.
      You lost ${round((place.money / 3),0)}
      """)
      place.money -= place.money / 3
      round(place.money,0)
      sleep(2)
      os.system("clear")
      enemy2.soldiers += bn
      mainMenu()
    
  elif fight == "3":
    os.system("clear")
    extTxt("Determining the winner.")
    sleep(2)
    cb = enemy3.soldiers
    cn = place.soldiers
    enemy3.soldiers -= cn
    place.soldiers -= cb
    if place.soldiers > enemy3.soldiers:
      print(f"""
      You won!
      You got ${round((enemy3.money / 3),0)}
      """)
      place.money += enemy3.money / 3
      round(place.money)
      sleep(2)
      os.system("clear")
      enemy3.soldiers += cb
      mainMenu()
    elif place.soldiers < enemy3.soldiers:
      print(f"""
      You lost.
      You lost ${round((place.money / 3),0)}
      """)
      place.money -= place.money / 3
      round(place.money,0)
      sleep(2)
      os.system("clear")
      enemy3.soldiers += cb
      mainMenu()

  elif fight == "4":
    os.system("clear")
    extTxt("You are fighting the game devs, may the gods have mercy on your souls.\n\n")
    extTxt("Determining the winner.")
    sleep(2)
    db = devPlace.soldiers
    dn = place.soldiers
    devPlace.soldiers -= dn
    place.soldiers -= db
    if place.soldiers > devPlace.soldiers:
      print(f"""
      You won! You managed to beat the game devs.
      It probably won't happen again
      You got ${round(devPlace.money,0)}
      """)
      place.money += devPlace.money
      round(place.money,0)
      sleep(2)
      os.system("clear")
      devPlace.soldiers += db
      mainMenu()
    elif place.soldiers < devPlace.soldiers:
      print(f"""
      You lost.
      The game devs were just to strong to beat
      You lost ${round((place.money / 3),0)}
      """)
      place.money -= place.money / 3
      round(place.money,0)
      sleep(2)
      os.system("clear")
      devPlace.sodliers += db
      mainMenu()

    elif fight == '5':
      os.system('clear')
  else:
     os.system('clear')
     mainMenu()

def natural_disaster():
      natDisChance = random.randint(1,23)
      if natDisChance == 1:
        place.money *= .85
        round(place.money,0)
        print(f"\nBecause of a Hurricane {place.name} now has ${place.money}.")
        sleep(2)
        os.system("clear")
        mainMenu()
      elif natDisChance in [2, 3]:
        place.money *= 0.10
        round(place.money,0)
        extTxt(f"Because of a Tornado {place.name} now has ${place.money}." )
        sleep(2)
        os.system("clear")
        mainMenu()
      elif natDisChance in [4, 5]:
        place.money *= 0.25
        round(place.money,0)
        extTxt(f"Because of an Earthquake {place.name} now has ${place.money}.")
        sleep(2)
        os.system("clear")
        mainMenu()
      elif natDisChance in [6, 7]:
        place.money *= .30
        round(place.money,0)
        extTxt(f"Because of a Flood {place.name} now has S{place.money}.")
        sleep(2)
        os.system("clear")
        mainMenu()
      elif natDisChance == 8:
        place.money *= 0.50
        round(place.money,0)
        place.civilians *= 0.50
        if place.soldiers < 1:
          place.soldeirs += 1
        round(place.civilians,0)
        place.soldiers *= 0.50
        round(place.soldiers,0)
        extTxt(f"Because of a Tsunami, {place.name} now has ${place.money}, {place.civilians} people, and the army size is now {place.soldiers}.")
        sleep(5)
        os.system("clear")
        mainMenu()
      else:
        os.system("clear")
        mainMenu()
  

def dog():
  print('''
   |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|\n\n(1) Back
  ''')
  place.money += 1
  dogback = input('\n>>> ')
  if dogback == '1':
    os.system('clear')
    mainMenu()
  elif dogback == '3':
    place.money += 1000
    place.soldiers += 10
    os.system('clear')
    mainMenu()
  else:
    os.system('clear')
    mainMenu() 


def Assign_Market_Workers() :
  Assign_Worker = input("Would you like to assign a civilian to become a worker in the market? Y/N")
  if Assign_Worker.lower() in ["yes" "y"] :
    if place.civilians >= 1:
      market.workers += 1
      os.system("clear")
      mainMenu()
  elif Assign_Worker.lower() in ["n", "no"]:
    os.system("clear")
    mainMenu()
  else:
    os.system("clear")
    Assign_Market_Workers()
  
  
def sabotage() :
  ask_sabotage = input("Would you like to sabotage your alliance? \n Warning:This will decrease your chance of getting another alliance.")
  if ask_sabotage.lower is ["yes" "y"]:
    war()
  else:
    pass

def Form_Alliances() :
  Ask_For_Alliance = input("Would you like to form an alliance?")
  if Ask_For_Alliance.lower is ["yes" or "y"] :
    Alliance = input(f"Who would you like to form an alliance with?\n(1) for {enemy1.name}\n(2) for {enemy2.name}\n(3) for {enemy3.name}.")
    randAlliance = random.randint(1,2)
    if Alliance == 1:
      if randAlliance == 1 :
        extTxt(f"{enemy1.name} has accepted your alliance.")
        Player_Alliance = [enemy1.name]
      else:
        extTxt(f"The {enemy1.name} has rejected your alliance.")
    if Alliance == 2:
      if randAlliance == 1:
        extTxt(f"{enemy2.name} has accepted your alliance.")
        Player_Alliance = [enemy2.name]
      else:
        extTxt(f"The {enemy2.name} has rejected your alliance.")
    if Alliance == 3:
      if randAlliance == 1:
        extTxt(f"{enemy3.name} has excepted your alliance.")
        Player_Alliance = [enemy3.name]
      else:
        extTxt(f"{enemy3.name} has rejected your alliance")
  else:
    pass

def bankStore():
  if place.bank >= 1:
    extTxt("Do you want to take out money or store money?\n(1) Store\n(2) Take\n(3) Borrow\n(4) Go Back")
    bankDecide = input()
    if bankDecide == "1":
      extTxt(f"How much money would you like to store.\n$1 to ${place.money}")
      storeMoney = int(input("\n>>> "))
      extTxt(f"You stored ${storeMoney}")
      place.money -= storeMoney
      bank.storedMoney += storeMoney
      sleep(1)
      os.system("clear")
      mainMenu()
    elif bankDecide == "2":
      extTxt(f"How much money do you want to take out? $1 to ${bank.storedMoney}")
      takeMoney = int(input("\n>>> "))
      extTxt(f"You took ${takeMoney}")
      place.money += takeMoney
      bank.storedMoney -= takeMoney
      sleep(1)
      os.system("clear")
      mainMenu()
    elif bankDecide == "3" :
      extTxt("How much money would you like to borrow from the bank, remember you have to pay 10% interest")
      borrowMoney = int(input("\n >>>"))
      place.money += borrowMoney
      debt = borrowMoney * 1.1
      sleep(1)
      os.system("clear")
      mainMenu()
    elif bankDecide == "4":
      os.system("clear")
      mainMenu()
    else:
      os.system("clear")
      bankStore

def cBuildings():
  print(f"""
  (1) Market lv.{market.lvl}, workers: {market.workers}
  (2) Bank stored money: {bank.storedMoney}

  What do you want to look at
  """)
  pickBuilding = input("\n>>> ")
  if pickBuilding == "1":
    os.system("clear")
    Assign_Market_Workers()
  elif pickBuilding == "2":
    os.system("clear")
    bankStore()
  else:
    os.system("clear")
    cBuildings()
  

homeScreen()
