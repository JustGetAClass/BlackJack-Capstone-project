import random
from replit import clear
from art import logo

def deal_card():
  """returns a random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  if computer_score == user_score:
    return "it's a draw"
  elif computer_score == 0:
    return "You Lost, computer has Blackjack"
  elif user_score == 0:
    return "You won with a Blackjack"
  elif user_score > 21:
    return "You lost. you went over"
  elif computer_score > 21:
    return "You won, the computer went over"
  elif user_score > computer_score:
    return "You have the higher score"
  elif computer_score > user_score:
    return "The computer has the higher score"

def blackjack():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, Your score: {user_score}")
    print(f"computer's first card: {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
      is_game_over = True
    else:
      answer = input("Do you want to draw another card? yes or no? ")
      if answer == "yes":
        user_cards.append(deal_card())
      elif answer == "no":
        is_game_over = True
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand is: {user_cards}, your final score: {user_score}")
  print(f"The computer's hand is : {computer_cards}, computer score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of black jack? yes or no? ") == "yes":
  clear()
  blackjack()
