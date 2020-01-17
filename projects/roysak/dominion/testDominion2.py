# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 4:05 AM

@author: Saket Roy
"""
import testUtility
import random


def bug(box):
    """
    The box object is a key-value pair object
    that relates Card Names to Card Objects. The
    following bug randomly assigns to each Card Name
    a random Card Object.
    """

    cardObjects = list(box.values())
    buggyBox = {}
    for card in box:    
        buggyBox[card] = cardObjects[random.randint(0, len(cardObjects)-1)]

    return buggyBox

def main():
    #Set player names
    player_names = ["*Annie","*Ben","*Carla"]

    #number of Curses and Victory cards
    nV = testUtility.get_nV(player_names)
    nC = testUtility.get_nC(player_names)

    #Define box
    box = testUtility.getBoxes(nV)
    box = bug(box)

    #Get Supply order
    supply_order = testUtility.getSupplyOrder()

    #Get Supply
    supply = testUtility.getSupply(box, player_names, nV, nC)

    #Get players for the game
    players = testUtility.getPlayers(player_names)
    
    
    testUtility.play(supply, supply_order, players)

if __name__ == "__main__":
    main()