# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 4:35 AM

@author: Saket Roy
"""

import Dominion
import random
from collections import defaultdict


def get_nV(player_names):
    """
    Returns the number of Victory Cards in play.
    Takes player_names as argument that represents
    an array of the names of the players in the game
    """

    if len(player_names)>2:
        nV=12
    else:
        nV=8
    
    return nV


def get_nC(player_names):
    """
    Returns the number of Curse Cards in play
    takes player_names as argument that represents
    an array of the names of the players in the game
    """

    nC = -10 + 10 * len(player_names)

    return nC


def getBoxes(nV): 
    """
    Returns a box object
    takes nV as an argument that represents 
    the number of Victory Cards in play
    """

    #Create a box object
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10

    return box


def getSupplyOrder():
    """
    Returns the supply order for the game
    """

    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

    return supply_order


def getSupply(box, player_names, nV, nC):
    """
    Returns a randomized supply for the current game. 
    Takes in arguments the current box object, supply order, 
    and the number of Victory Cards and Curses in play.
    """

    #Pick 10 cards from box to be in the supply.
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list,[(k,box[k]) for k in random10])


    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC

    return supply


def getPlayers(player_names):
    """
    Returns the Player objects constructed from Dominion.py
    """

    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    
    return players


def play(supply, supply_order, players):
    """
    Implement play logic to run the game
    """

    #initialize the trash
    trash = []

    #Play the game
    turn  = 0
    while not Dominion.gameover(supply):
        turn += 1    
        print("\r")    
        for value in supply_order:
            print (value)
            for stack in supply_order[value]:
                if stack in supply:
                    print (stack, len(supply[stack]))
        print("\r")
        for player in players:
            print (player.name,player.calcpoints())
        print ("\rStart of turn " + str(turn))    
        for player in players:
            if not Dominion.gameover(supply):
                print("\r")
                player.turn(players,supply,trash)
                

    #Final score
    dcs=Dominion.cardsummaries(players)
    vp=dcs.loc['VICTORY POINTS']
    vpmax=vp.max()
    winners=[]
    for i in vp.index:
        if vp.loc[i]==vpmax:
            winners.append(i)
    if len(winners)>1:
        winstring= ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0],'wins!'])

    print("\nGAME OVER!!!\n"+winstring+"\n")
    print(dcs)