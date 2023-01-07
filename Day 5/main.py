import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to PyPassword Generator!")
letters_chosen = int(input("How many letters you want in your password?\n"))
symbols_chosen = int(input("How many symbols you want? \n"))
numbers_chosen = int(input("How many numbers you want? \n"))
# Easy level without shuffling the password
password = ""
#for letter in range(0, letters_chosen):
#    password = password + random.choice(letters)
#for number in range(0, numbers_chosen):
#    password = password + random.choice(numbers)
#for symbol in range(0, symbols_chosen):
#    password = password + random.choice(symbols)
#print(password)

# Hard level password shuffle
password_list = []
for letter in range(0, letters_chosen):
    password_list.append(random.choice(letters))
for symbol in range(0, symbols_chosen):
    password_list.append(random.choice(symbols))
for number in range(0, numbers_chosen):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)