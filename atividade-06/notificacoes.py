# Atividade 06 - Laboratorio: Central de Notificacoes (POO com ABC)

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def enviar(self, msg):
        pass

    def cabecalho(self):
        return f"[{self.tipo()}] para {self.destinatario}"


# Interface (classe abstrata sem estado)
class Agendavel(ABC):
    @abstractmethod
    def agendar_para(self, h):
        pass

    @abstractmethod
    def horario_agendado(self):
        pass

    # default method
    def resumo_agendamento(self):
        h = self.horario_agendado()
        return f"agendado para {h}" if h else "sem agendamento"


class EmailNotificacao(Notificacao, Agendavel):
    def __init__(self, destinatario):
        super().__init__(destinatario)
        self._horario = None

    def tipo(self):
        return "E-MAIL"

    def enviar(self, msg):
        print(f"{self.cabecalho()}: {msg}")

    def agendar_para(self, h):
        self._horario = h

    def horario_agendado(self):
        return self._horario


class SmsNotificacao(Notificacao):
    def tipo(self):
        return "SMS"

    def enviar(self, msg):
        print(f"{self.cabecalho()}: {msg[:160]}")


class PushNotificacao(Notificacao, Agendavel):
    def __init__(self, destinatario):
        super().__init__(destinatario)
        self._horario = None

    def tipo(self):
        return "PUSH"

    def enviar(self, msg):
        print(f"{self.cabecalho()}: {msg}")

    def agendar_para(self, h):
        self._horario = h

    def horario_agendado(self):
        return self._horario


# --- programa principal ---

msg = "Reunião do squad hoje às 19h!"

notificacoes = [
    EmailNotificacao("ana@undb.edu.br"),
    SmsNotificacao("98 99999-0000"),
    PushNotificacao("app-joao"),
]

for n in notificacoes:
    if isinstance(n, Agendavel):
        n.agendar_para("08:00")
    n.enviar(msg)
    if isinstance(n, Agendavel):
        print(f"  {n.resumo_agendamento()}")
