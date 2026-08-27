#include <stdio.h>

int main(void)
{
    char  nome[100];
    int   idade, quantidade;
    float saldo, preco, total;
    char  status[60];

    printf("Nome do cliente: ");
    scanf(" %[^\n]", nome);

    printf("Idade: ");
    scanf("%d", &idade);

    printf("Saldo disponivel (R$): ");
    scanf("%f", &saldo);

    printf("Preco do produto +18 (R$): ");
    scanf("%f", &preco);

    printf("Quantidade desejada: ");
    scanf("%d", &quantidade);

    total = preco * quantidade;

    if (idade >= 18 && saldo >= total) {
        sprintf(status, "APROVADA - compra autorizada");
        saldo = saldo - total;
    } else if (idade >= 18) {
        sprintf(status, "NEGADA - saldo insuficiente");
    } else if (saldo >= total) {
        sprintf(status, "NEGADA - menor de idade");
    } else {
        sprintf(status, "NEGADA - menor de idade e sem saldo");
    }

    printf("\n--- COMPROVANTE ---\n");
    printf("Cliente: %s\n", nome);
    printf("Idade: %d\n", idade);
    printf("Quantidade: %d\n", quantidade);
    printf("Total: R$ %.2f\n", total);
    printf("Situacao: %s\n", status);
    printf("Saldo final: R$ %.2f\n", saldo);

    return 0;
}
