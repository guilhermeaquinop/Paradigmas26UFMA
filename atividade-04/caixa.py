# Atividade 04 - Caixa eletronico (atividade 02) refatorado para o paradigma funcional.

def mostrar_menu():
    print("\n--- MENU ---")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Encerrar")


def depositar(saldo, valor):
    if valor > 0:
        print("Deposito realizado. Novo saldo: R$ %.2f" % (saldo + valor))
        return saldo + valor
    else:
        print("Valor invalido. O deposito deve ser maior que zero.")
        return saldo


def sacar(saldo, valor):
    if valor <= 0:
        print("Valor invalido. O saque deve ser maior que zero.")
        return saldo
    elif valor > saldo:
        print("Saldo insuficiente. Saldo atual: R$ %.2f" % saldo)
        return saldo
    else:
        print("Saque realizado. Novo saldo: R$ %.2f" % (saldo - valor))
        return saldo - valor


def executar(saldo):
    mostrar_menu()
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        print("Saldo atual: R$ %.2f" % saldo)
        return executar(saldo)
    elif opcao == 2:
        valor = float(input("Valor do deposito (R$): "))
        return executar(depositar(saldo, valor))
    elif opcao == 3:
        valor = float(input("Valor do saque (R$): "))
        return executar(sacar(saldo, valor))
    elif opcao == 4:
        return saldo
    else:
        print("Opcao inexistente. Tente novamente.")
        return executar(saldo)


# --- programa principal ---

print("=== CAIXA ELETRONICO ===")

saldo_final = executar(0.0)

print("\nEncerrando... Saldo final: R$ %.2f" % saldo_final)
print("Obrigado por utilizar nosso caixa eletronico!")
