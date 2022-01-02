# Import required packages
import random
import string
# Check if input is an integer
try:
    size= int(input('Type the required length of your password: '))
# Raise an exception if not
except:
    print("Please type a number as input.")
    exit()
# Check input size is greater then 15
if size < 16 or size >= 31:
    print("Please type your input again. The length should be between 16 and 30.")
    exit()
# Create the password string
password=''
# Add random uppercase letter, lowercase letter or number
for i in range(size):
    password+=random.choice(string.ascii_letters + string.digits)
# Print the random secure password
print(password)
