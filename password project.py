import random
import string
print(string.ascii_letters) # All lowercase and uppercase letters
print(string.digits) # Numbers 0-9
print(string.punctuation) #Symbols
length = int(input("Enter the length of your password: "))
all = string.ascii_letters + string.digits + string.punctuation
list = random.choices(all, k=length)
final = "".join(list)
print("Your final pass is: ", final)


