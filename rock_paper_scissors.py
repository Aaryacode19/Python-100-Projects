#I dont think i need to explain this to you, you already know. Give it a try, i also added some ascii art to make it cool n fun.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to the Rock, Paper, Scissors game!")
import random
user = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user == 0:
  print(rock,"Rock")
elif user == 1:
    print(paper,"Paper")
else: #if user == 2
      print(scissors,"Scissors")
#for computer
random_number = random.randint(0, 2)
#print(random_number)
if random_number == 0:
  print(rock,"Rock")
elif random_number == 1:
  print(paper,"Paper")
else: #if user == 2
  print(scissors,"Scissors")
#for the result
if user == 0 and random_number == 2:
  print("user wins")
elif user == 0 and random_number == 1:
  print("user wins")
elif user == 1 and random_number == 0:
  print("Tie Both loss n win")
elif user == 1 and random_number == 1:
  print("Tie Both loss n win")
elif user == 1 and random_number == 2:
  print("user wins")
elif user == 2 and random_number == 0:
  print("Computer wins")
elif user == 2 and random_number == 2:
  print("Tie Both loss n win")
elif user == 0 and random_number == 0:
  print("Tie Both loss n win")
elif user == 2 and random_number == 1:
  print("user wins")



