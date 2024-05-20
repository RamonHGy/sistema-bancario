from exbanco.interface import *
from time import sleep
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    resposta = menu(['Depositar', 'Sacar', 'Extrato', 'Sair'])
    if resposta == 1:
        cabecalho('DEPÓSITO')
        deposito = float(input('Valor que deseja depositar: '))
        if deposito > 0:
            print(f'Depósito de R${deposito:.2f} realizado com sucesso')
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}\n'
        else:
            print('Informe um valor válido para depósito!')
    elif resposta == 2:
        cabecalho('SAQUE')
        saque = float(input('Valor que deseja sacar: '))

        limite_saldo = saque > saldo

        limite_saque = numero_saques >= LIMITE_SAQUES

        saque_excedido = saque > limite

        if limite_saldo:
            print('Operação falhou! Saldo insuficiente.')
        elif saque_excedido:
            print('Operação falhou! Valor excede o limite de saque por vez')
        elif limite_saque:
            print('Operação falhou! Limite diario de saque excedido')

        elif saque > 0:
            print(f'Saque de {saque:.2f} realizado com sucesso!')
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! Informe um valor válido.')
    elif resposta == 3:
        cabecalho('EXTRATO')
        if not extrato:
            print('Nenhum movimentação foi realizada')
        else:
            print(extrato)
            print(f'Saldo: R$ {saldo:.2f}')
    elif resposta == 4:
        print('Encerrando o sistema!')
        break
    else:
        print('Operação inválida! Escolha uma operação válida.')
    sleep(1)