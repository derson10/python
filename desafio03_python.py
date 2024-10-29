import os
from datetime import datetime
import pytz
import textwrap

def menu():
    menu = """\n
    =======================
    -  MENU BANCO DO POVO -
    -----------------------
    - [d]\tDepositar       
    - [s]\tSacar           
    - [e]\tExtrato         
    - [ab]\tAbrir Conta    
    - [lc]\tListar Contas  
    - [nc]\tNovo Cliente   
    - [q]\tSair            
    ------------------------
    => """
    return input(textwrap.dedent(menu))

#Função que cadastra cliente
# Argumentos: nome, data_nasc, endereco)logradouro/bairro/cidade/UF, cpf
# gravar somente os numeros do CPF - sem ponto e traco
# nao podemos cadastrar o mesmo cpf

def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF - somente número: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("CPF já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento - dd-mm-aaaa: ")
    endereco = input("Informe o endereço - logradouro, nro - bairro - cidade/sigla estado: ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Cliente cadastrado com sucesso! ===")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

#Função que cria conta-corrente
# armazenar lista: agencia-número da conta - usuario
# Argumentos: documento, agencia, conta
# 022.222.222-22 - Ag:0001 - Conta: 1
def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#Função que realiza depósito - positional only *** 
# argumentos: saldo, valor, extrato
# retorna: saldo e extrato
def realiza_deposito(saldo, valor_deposito, extrato, /):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("Valor de depósito inválido. Por favor, insira um valor positivo.")

    return saldo, extrato

#Fundção que realiza o saque - keyword only***
def realiza_saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente para realizar o saque!")
    
    elif excedeu_limite:
        print("Você excedeu o limite de saque diário!")

    elif excedeu_saques:
        print("Você excedeu o número de saques diários!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

#Função que imprime extrato com toda movimentação realizada
#Função que coloca cabeçalho no extrato e imprime extrato
#sempre exibir o saldo atual da conta no formato R$ 1500.45
def imprime_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")



def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            os.system('cls')
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = realiza_deposito(saldo, valor, extrato)
        
        elif opcao == "s":
            os.system('cls')
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = realiza_saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            os.system('cls')
            imprime_extrato(saldo, extrato=extrato)
        
        elif opcao == "nc":
            os.system('cls')
            cadastrar_cliente(clientes)

        elif opcao == "ab":
            os.system('cls')
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            os.system('cls')
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida. Tente novamente.")


main()