import os

menu = '''
------------------
-  BANCO DO POVO -
------------------
- [d] Depositar  -
- [s] Sacar      -
- [e] Extrato    -
- [q] Sair       -
------------------
=> '''

saldo = 0

limite_diario = 500

saques_realizados = 0

meu_extrato = ""

LIMITE_SAQUES = 3

#Função que realiza depósito
def realiza_deposito(valor_deposito):
    
    global saldo

    if valor_deposito > 0:
        
        saldo += valor_deposito
        grava_extrato("Depósito", valor_deposito)
        print("Depósito realizado com sucesso!")
    else:
        print("Valor de depósito inválido. Por favor, insira um valor positivo.")

#Fundção que realiza o saque 
def realiza_saque(valor_saque):
    
    global saldo
    global limite_diario
    global LIMITE_SAQUES
    
    if LIMITE_SAQUES == 0:
        print("ATENÇÃO!!! Você ultrapassou a quantidade de saques diário!")
        return False
    
    if limite_diario == 0:
        print("ATENÇÃO!!! Você ultrapassou o seu limite de saque!")
        return False

    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_diario:
        LIMITE_SAQUES -= 1
        saldo -= valor_saque
        limite_diario -= valor_saque
        grava_extrato("Saque   ", valor_saque)

        print("Saque Realizado com Sucesso!")
    else:
        print("Saldo Indisponível!")


#Função que grava todas as movimentações realizadas na conta bancária 
def grava_extrato(tipo_operacao, valor_operacao):
    
    global meu_extrato
    global saldo
    global limite_diario
    global saques_realizados

    meu_extrato += tipo_operacao + " - R$ " + str(format(valor_operacao,".2f")) + "\n"

#Função que imprime extrato com toda movimentação realizada
#Função que coloca cabeçalho no extrato e imprime extrato
#sempre exibir o saldo atual da conta no formato R$ 1500.45
def imprime_extrato():
    global meu_extrato
    global saldo
    titulo_extrato = '''
---------------------------
- EXTRATO - BANCO DO POVO -
---------------------------
\n'''
    
    print(titulo_extrato + meu_extrato + "Saldo Atual: R$ " + str(format(saldo,".2f")))


while True:

    opcao = input(menu)

    if opcao == 'd':
        os.system('cls')
        valor_deposito = float(input("Informe o valor do depósito: "))
        realiza_deposito(valor_deposito)
    
    elif opcao == "s":
        os.system('cls')
        valor_saque = float(input("Informe o valor do saque: "))
        realiza_saque(valor_saque)

    elif opcao == "e":
        os.system('cls')
        imprime_extrato()

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Tente novamente.")