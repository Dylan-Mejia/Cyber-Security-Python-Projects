import random 
import string

uppercase_letters =  string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

upper,lower,nums,syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

length = 20
amount = 10

print("Here is a list of complex passwords to use.")
for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
