alfabeto = 'abcdefghijklmnopqrstuvwxyz'

rotacao = alfabeto[13:]+alfabeto[:13]

ed = int(input("Type 1 for encrypt and 2 for decrypt\n"))

arqv = open("texto.txt", "r")

text = str(arqv.readlines())

text = text.replace("[", "")
text = text.replace("'", "")
text = text.replace("]", "")

arqvout = open("encryptedsub.txt","r+")

if(ed == 1):
	text = text.lower()
	encrypted = ''
	for x in text:
		if(x.isalpha()):
			indice = alfabeto.find(x)
			encrypted += rotacao[indice]
		else:
			encrypted += x
	encrypted = encrypted.upper()
	print(encrypted)
	arqvout.write(encrypted)

elif(ed == 2):
	decrypt = str(arqvout.readlines())
	decrypt = decrypt.lower()
	decrypt.replace("[", "")
	decrypt.replace("'", "")
	decrypt.replace("]", "")
	decrypted = ''
	for x in decrypt:
		if(x.isalpha()):
			indice = rotacao.find(x)
			decrypted += alfabeto[indice]
		else:
			decrypted += x
	print(decrypted)
