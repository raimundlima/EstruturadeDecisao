#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = input ("digite uma letra \n")

if (vogal in ('aeiou') or vogal in ('AEIOU')):
    print (f"A letra que vc digitou foi {vogal}  ela é uma vogal!")

else:
    print("A letra não é uma vogal!")
