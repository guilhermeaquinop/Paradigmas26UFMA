# Atividade 02 — Caixa Eletronico (PDV) - Pseudocódigo

```
INÍCIO
    saldo    <- 0
    encerrar <- FALSO

    ESCREVA "=== CAIXA ELETRONICO ==="

    ENQUANTO encerrar = FALSO FAÇA
        ESCREVA "--- MENU ---"
        ESCREVA "1 - Consultar saldo"
        ESCREVA "2 - Depositar"
        ESCREVA "3 - Sacar"
        ESCREVA "4 - Encerrar"
        LEIA opcao

        SE opcao = 1 ENTÃO
            ESCREVA "Saldo atual: R$ ", saldo

        SENÃO SE opcao = 2 ENTÃO
            LEIA valor
            SE valor > 0 ENTÃO
                saldo <- saldo + valor
                ESCREVA "Deposito realizado. Novo saldo: R$ ", saldo
            SENÃO
                ESCREVA "Valor invalido. O deposito deve ser maior que zero."
            FIM_SE

        SENÃO SE opcao = 3 ENTÃO
            LEIA valor
            SE valor <= 0 ENTÃO
                ESCREVA "Valor invalido. O saque deve ser maior que zero."
            SENÃO SE valor > saldo ENTÃO
                ESCREVA "Saldo insuficiente. Saldo atual: R$ ", saldo
            SENÃO
                saldo <- saldo - valor
                ESCREVA "Saque realizado. Novo saldo: R$ ", saldo
            FIM_SE

        SENÃO SE opcao = 4 ENTÃO
            encerrar <- VERDADEIRO
            ESCREVA "Encerrando... Saldo final: R$ ", saldo
            ESCREVA "Obrigado por utilizar nosso caixa eletronico!"

        SENÃO
            ESCREVA "Opcao inexistente. Tente novamente."
        FIM_SE
    FIM_ENQUANTO
FIM
```
