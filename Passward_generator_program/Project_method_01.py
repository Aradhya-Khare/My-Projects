#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Method does not includes shuffling of numbers, letters and symbols example like this "#$50nC"
Password = ""
for i in range (1, nr_letters+1):
    rand = random.choice(letters)
    # print(rand)
    Password = rand + Password
# print(Password)

for i in range (1, nr_symbols+1):
    rand = random.choice(numbers)
    # print(rand)
    Password = rand + Password
# print(Password)

for i in range (1, nr_numbers+1):
    rand = random.choice(symbols)
    # print(rand)
    Password = rand + Password
print(f"The Password is {Password}")

# Method includes shuffling of numbers, letters and symbols example like this "&mE#96"

password = []
for i in range (1,nr_letters+1):
    random_val = random.choice(letters)
    password.append(random_val)
# print(password)

for i in range (1,nr_symbols+1):
    random_val = random.choice(symbols)
    password.append(random_val)
# print(password)

for i in range (1,nr_numbers+1):
    random_val = random.choice(numbers)
    password.append(random_val)
# print(password)

random.shuffle(password)
final_password = ""
for i in password:
    final_password = i + final_password

print(f"The new password is {final_password}")


