alfabeto = 'abcdefghijklmnopqrstuvwxyz'

rotacao = alfabeto[13:]+alfabeto[:13]

ed = int(input("Type 1 for encrypt and 2 for decrypt\n"))

if(ed == 1):
	text = input("Type in what you want encrypted\n")
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

elif(ed == 2):
	text = input("Type in what you want decrypted\n")
	text = text.lower()
	decrypted = ''
	for x in text:
		if(x.isalpha()):
			indice = rotacao.find(x)
			decrypted += alfabeto[indice]
		else:
			decrypted += x
	print(decrypted)
