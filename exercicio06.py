#Faça um Programa que leia três números e mostre o maior deles.

number01 = int(input("Digite o número 01: \n"))
number02 = int(input("Digite o número 02: \n"))
number03 = int(input("Digite o número 03: \n"))

maior = number01 

if (number02 > maior):
    maior = number02
if (number03 > maior):
    maior = number03

print (f" o maior número é {maior} ")