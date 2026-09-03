#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int   opcao;
    float saldo = 0.0f;
    float valor;
    bool  encerrar = false; 

    printf("=== CAIXA ELETRONICO ===\n");

    while (encerrar == false) {
        printf("\n--- MENU ---\n");
        printf("1 - Consultar saldo\n");
        printf("2 - Depositar\n");
        printf("3 - Sacar\n");
        printf("4 - Encerrar\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            printf("Saldo atual: R$ %.2f\n", saldo);
        } else if (opcao == 2) {
            printf("Valor do deposito (R$): ");
            scanf("%f", &valor);

            if (valor > 0) {
                saldo = saldo + valor;
                printf("Deposito realizado. Novo saldo: R$ %.2f\n", saldo);
            } else {
                printf("Valor invalido. O deposito deve ser maior que zero.\n");
            }
        } else if (opcao == 3) {
            printf("Valor do saque (R$): ");
            scanf("%f", &valor);

            if (valor <= 0) {
                printf("Valor invalido. O saque deve ser maior que zero.\n");
            } else if (valor > saldo) {
                printf("Saldo insuficiente. Saldo atual: R$ %.2f\n", saldo);
            } else {
                saldo = saldo - valor;
                printf("Saque realizado. Novo saldo: R$ %.2f\n", saldo);
            }
        } else if (opcao == 4) {
            encerrar = true;
            printf("\nEncerrando... Saldo final: R$ %.2f\n", saldo);
            printf("Obrigado por utilizar nosso caixa eletronico!\n");
        } else {
            printf("Opcao inexistente. Tente novamente.\n");
        }
    }

    return 0;
}
