    #----------------------------------------------------------------------------------------------------#
    #----------------------------NOME: ANDREZA OLIVEIRA--------------------------------------------------# 
    #----------------------------Data: 05/01/2023--------------------------------------------------------#
    #----------------------------Programa: Validação de CPF----------------------------------------------#
    #----------------------------------------------------------------------------------------------------#
  
    #------------------------------INÍCIO--------------------------------------------------------------#
   
    #------------------------DECLARAÇÃO DE VÁRIAVEIS E IMPORTAÇÕES----------------------------------#
seucpf =''
dig1 = 0 
dig2 = 0
dig1_checar = 0
dig2_checar = 0
i = 1   
resposta ='1'
while resposta == '1':
    #-------------------------INÍCIO DO PROGRAMA E COLETA DE DADOS--------------------------------#
 print("-------------------------------Validar CPF---------------------------------------\n")
 print("----------------------------------------------------------------------------\n") 
 print("Digite seu nome: \n")
 print("----------------------------------------------------------------------------\n")
 nome = input()
 print("----------------------------------------------------------------------------\n")
 print("Digite seu CPF. OBS: Sem PONTOS(.) e  TRAÇOS(-), somente o NÚMERO!!!:\n")
 print("----------------------------------------------------------------------------\n")
 seucpf = input()
 print("----------------------------------------------------------------------------\n")
  
 if not seucpf.isdigit():     #----VERIFICA SE O QUE O USUARIO DIGITOU É UM NÚMERO, SENÃO ELE PARA O PROGRAMA. 
       print("CPF INVÁLIDO\n")
       print(seucpf)
       resposta = input("Deseja fazer novamente?\n 1-SIM \n 2-NÂO")
    
 elif (len(seucpf))<11 or (len(seucpf))>11: #----VERIFICA O TAMANHO DO CPF, SE FOR MENOR QUE 11 DIGITOS OU SE FOR MAIOR O CPF É INVÁLIDO!
       print("CPF INVÁLIDO\n")
       resposta = input("Deseja fazer novamente?\n 1-SIM \n 2-NÂO")

 else:
    #----------------------------PARTE QUE OBTÉM O PENÚLTIMO E ÚLTIMO DÍGITO DO CPF--------------#
        dig1_checar = int(seucpf[9:10])  #--OBTÉM O PENÚLTIMO DÍGITO ----------------------------------#
        dig2_checar = int(seucpf[10:11]) #--OBTÉM O ÚLTIMO DÍGITO -------------------------------------#
   

    #----------------------------CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR--------------------------#
        for i in range(1,10) :
            dig1 = dig1 + int(seucpf[i-1:i]) * i
    
    #----------------------------------RESTO DO PRIMEIRO DIGITO VERIFICADOR----------------------# 
        dig1 = dig1 % 11
  
 
        if (dig1 == 10):
            dig1 = 0

        if (dig1 != dig1_checar) :
              print("Digito 1 inválido!\n")
   
    #----------------------------CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR--------------------------#
        for i in range(2,11):
            dig2 = dig2 + int(seucpf[i-1:i]) * (i -1)
    
    #----------------------------------RESTO DO SEGUNDO DIGITO VERIFICADOR----------------------# 
        dig2 = dig2 % 11
    
        if dig2 != dig2_checar:
            print("Digito 2 inválido!\n")
    
    #----------------------------------CONDIÇÃO QUE VERIFICA SE O CPF É VÁLIDO-----------------#    
        if (dig1 == dig1_checar and dig2 == dig2_checar): #VERIFICA OS DIGITOS
            print("--------------------Resultado-----------------------------\n")
            print(nome,", seu CPF é válido!\n")
    #------------------------FORMATAÇÃO--------------------------------------------------------#
            print(seucpf[0:3],".",seucpf[3:6],".",seucpf[6:9],"-",seucpf[9:11]) 
            resposta = input("Deseja fazer novamente?\n 1-SIM \n 2-NÂO")

        else:
           print("-------------------------------RESULTADO-----------------------------------------\n")
           print("---------------------------------------------------------------------------------\n")
           print(nome,", seu CPF é inválido!\n")
           print("---------------------------------------------------------------------------------\n")
           resposta = input("Deseja fazer novamente?\n 1-SIM \n 2-NÂO")

