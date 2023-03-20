
import random
import time
from art import logo
from art import zero
from replit import clear
user_cards = []
computer_cards = []
is_game_over = False

def starting_screen():
  print (logo)
  print (zero)
  time.sleep(2)
  print ("Dealing the cards")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  clear()


def deal_card():
  """returns card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards):
  if sum(cards) ==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)



def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score== 0:
    return "Lose, opponent has Blackjack"
  elif user_score ==0:
    return "Win with a Blackjack"
  elif user_score >21:
    return "You went over, you lose"
  elif computer_score > 21:
    return "Opponent went over, you win"
  elif user_score>computer_score:
    return "You have a higher score, you win."
  else:
    return "You lose"
#starting_screen()

game_on=True

while game_on:
  is_game_over=False
  computer_cards.clear()
  user_cards.clear()
  user_score=0
  computer_score=0
  twist=""
  
  for _ in range(2):
 
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  
  while not is_game_over:
    clear()
    twist=""
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f" Your cards: {user_cards}, current score : {user_score}")
    print(f" Computer cards: {computer_cards}, current score : {computer_score}")
    
    if user_score ==0 or computer_score ==0 or user_score >21:
      is_game_over =True
    else:
      while twist!="Y" and twist!="N": 
        twist = input("Twist? Y/N\n")
      if twist=="Y":
        user_cards.append(deal_card())
      else:
        is_game_over=True
  while computer_score!=0 and computer_score <17 or( computer_score<user_score and user_score<22):
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    
  print(compare(user_score, computer_score))
  print("-----------------------------------------------")
  play_again=input("Do you want to play again? Y/N\n")
  if play_again=="Y":
    game_on=True
  else:
    game_on=False
  
 
  
  





print("\nThanks for playing\n")