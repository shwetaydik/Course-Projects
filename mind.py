# Create two variables; 'last_1' and 'last_2' with 0 as their initial values.
from gettext import install


last_1 = 0
last_2 = 0

import numpy as np
import random

inputs = np.zeros(shape=(2, 2, 2), dtype=int)

# Create the 'update_inputs()' function.
def update_inputs(current):
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1 
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0 
    inputs[last_2][last_1][0] = current
 
  last_2 = last_1 
  last_1 = current
  
# Create the 'prediction()' function which returns the predicted value.
def prediction():
  if inputs[last_2][last_1][1] == 1: 
    predict = inputs[last_2][last_1][0]    
  else:
    predict = random.randint(0, 1)  
  return predict

# Student Action: Create the 'update_scores()' function to keep the scores for both the computer and the player. It should not return anything.
scores = [0, 0] # [computer_score, player_score]

def update_scores(predicted, player_input):
  if predicted == player_input:
    scores[0] =  scores[0] + 1
    print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1]) # The '\n' is called a newline character. It adds an empty newline.
               
  else:
    scores[1] = scores[1] + 1
    print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1])
  
# Student Action: Create the 'reset()' function which resets the values of the 'inputs' items to 0.
def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k] = 0

  for i in range(len(scores)):
    scores[i] = 0    
    
# Student Action: Put all the functions and variables of the Mind Reader game algorithm here.
import random
import numpy as np

inputs = np.zeros(shape=(2, 2, 2), dtype=int) 

last_1 = 0
last_2 = 0

scores = [0, 0] # [computer_score, player_score]

def update_inputs(current):
  global last_1, last_2
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1 
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0 
    inputs[last_2][last_1][0] = current
  
  last_2 = last_1 # last_1 becomes last_2 
  last_1 = current # current becomes last_1, i.e., current -> last_1 -> last_2 
    
def prediction():
  if inputs[last_2][last_1][1] == 1: 
    predict = inputs[last_2][last_1][0]    
  else:
    predict = random.randint(0, 1)  
  return predict

def update_scores(predicted, player_input):  
  if predicted == player_input:
    scores[0] = scores[0] + 1
    print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1]) 
        
  else:
    scores[1] = scores[1] + 1
    print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1]) 

def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k] = 0
  
  for i in range(2):
    scores[i] = 0   
    
# Student Action: Create the 'gameplay()' function.
def gameplay():
  reset()
  print(inputs) # To verify whether the 'reset()' function, resets the 'inputs' and 'scores' values or not print their values.
  print(scores)
  valid_entries = ['0', '1']
  while True:
    predicted = prediction()
    player_input = input("\nEnter either 1 or 0: ")
    
    while player_input not in valid_entries:
      print("\nInvalid Input!")
      player_input = input("Please enter either 1 or 0: ")
    
    player_input = int(player_input)
    update_inputs(player_input)
    update_scores(predicted, player_input)
        
    if scores[0] == 20:
      print("\nBad Luck, Computer Wins!\n")
      break
        
    elif scores[1] == 20:
      print("\nCongrats, You Won!\n")
      break
  
# Student Action: Run the game by executing the 'gameplay()' function.
gameplay()