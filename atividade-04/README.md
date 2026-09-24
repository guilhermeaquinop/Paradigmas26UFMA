# Atividade 04 — Caixa Eletronico (Paradigma Funcional) - Pseudocódigo

```
FUNÇÃO mostrar_menu()
    ESCREVA "--- MENU ---"
    ESCREVA "1 - Consultar saldo"
    ESCREVA "2 - Depositar"
    ESCREVA "3 - Sacar"
    ESCREVA "4 - Encerrar"
FIM_FUNÇÃO

FUNÇÃO depositar(saldo, valor)
    SE valor > 0 ENTÃO
        ESCREVA "Deposito realizado. Novo saldo: R$ ", saldo + valor
        RETORNE saldo + valor
    SENÃO
        ESCREVA "Valor invalido. O deposito deve ser maior que zero."
        RETORNE saldo
    FIM_SE
FIM_FUNÇÃO

FUNÇÃO sacar(saldo, valor)
    SE valor <= 0 ENTÃO
        ESCREVA "Valor invalido. O saque deve ser maior que zero."
        RETORNE saldo
    SENÃO SE valor > saldo ENTÃO
        ESCREVA "Saldo insuficiente. Saldo atual: R$ ", saldo
        RETORNE saldo
    SENÃO
        ESCREVA "Saque realizado. Novo saldo: R$ ", saldo - valor
        RETORNE saldo - valor
    FIM_SE
FIM_FUNÇÃO

FUNÇÃO executar(saldo)
    mostrar_menu()
    LEIA opcao

    SE opcao = 1 ENTÃO
        ESCREVA "Saldo atual: R$ ", saldo
        RETORNE executar(saldo)
    SENÃO SE opcao = 2 ENTÃO
        LEIA valor
        RETORNE executar(depositar(saldo, valor))
    SENÃO SE opcao = 3 ENTÃO
        LEIA valor
        RETORNE executar(sacar(saldo, valor))
    SENÃO SE opcao = 4 ENTÃO
        RETORNE saldo
    SENÃO
        ESCREVA "Opcao inexistente. Tente novamente."
        RETORNE executar(saldo)
    FIM_SE
FIM_FUNÇÃO

INÍCIO
    ESCREVA "=== CAIXA ELETRONICO ==="

    saldo_final <- executar(0)

    ESCREVA "Encerrando... Saldo final: R$ ", saldo_final
    ESCREVA "Obrigado por utilizar nosso caixa eletronico!"
FIM
```
