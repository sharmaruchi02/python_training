import random
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

name_gen =[rock, paper, scissors]

user_choice = int(input("What do you choose ? 0 for Rock, 1 for Paper, 2 for Scissors : "))
if user_choice >=0 and user_choice < 3 :
  print(name_gen[user_choice])

  com_ran = random.randint(0,2)
  print("Computer Choose :  ",name_gen[com_ran])
 
 
  if (user_choice == 0 and com_ran == 2) or (user_choice == 2 and       com_ran == 1) or (user_choice == 1 and com_ran == 0):
    print("You Win")
  elif user_choice == com_ran:
    print("Its Draw")
  else:
    print("You Loss")
else:
  print("Wrong Choice")