menu = '''
===================
    Menu Banco PY

[1] Depósito;
[2] Saque;
[3] Extrato;
[9] Sair

===================   '''

saldo = 0
limite_por_operacao = 500
extrato = ""
quantid_saques_dia = 0
LIMITE_SAQUES_DIA = 3

while True:
    opcao = input(f'{menu}\n opção: ')

    if opcao == '1':
        valor_deposito = float(input('Informe o valor do depósito: ')) 

        if valor_deposito >0:
            saldo += valor_deposito
            extrato += (f' Depósito: R$ {valor_deposito:.2f} (+) \n ')
            print('Depósito bem sucedido!') 
        
        else:
            print("O valor informado é inválido!")

    elif opcao =='2':
        valor_saque = float(input('Informe o valor de saque: '))

        excedeu_saldo = valor_saque>saldo
        excedeu_limite_por_operacao = valor_saque > limite_por_operacao
        excedeu_saques = quantid_saques_dia >= LIMITE_SAQUES_DIA

        if excedeu_saldo:
            print('Operação fahou!\nVocê não tem saldo suficiente.')

        elif excedeu_limite_por_operacao:
            print(f'Operação fahou!\nO valor do saque excede o limite o seu limite.\nO seu limite de saque por operação é R${limite_por_operacao:.2f}')
        
        elif excedeu_saques:
            print('Operação fahou!\nMúmero máximo de saques excedido.')
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += (f'Saque: R$ {valor_saque:.2f} (-)\n ')
            quantid_saques_dia += 1
            print(f'Saque bem sucedido!\nVocê ainda tem {LIMITE_SAQUES_DIA-quantid_saques_dia} saques diário') 
        
        else:
            print("Operação fahou!\nValor informado é inválido.\n ")

    
    elif opcao == '3':
        print("\n ------------------- Extrato -------------------")
        print("\n Não foram realizadas movimentações anteriores." if not extrato else extrato )
        print(f"Saldo: R${saldo:.2f}")
        print("----------------- Fim Extrato -----------------")

    
    elif opcao == '9':
        print("Processo finalizado!")
        break

    else:
        print("Operação inválida\nEscolha uma das opções do MENU")





