# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


resposta = str.upper(input("Que turno você estuda? \n M-Matutino  V-Vespertino  N- Noturno   \n"))



if resposta == "M":
    print("Bom dia")

elif resposta == "V":
        print("Boa Tarde")


elif resposta == "N":
      print ("Boa Noite!")

else:
      print("Você precisa digitar o turno que você estuda!")