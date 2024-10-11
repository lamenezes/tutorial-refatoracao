from dataclasses import dataclass
from calculadora import cria_calculadora


@dataclass
class Fatura:
    cliente: str
    performances: list['Performance']

    def calcula_creditos_totais(self):
        total_créditos = 0
        for performance in self.performances:
            total_créditos += performance.creditos
        return total_créditos

    def calcula_valor_total(self):
        valor_total = 0
        for performance in self.performances:
            valor_total += performance.valor
        return valor_total


@dataclass
class Performance:
    espectadores: int
    obra: dict

    @classmethod
    def cria_varios(cls, dados, obras):
        performances = []
        for perf in dados["performances"]:
            performance = Performance(obra=obras[perf["id_obra"]], espectadores=perf["espectadores"])
            performances.append(performance)
        return performances

    def __post_init__(self):
        self.valor = cria_calculadora(self).valor
        self.creditos = cria_calculadora(self).creditos
