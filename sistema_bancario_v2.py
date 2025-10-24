import textwrap

tam = 54

print(f"+{'-' * tam}+")
print(f"|{'BEM-VINDO(A)':^{tam}}|")
print(f"|{'':^{tam}}|")
print(f"|{'<< SISTEMA BANCÁRIO 2023 - PYTHON >>':^{tam}}|")
print(f"+{'-' * tam}+\n")

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tAplicação
    [4]\tExtrato
    [5]\tNovo usuário 
    [6]\tListar usuários
    [7]\tNova conta
    [8]\tListar contas
    [9]\tSair

    => """
    return input(textwrap.dedent(menu))

def menu_aplicacao():
    menu_aplicacao = """\n
    ================ APLICAÇÃO ================
    [1]\tAplicar
    [2]\tResgatar
    [3]\tVoltar

    => """
    return input(textwrap.dedent(menu_aplicacao))


def depositar(saldo_corrente, valor, extrato, /):

    if valor > 0:
        print("\nDepósito realizado com sucesso!\n")
        saldo_corrente += valor
        extrato += f"|{f'> Depósito: R$ {valor:.2f}':{tam}}|\n"

    else:
        print("\nAtenção: digite um valor válido.\n")

    return saldo_corrente, extrato


def sacar(*, saldo_corrente, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo_corrente
    excedeu_saques = valor > 0 and numero_saques >= limite_saques

    if excedeu_limite:
        print(f"\nOperação Falhou! Valor limite por operação: {limite}\n")

    elif excedeu_saldo:
        print("\nOperação Falhou! Valor digitado para saque é superior ao saldo em Conta Corrente.\n")

    elif excedeu_saques:
        print(f"\nOperação Falhou! Atingiu a quantidade de saque diário: {limite_saques}\n")

    elif valor > 0:
        print("\nSaque realizado com sucesso!\n")
        saldo_corrente -= valor
        numero_saques += 1
        extrato += f"|{f'> Saque: R$ {valor:.2f}':{tam}}|\n"

    else:
        print("\nAtenção: digite um valor válido.\n")

    return saldo_corrente, extrato


def aplicacao(saldo_corrente, saldo_aplicacao, valor, minimo, extrato, /):
    valor_minimo = valor > 0 and valor < minimo
    excedeu_saldo = valor > saldo_corrente

    if valor_minimo:
        print(f"\nOperação Falhou! Valor mínimo para aplicação: {minimo}\n")

    elif excedeu_saldo:
        print("\nOperação Falhou! Valor digitado para aplicação é superior ao saldo em Conta Corrente.\n")

    elif valor > 0:
        print("\nAplicação realizada com sucesso!\n")
        saldo_corrente -= valor
        saldo_aplicacao += valor
        extrato += f"|{f'> Aplicação: R$ {valor:.2f}':{tam}}|\n"

    else:
        print("\nAtenção: digite um valor válido.\n")

    return saldo_corrente, saldo_aplicacao, extrato


def resgatar(*, saldo_corrente, saldo_aplicacao, valor, extrato, minimo, numero_saques, limite_resgates):
    valor_minimo = valor > 0 and valor < minimo
    excedeu_saldo = valor > saldo_aplicacao
    excedeu_saques = valor > 0 and numero_saques >= limite_resgates

    if valor_minimo:
        print(f"\nOperação Falhou! Valor mínimo para resgate: {minimo}\n")

    elif excedeu_saldo:
        print("\nOperação Falhou! Valor digitado para resgate é superior ao saldo em Aplicação.\n")

    elif excedeu_saques:
        print(f"\nOperação Falhou! Atingiu a quantidade de resgate diário: {limite_resgates}\n")

    elif valor > 0:
        print("\nResgate realizado com sucesso!\n")
        saldo_aplicacao -= valor
        saldo_corrente += valor
        numero_saques += 1
        extrato += f"|{f'> Resgate: R$ {valor:.2f}':{tam}}|\n"

    else:
        print("\nAtenção: digite um valor válido.\n")

    return saldo_corrente, saldo_aplicacao, extrato


def exibir_extrato(saldo_corrente, saldo_aplicacao, /, *, extrato):
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
    print(f"+{'-' * tam}+\n")

    return saldo_corrente, saldo_aplicacao, extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n*** Usuário criado com sucesso! ***")


def listar_usuarios(usuarios):

    for usuario in usuarios:

        linha = f"""\
            Nome:\t{usuario['nome']}
            Data de Nascimento:\t5{usuario['data_nascimento']}
            CPF:\t{usuario['cpf']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n*** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não econtrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):

    for conta in contas:

        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    LIMITE_RESGATES = 1
    AGENCIA = "0001"

    saldo_corrente = 0
    saldo_aplicacao = 0
    limite = 500
    minimo = 100
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao_principal = menu()

        if opcao_principal == "1":
            try:
                valor = float(input(f"\nDigite o valor: "))
                saldo_corrente, extrato = depositar(saldo_corrente, valor, extrato)

            except:
                print("\nAtenção: digite apenas números.\n")

        elif opcao_principal == "2":
            try:
                valor = float(input("\nDigite o valor: "))
                saldo_corrente, extrato = sacar(
                    saldo_corrente=saldo_corrente,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )

            except:
                print("\nAtenção: digite apenas números.\n")

        elif opcao_principal == "3":
            opcao_aplicar = menu_aplicacao()

            if opcao_aplicar == "1":
                try:
                    valor = float(input("\nDigite o valor: "))
                    saldo_corrente, saldo_aplicacao, extrato = aplicacao(saldo_corrente, saldo_aplicacao, valor, minimo, extrato)

                except:
                    print("\nAtenção: digite apenas números.\n")

            elif opcao_aplicar == "2":
                try:
                    valor = float(input("\nDigite o valor: "))
                    saldo_corrente, saldo_aplicacao, extrato = resgatar(
                        saldo_corrente=saldo_corrente,
                        saldo_aplicacao=saldo_aplicacao,
                        valor=valor,
                        minimo=minimo,
                        extrato=extrato,
                        numero_saques=numero_saques,
                        limite_resgates=LIMITE_RESGATES
                    )

                except:
                    print("\nAtenção: digite apenas números.\n")

            elif opcao_aplicar == "3":
                opcao_aplicar = opcao_principal

            else:
                print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")

        elif opcao_principal == "4":
            saldo_corrente, saldo_aplicacao, extrato = exibir_extrato(saldo_corrente, saldo_aplicacao, extrato=extrato)

        elif opcao_principal == "5":
            criar_usuario(usuarios)

        elif opcao_principal == "6":
            listar_usuarios(usuarios)

        elif opcao_principal == "7":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao_principal == "8":
            listar_contas(contas)

        elif opcao_principal == "9":
            print(f"\n+{'-' * tam}+")
            print(f"|{f'OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS':^{tam}}|")
            print(f"|{'':^{tam}}|")
            print(f"|{'<< SISTEMA BANCÁRIO 2023 - PYTHON >>':^{tam}}|")
            print(f"+{'-' * tam}+\n")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")

main()