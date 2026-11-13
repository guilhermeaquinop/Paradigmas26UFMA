Discente: Guilherme de Aquino Pacheco

Na P1 o código era feito com funções (converterParaCelsius, converterParaKelvin...) e uma estrutura de condição para escolher qual chamar. Agora cada escala virou uma classe.

A classe Escala é abstrata e obriga as filhas a terem os métodos para_celsius e de_celsius. As classes Celsius, Kelvin e Fahrenheit herdam dela:

    class Kelvin(Escala):
        simbolo = 'K'

        def para_celsius(self, valor):
            return valor - 273.15

        def de_celsius(self, valor):
            return valor + 273.15

A classe ConversorTemperatura guarda as escalas e faz a conversão sempre passando pelo Celsius (origem -> Celsius -> destino). Assim ela trata todas as escalas do mesmo jeito (polimorfismo) e, para adicionar uma escala nova, basta criar outra classe.

A classe Aplicacao cuida só da parte de entrada e saída (input e print), e recebe o conversor no construtor.

Também corrigi umas fórmulas da P1 que estavam trocadas (por exemplo, de Celsius para Kelvin estava subtraindo 273.15 em vez de somar).

Para rodar:

    python conversor_temperatura.py
