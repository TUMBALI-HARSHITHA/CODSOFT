#TASK 3
import random
len_p = int(input("Enter the desired password length: "))
characters = "abcdefghijklmnopqrstuvwxyz0123456789.!@#$€¥¢"
password = ""
for i in range(len_p):
    password += random.choice(characters)
print("Generated Password:", password)