#TASK 3
import random
passlen = int(input("Enter the password length:"))
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/"
password = ""
for i in range(passlen):
    password += random.choice(characters)
print("Generated Password:", password)