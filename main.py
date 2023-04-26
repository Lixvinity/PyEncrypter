import random
import string
import copy

Debug = False

Normal_Characters = list(string.ascii_letters + string.digits + string.punctuation)

Key = input ('Enter debug key')
random.seed(Key)

CypherCharacters = copy.deepcopy(Normal_Characters)

random.shuffle(CypherCharacters)

crypt_Type = input('Encrypt or Decrypt... E or D')

if crypt_Type == 'e':
  crypt_Type = True
else:
  crypt_Type = False
if Debug == True:
  print (Normal_Characters)
  print('------NEW LINE------')
  print (CypherCharacters)

InputPVtext = 'decrypt'

if crypt_Type == True:
  InputPVtext = ('encrypt')

Text = input('What would you like to ' + InputPVtext)
