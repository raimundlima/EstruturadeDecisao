#Faça um Programa que peça dois números e imprima o maior deles.

number01 = int(input("Digite o primeiro número: \n"))
number02 = int(input("Digite o segundo  número: \n"))

if number01 > number02:
    print(f"O número {number01} é maior que o {number02}")

elif number02 > number01:
        print(f"O número {number02} é maior que o {number01}")

else:
      print("Os dois números são iguais.")


