# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

resposta = str(input("Digite seu sexo: \n"))



if resposta == "M":
    print("Masculino")

elif resposta == "F":
        print("Feminino")

else:
      print("Você precisa digitar M ou F")