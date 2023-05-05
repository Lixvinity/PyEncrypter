import random
import string
import copy
import os


Debug = False

Normal_Characters = list(string.ascii_letters + string.punctuation + string.digits + 'ĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄɅɆɇɈɉɊɋɌɍɎɏɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯʰʱʲʳʴʵʶʷʸʹʺʻʼʽʾʿˀˁ˂˃˄˅ˆˇבגדהוזחטיךכלםמןנסעֈ')

Key = input ('Enter debug key')
random.seed(Key)

CypherCharacters = copy.deepcopy(Normal_Characters)

random.shuffle(CypherCharacters)

crypt_Type = input('Encrypt or Decrypt... E or D')

if crypt_Type == 'e' or crypt_Type == 'E':
  crypt_Type = True
if crypt_Type == 'd' or crypt_Type == 'D':
  crypt_Type = False
if Debug == True:
  print (Normal_Characters)
  print('------NEW LINE------')
  print (CypherCharacters)



if crypt_Type == True:
  InputPVtext = 'encrypt'
  Text = input('What would you like to ' + InputPVtext)
  CipherText = ''
  for letter in Text:
   index = Normal_Characters.index(letter)
   CipherText += CypherCharacters[index]
  print (CipherText)


if crypt_Type == False:
  InputPVtext = 'decrypt'
  CipherText = input('What would you like to ' + InputPVtext)
  Text = ''
  for letter in CipherText:
   index = CypherCharacters.index(letter)
   Text += Normal_Characters[index]
  print (Text)

Close_Program = input('enter any key to close program')
os._exit()
