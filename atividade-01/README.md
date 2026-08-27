# Atividade 01 — Programa com Tomada de Decisão - Pseudocódigo

```
INÍCIO
    LEIA nome, idade, saldo, preco, quantidade

    total <- preco * quantidade

    SE idade >= 18 E saldo >= total ENTÃO
        status <- "APROVADA - compra autorizada"
        saldo  <- saldo - total
    SENÃO SE idade >= 18 ENTÃO
        status <- "NEGADA - saldo insuficiente"
    SENÃO SE saldo >= total ENTÃO
        status <- "NEGADA - menor de idade"
    SENÃO
        status <- "NEGADA - menor de idade e sem saldo"
    FIM_SE

    ESCREVA "--- COMPROVANTE ---"
    ESCREVA "Cliente: ", nome
    ESCREVA "Idade: ", idade
    ESCREVA "Quantidade: ", quantidade
    ESCREVA "Total: R$ ", total
    ESCREVA "Situacao: ", status
    ESCREVA "Saldo final: R$ ", saldo
FIM
```