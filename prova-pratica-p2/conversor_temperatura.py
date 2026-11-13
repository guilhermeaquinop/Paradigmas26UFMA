from abc import ABC, abstractmethod


class Escala(ABC):
    simbolo = ''

    @abstractmethod
    def para_celsius(self, valor):
        pass

    @abstractmethod
    def de_celsius(self, valor):
        pass


class Celsius(Escala):
    simbolo = '°C'

    def para_celsius(self, valor):
        return valor

    def de_celsius(self, valor):
        return valor


class Kelvin(Escala):
    simbolo = 'K'

    def para_celsius(self, valor):
        return valor - 273.15

    def de_celsius(self, valor):
        return valor + 273.15


class Fahrenheit(Escala):
    simbolo = '°F'

    def para_celsius(self, valor):
        return (valor - 32) * 5 / 9

    def de_celsius(self, valor):
        return valor * 9 / 5 + 32


class ConversorTemperatura:

    def __init__(self):
        self._escalas = {'C': Celsius(), 'K': Kelvin(), 'F': Fahrenheit()}

    def escala(self, sigla):
        if sigla not in self._escalas:
            raise ValueError('UNIDADE INVÁLIDA!')
        return self._escalas[sigla]

    def converter(self, valor, origem, destino):
        celsius = self.escala(origem).para_celsius(valor)
        return self.escala(destino).de_celsius(celsius)


class Aplicacao:
    def __init__(self, conversor):
        self._conversor = conversor

    def executar(self):
        origem = input('QUAL UNIDADE DA TEMPERATURA DESEJA CONVERTER (C/K/F) ?').upper()
        destino = input('PARA QUAL UNIDADE DA TEMPERATURA DESEJA CONVERTER (C/K/F) ?').upper()
        try:
            escala_destino = self._conversor.escala(destino)
            self._conversor.escala(origem)
            valor = float(input('QUAL O VALOR A SER CONVERTIDO ?'))
        except ValueError as erro:
            print(erro if str(erro).startswith('UNIDADE') else 'VALOR INVÁLIDO!')
            return
        resultado = self._conversor.converter(valor, origem, destino)
        print(f'{resultado}{escala_destino.simbolo}')


if __name__ == '__main__':
    Aplicacao(ConversorTemperatura()).executar()
