import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome To Password Generator")

no_letters = int(input("\nHow many letters would you like in your password : "))
no_numbers = int(input("How many numbers you want : "))
no_symbols = int(input("How many symbols you want : "))

new_pass = []

for i in range(1,no_letters+1):
  ran_let = random.choice(letters)
  new_pass +=ran_let

for i in range(1,no_numbers+1):
  ran_num = random.choice(numbers)
  new_pass += ran_num

for i in range(1,no_symbols+1):
  ran_sym = random.choice(symbols)
  new_pass += ran_sym


random.shuffle(new_pass)
  

new_pass1 = ""
for i in new_pass:
  new_pass1 += i

print(f"Your Possible Password will be :  {new_pass1}")  


