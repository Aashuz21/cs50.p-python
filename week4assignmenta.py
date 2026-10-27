import emoji
emj=input("Enter a string in proper format:")
data=emoji.emojize(emj,language='alias')
print(data)