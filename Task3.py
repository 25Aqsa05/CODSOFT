# Password Generator
import random 
password_len=int(input("Enter the length of the password: "))

alphabet= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="@#$%^&*!"
all_character=alphabet+numbers+symbols

password=""
for i in range(password_len):
    random_index = random.randint(0, len(all_character) - 1)
    password += all_character[random_index]
print(f"Your Password is generated : {password} ")
