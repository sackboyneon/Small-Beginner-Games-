import random
import string

uppercase = ["F", "E", "R", "N", "A", "N", "D", "O"]
lowercase = ["f", "e", "r", "n", "a", "n", "d", "o"]
signs = ["!", "$", "&", "%"]

bag = uppercase + lowercase + signs

lenght = 5
password = ""

for x in range(lenght):
    password+=random.choice(bag)

print("Your new password is: ", password)
print(f"Your password lenght is: {password}")



