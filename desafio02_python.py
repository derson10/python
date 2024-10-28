import os
from datetime import datetime
import pytz

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

meu_limite = 500

saques_realizados = 0

meu_extrato = ""

LIMITE_TRANSACOES = 10

LIMITE_SAQUES = 3

#Função que cadastra cliente
# Argumentos: nome, data_nasc, endereco)logradouro/bairro/cidade/UF, cpf
# gravar somente os numeros do CPF - sem ponto e traco
# nao podemos cadastrar o mesmo cpf


#Função que cria conta-corrente
# armazenar lista: agencia-número da conta - usuario
# Argumentos: documento, agencia, conta
# 017.963.259-02 - Ag:0001 - Conta: 1


#Função que realiza depósito - positional only *** 
# argumentos: saldo, valor, extrato
# retorna: saldo e extrato
def realiza_deposito(valor_deposito):
    
    global saldo
    global LIMITE_TRANSACOES

    if LIMITE_TRANSACOES == 0:
        print("Você atingiu o limite de transações diárias!")
        return False

    if valor_deposito > 0:
        
        saldo += valor_deposito
        LIMITE_TRANSACOES -= 1
        grava_extrato("Depósito", valor_deposito)
        print("Depósito realizado com sucesso!")
        return saldo
    else:
        print("Valor de depósito inválido. Por favor, insira um valor positivo.")

#Fundção que realiza o saque - keyword only***
def realiza_saque(valor_saque):
    
    global saldo
    global limite_diario
    global LIMITE_SAQUES
    global LIMITE_TRANSACOES
    global meu_limite 
    
    if LIMITE_TRANSACOES == 0:
        print("Você atingiu o limite de transações diárias!")
        return False
    
    if LIMITE_SAQUES == 0:
        print("ATENÇÃO!!! Você ultrapassou a quantidade de saques diário!")
        return False
    
    if limite_diario == 0 or valor_saque > limite_diario:
        print("ATENÇÃO!!! Você ultrapassou o seu limite de saque diário!")
        return False
    
    if valor_saque > meu_limite:
        print("ATENÇÃO!!! O valor do saque excedido!")
        return False
    
    if valor_saque <= 0:
        print("Valor de saque inválido. Por favor, insira um valor positivo.")
        return False
    
    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_diario:
        LIMITE_SAQUES -= 1
        LIMITE_TRANSACOES -= 1
        saldo -= valor_saque
        limite_diario -= valor_saque
        grava_extrato("Saque   ", valor_saque)
        print("Saque Realizado com Sucesso!")
    else:
        print("Saldo Indisponível!")

#Função que grava todas as movimentações realizadas na conta bancária 
# receber argumentos positional only e keyword only
# argumentos posicionais: saldo, argumentos nomeados:extrato

def grava_extrato(tipo_operacao, valor_operacao):
    
    global meu_extrato
    global saldo
    global limite_diario
    global saques_realizados
    mascara_ptbr = "%d/%m/%Y %H:%M:%S"  

    data_hora_atual = datetime.now()
    data_hora_transacao = data_hora_atual.strftime(mascara_ptbr) 
    
    meu_extrato += data_hora_transacao + " - " + tipo_operacao + " - R$ " + str(format(valor_operacao,".2f")) + "\n"

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