import time
import random
import os

global wins, losses
wins, losses = 0, 0
time_start = time.time()

def populate_doors(): # put a car behind one door
	door = [False, False, False]
	door[random.randint(0,2)] = True
	return door

def result():
    print(f"Wins : {wins} Losses : {losses} \
            \nWin rate : {(wins/(wins+losses)):.2f} \
            \nElapsed time : {(time.time()-time_start):.2f}")

def monty():
    global wins, losses
    doors = populate_doors()
    first_choice = random.randint(0,2) # 문을 골라버렸~
    for x in range(3): # 내가 고른 문이 아닌 것 중에, 염소가 든 문
        if not doors[x] and x != first_choice: break
    
    if doors[first_choice]: losses += 1
    else: wins += 1
