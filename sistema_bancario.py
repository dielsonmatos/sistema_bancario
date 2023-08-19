tam = 54

print(f"+{'-' * tam}+")
print(f"|{'BEM-VINDO(A)':^{tam}}|")
print(f"|{'':^{tam}}|")
print(f"|{'<< SISTEMA BANCÁRIO 2023 - PYTHON >>':^{tam}}|")
print(f"+{'-' * tam}+\n")

menu_principal = {
    "1": "DEPÓSITO",
    "2": "SAQUE",
    "3": "APLICAÇÃO",
    "4": "EXTRATO",
    "5": "SAIR",

}

menu_aplicacao = {
    "1": "APLICAR", "2": "RESGATAR", "3": "VOLTAR",

}

saldo_corrente = 0
saldo_aplicacao = 0
limite = 500
minimo = 100
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_RESGATES = 1

while True:
    print(f"+{'-' * tam}+")
    print(f"|{'MENU PRINCIPAL':^{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in menu_principal.items():
        print(f"|{f' {k} - {v}':{tam}}|")
    print(f"+{'-' * tam}+\n")

    opcao_principal = input()

    if opcao_principal == "1":
        while True:
            try:
                valor = float(input(f"\nDigite o valor: "))

                if valor > 0:
                    print("\nDepósito realizado com sucesso!\n")
                    saldo_corrente += valor
                    extrato += f"|{f'> Depósito: R$ {valor:.2f}':{tam}}|\n"
                    break

                else:
                    print("\nAtenção: digite um valor válido.\n")

            except:
                print("\nAtenção: digite apenas números.\n")

    elif opcao_principal == "2":
        while True:
            try:
                valor = float(input("\nDigite o valor: "))

                excedeu_limite = valor > limite

                excedeu_saldo = valor > saldo_corrente

                excedeu_saques = valor > 0 and numero_saques >= LIMITE_SAQUES

                if excedeu_limite:
                    print(f"\nOperação Falhou! Valor limite por operação: {limite}\n")
                    break

                elif excedeu_saldo:
                    print("\nOperação Falhou! Valor digitado para saque é superior ao saldo em Conta Corrente.\n")
                    break

                elif excedeu_saques:
                    print(f"\nOperação Falhou! Atingiu a quantidade de saque diário: {LIMITE_SAQUES}\n")
                    break

                elif valor > 0:
                    print("\nSaque realizado com sucesso!\n")
                    saldo_corrente -= valor
                    numero_saques += 1
                    extrato += f"|{f'> Saque: R$ {valor:.2f}':{tam}}|\n"
                    break

                else:
                    print("\nAtenção: digite um valor válido.\n")

            except:
                print("\nAtenção: digite apenas números.\n")

    elif opcao_principal == "3":
        print(f"\n+{'-' * tam}+")
        print(f"|{'APLICAÇÃO':^{tam}}|")
        print(f"+{'-' * tam}+")
        for k, v in menu_aplicacao.items():
            print(f"|{f' {k} - {v}':{tam}}|")
        print(f"+{'-' * tam}+\n")

        opcao_aplicar = input()

        if opcao_aplicar == "1":
            while True:
                try:
                    valor = float(input("\nDigite o valor: "))

                    valor_minimo = valor > 0 and valor < minimo

                    excedeu_saldo = valor > saldo_corrente

                    if valor_minimo:
                        print(f"\nOperação Falhou! Valor mínimo para aplicação: {minimo}\n")
                        break

                    elif excedeu_saldo:
                        print("\nOperação Falhou! Valor digitado para aplicação é superior ao saldo em Conta Corrente.\n")
                        break

                    elif valor > 0:
                        print("\nAplicação realizada com sucesso!\n")
                        saldo_corrente -= valor
                        saldo_aplicacao += valor
                        extrato += f"|{f'> Aplicação: R$ {valor:.2f}':{tam}}|\n"
                        break

                    else:
                        print("\nAtenção: digite um valor válido.\n")

                except:
                    print("\nAtenção: digite apenas números.\n")

        elif opcao_aplicar == "2":
            while True:
                try:
                    valor = float(input("\nDigite o valor: "))

                    valor_minimo = valor > 0 and valor < minimo

                    excedeu_saldo = valor > saldo_aplicacao

                    excedeu_saques = valor > 0 and numero_saques >= LIMITE_RESGATES

                    if valor_minimo:
                        print(f"\nOperação Falhou! Valor mínimo para resgate: {minimo}\n")
                        break

                    elif excedeu_saldo:
                        print("\nOperação Falhou! Valor digitado para resgate é superior ao saldo em Aplicação.\n")
                        break

                    elif excedeu_saques:
                        print(f"\nOperação Falhou! Atingiu a quantidade de resgate diário: {LIMITE_RESGATES}\n")
                        break

                    elif valor > 0:
                        print("\nResgate realizado com sucesso!\n")
                        saldo_aplicacao -= valor
                        saldo_corrente += valor
                        numero_saques += 1
                        extrato += f"|{f'> Resgate: R$ {valor:.2f}':{tam}}|\n"
                        break

                    else:
                        print("\nAtenção: digite um valor válido.\n")

                except:
                    print("\nAtenção: digite apenas números.\n")

        elif opcao_aplicar == "3":
            opcao_conta = menu_principal

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")

    elif opcao_principal == "4":

        saldo_total = saldo_corrente + saldo_aplicacao

        print(f"\n+{'-' * tam}+")
        print(f"|{'EXTRATO':^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{f'> Saldo Conta Corrente: R$ {saldo_corrente:.2f}' :{tam}}|")
        print(f"|{f'> Saldo Aplicação: R$ {saldo_aplicacao:.2f}' :{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{f'> Saldo Total: R$ {saldo_total:.2f}' :{tam}}|")

        print(f"+{'-' * tam}+")
        print(f"|{'MOVIMENTAÇÕES':^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{f'> Não foram realizadas movimentações.':{tam}}|" if not extrato else extrato.rstrip('\n'))
        print(f"\r+{'-' * tam}+\n")
            
    elif opcao_principal == "5":
        print(f"\n+{'-' * tam}+")
        print(f"|{f'OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS':^{tam}}|")
        print(f"|{'':^{tam}}|")
        print(f"|{'<< SISTEMA BANCÁRIO 2023 - PYTHON >>':^{tam}}|")
        print(f"+{'-' * tam}+\n")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")