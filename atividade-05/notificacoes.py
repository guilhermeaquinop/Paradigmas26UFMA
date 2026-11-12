# Atividade 05 - Central de Notificacoes (Paradigma Orientado a Objetos)

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, destino, mensagem):
        self.destino = destino
        self.mensagem = mensagem

    # Template Method
    def enviar(self):
        print(f"[{self.canal()}] para {self.destino}: {self.mensagem}")

    @abstractmethod
    def canal(self):
        pass


# Interface (em Python, classe abstrata sem estado)
class Agendavel(ABC):
    @abstractmethod
    def horario(self):
        pass

    # default method
    def agendamento(self):
        if self.horario() is None:
            return "imediato"
        return f"agendado para {self.horario()}"


class Email(Notificacao, Agendavel):
    def __init__(self, destino, mensagem, horario):
        super().__init__(destino, mensagem)
        self._horario = horario

    def canal(self):
        return "E-MAIL"

    def horario(self):
        return self._horario


class Sms(Notificacao):
    def canal(self):
        return "SMS"


class Push(Notificacao, Agendavel):
    def canal(self):
        return "PUSH"

    def horario(self):
        return None


class CentralNotificacoes:
    def __init__(self):
        self.notificacoes = []

    def adicionar(self, notificacao):
        self.notificacoes.append(notificacao)

    def disparar(self):
        for n in self.notificacoes:
            n.enviar()  # polimorfismo
            if isinstance(n, Agendavel):
                print(f"  {n.agendamento()}")


# --- programa principal ---

mensagem = "Reunião do squad hoje às 19h!"

central = CentralNotificacoes()
central.adicionar(Email("ana@undb.edu.br", mensagem, "08:00"))
central.adicionar(Sms("98 99999-0000", mensagem))
central.adicionar(Push("app-joao", mensagem))

central.disparar()
