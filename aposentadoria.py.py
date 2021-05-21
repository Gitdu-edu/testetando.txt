## Projeto aposentadoria
## Boa noite,Deu MUITO trabalho, com muito custo consegui resolver, espero que aceite.

nome = input("Informe seu nome: \n")
renda = float(input("Informe sua renda: \n"))
sexo = str(input("Genero m ou f: \n"))
idade = int(input("Qual sua Idade: \n"))

if renda == 0:
    print("Sua renda não pode ser zero")
    exit()
if sexo == "f" and idade >=61:
    aposentou = renda * 0.7
    print("Aposentadoria liberada Sra", nome,"valor a receber:",aposentou)
if sexo == "f" and idade <61:
    tempo = 60 - idade
    print("Olá Sra", nome,"não está na idade para aposentar. Daqui", tempo,"anos a mesma irá aposentar")
if sexo == "m" and idade >=66:
    aposentou = renda * 0.75
    print("Aposentadoria liberada Sr", nome,"valor a receber:",aposentou)
if sexo == "m" and idade <66:
    tempo = 65 - idade
    print("Olá Sr", nome,"não está na idade para aposentar. Daqui", tempo,"anos a mesmo irá aposentar")
    
