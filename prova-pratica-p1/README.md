Na implementação conversor-temperatu.py é utilizado principalmente do paradigma funcional, onde pode ser observado nos trechos entre as linhas 1 à 52. Onde há a definição das funções de conversão e recebimento de valor.

Exemplo:

def recebeValor():
    valor = float(input('QUAL O VALOR A SER CONVERTIDO ?'))
    return valor

def converterParaCelsius(valor, unidade):
    naoExisteConversao = unidade == 'C'
    if naoExisteConversao:
        print(str(valor) +'°C')
        return
    
    match unidade:
        case 'F':
            valorConvertido = ((valor - 32) * 5)/9
            print(str(valorConvertido)+'°C')
            return
        case 'K':
            valorConvertido = valor + 273.15
            print(str(valorConvertido)+'°C')
            return

Nos trechos entre as linhas 55 e 66 há a utilização do paradigma imperativo, com a utilização de estruturas de condição.

Exemplo:

    match unidadeInicial:
        case 'C':
            converterParaCelsius(recebeValor(), unidadeFinal)
        case 'K':
            converterParaKelvin(recebeValor(), unidadeFinal)
        case 'F':
            converterParaFahrenheit(recebeValor(), unidadeFinal)
        case _:
            print('VALOR INVÁLIDO!')

