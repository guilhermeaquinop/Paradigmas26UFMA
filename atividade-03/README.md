# Atividade 03 — Classificação de Disciplinas (Paradigma Funcional) - Pseudocódigo

```
FUNÇÃO ler_notas(quantidade)
    notas <- vetor vazio
    PARA i DE 1 ATÉ quantidade FAÇA
        LEIA nota
        notas <- notas + [nota]
    FIM_PARA
    RETORNE notas
FIM_FUNÇÃO

FUNÇÃO calcular_media(notas)
    soma <- 0
    PARA CADA nota EM notas FAÇA
        soma <- soma + nota
    FIM_PARA
    RETORNE soma / tamanho(notas)
FIM_FUNÇÃO

FUNÇÃO gerar_classificacao(media)
    SE media >= 9.5 ENTÃO RETORNE "A"
    SENÃO SE media >= 8.0 ENTÃO RETORNE "B"
    SENÃO SE media >= 7.5 ENTÃO RETORNE "C"
    SENÃO SE media >= 6.0 ENTÃO RETORNE "D"
    SENÃO RETORNE "E"
    FIM_SE
FIM_FUNÇÃO

FUNÇÃO gerar_classificacoes(medias)
    classificacoes <- vetor vazio
    PARA CADA media EM medias FAÇA
        classificacoes <- classificacoes + [gerar_classificacao(media)]
    FIM_PARA
    RETORNE classificacoes
FIM_FUNÇÃO

FUNÇÃO gerar_aproveitamento(classificacao)
    SE classificacao = "A" OU classificacao = "B" ENTÃO
        RETORNE "Aproveita"
    SENÃO
        RETORNE "Nao aproveita"
    FIM_SE
FIM_FUNÇÃO

FUNÇÃO gerar_aproveitamentos(classificacoes)
    aproveitamentos <- vetor vazio
    PARA CADA classificacao EM classificacoes FAÇA
        aproveitamentos <- aproveitamentos + [gerar_aproveitamento(classificacao)]
    FIM_PARA
    RETORNE aproveitamentos
FIM_FUNÇÃO

INÍCIO
    ESCREVA "=== CLASSIFICACAO DE DISCIPLINAS DO MESTRADO ==="

    disciplinas <- vetor vazio
    medias      <- vetor vazio

    LEIA quantidade_disciplinas

    PARA i DE 1 ATÉ quantidade_disciplinas FAÇA
        LEIA nome
        LEIA quantidade_notas
        notas <- ler_notas(quantidade_notas)

        disciplinas <- disciplinas + [nome]
        medias      <- medias + [calcular_media(notas)]
    FIM_PARA

    classificacoes  <- gerar_classificacoes(medias)
    aproveitamentos <- gerar_aproveitamentos(classificacoes)

    ESCREVA "=== RESULTADO ==="
    PARA i DE 1 ATÉ quantidade_disciplinas FAÇA
        ESCREVA "Disciplina: ",    disciplinas[i]
        ESCREVA "Media: ",         medias[i]
        ESCREVA "Classificacao: ", classificacoes[i]
        ESCREVA "Doutorado: ",     aproveitamentos[i]
    FIM_PARA
FIM
```
