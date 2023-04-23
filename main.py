import random
import string


NormalCharacters = list(string.ascii_letters + string.digits + string.punctuation)

print (NormalCharacters)

Key = input('Enter Key')

random.seed(Key)
Output1 = (random.randint())
print (Output1)
