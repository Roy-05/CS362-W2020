# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 4:05 AM

@author: Saket Roy
"""
import testUtility
import random


#Set player names
player_names = ["Annie","*Ben","*Carla"]

#number of Curses and Victory cards
nV = testUtility.get_nV(player_names)
nC = testUtility.get_nC(player_names)

#Define box
box = testUtility.getBoxes(nV)

#Get Supply order
supply_order = testUtility.getSupplyOrder()


#Get Supply
supply = testUtility.getSupply(box, player_names, nV, nC)
supply = bug(supply)


#Get players for the game
players = testUtility.getPlayers(player_names)

testUtility.play(supply, supply_order, players)



def bug(supply):
    """
    The following bug changes the quantity of card objects 
    that is related to each card name in the supply by a factor 
    of 0-20. It further changes the quantity of Silver and Gold
    cards in the game to 0, resulting in the players to only have 
    Copper to play the game with.
    """ 
    buggySupply = {}

    for card in supply:
        buggySupply[card] = supply[card]*random.randint(0,20)
    
    cardsToRemove = ["Silver", "Gold"]
    for card in buggySupply:
        if card in cardsToRemove:
            buggySupply[card] *= 0

    return buggySupply