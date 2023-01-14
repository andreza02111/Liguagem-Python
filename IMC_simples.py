#------------------------------------------------------------------------------------------#
#------------------------NOME: ANDREZA OLIVEIRA--------------------------------------------# 
#------------------------E-MAIL: andrezaoliveira20199@gmail.com----------------------------#
#------------------------DATA: 11/12/2022--------------------------------------------------#
#------------------------IMC DE HOMENS E MULHERES------------------------------------------#

print("----------------------------Cálculo IMC----------------------------")
print("Qual seu nome?")
nome = input()
genero= int(input("Digite: \n1-Mulher\n2-Homem")) 

altura=float(input("Qual sua altura? Escreva em decimal (EX: 1.70)"))

peso=float(input("Qual seu peso? Escreva em decimal (EX: 55.60)"))

if genero == 1 :  #calculo imc feminino
    resultado=peso/(altura*altura)  #calcula o imc dividindo o peso pela altua ao quadrado 
    resultado = round(resultado,2)
    print("---------------------------Resultado---------------------------------------")
    if resultado<19.1:
        print(nome,", você está abaixo do peso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
    elif resultado ==19.1 or resultado<=25.8:
        print(nome,", seu peso é ideal!\n" "Sua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
        
    elif resultado ==25.9  or  resultado<= 27.3:
        print(nome,", você está um pouco acima do peso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
    elif resultado ==27.4 or resultado <=32.3 :
         print(nome,", você está acima do peso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
    elif resultado >= 32.4:
         print(nome,", você está obeso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
    else:
        print("PESO INVALÍDO, REFAÇA O TESTE!")
    print("-------------------------------------------------------------------------")    
#-------------------- MASCULINO--------------------------#

if genero == 2 :  #calculo imc masculino
    resultado=peso/(altura*altura)  #calcula o imc dividindo o peso pela altua ao quadrado 
    resultado = round(resultado,2)
    print("---------------------------Resultado---------------------------------------")
    if resultado<20.7:
        print(nome,", você está abaixo do peso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
        
    elif resultado ==20.7 or resultado<=26.4: 
        print(nome,", seu peso é ideal!\n" "Sua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
        
    elif resultado ==26.5  or  resultado<= 27.8:
        print(nome,", você está um pouco acima do peso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
        
    elif resultado ==27.9 or resultado <=31.1 :
         print(nome,", você está acima do peso! \nSua altura é:",altura,"\n eu peso é: ", peso, "\nSeu IMC é:",resultado)
         
    elif resultado >= 31.2:
         print(nome, ",você está obeso! \nSua altura é:",altura,"\nSeu peso é: ", peso, "\nSeu IMC é:",resultado)
    else:
        print("PESO INVALÍDO, REFAÇA O TESTE!")
    print("-------------------------------------------------------------------------")    