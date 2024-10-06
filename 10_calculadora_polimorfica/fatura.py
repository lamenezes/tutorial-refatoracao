from dataclasses import dataclass
from calculadora import CalculadoraPerformance


@dataclass
class Fatura:
    cliente: str
    performances: list["Performance"]

    @classmethod
    def cria(cls, dados, obras):
        return cls(
            cliente=dados["cliente"],
            performances=Performance.cria_varias(dados["performances"], obras),
        )

    def calcula_creditos(self):
        resultado = 0
        for performance in self.performances:
            # soma créditos por volume
            resultado += performance.creditos
        return resultado

    def calcula_valor_total(self):
        resultado = 0
        for performance in self.performances:
            resultado += performance.valor
        return resultado


@dataclass
class Performance:
    id_obra: str
    espectadores: int
    obra: dict
    valor: int = None
    creditos: int = None

    @classmethod
    def cria_varias(cls, dados_performances, obras):
        performances = []
        for dados in dados_performances:
            performance = cls(**dados, obra=obras[dados["id_obra"]])
            performances.append(performance)
        return performances

    def __post_init__(self):
        calculadora = CalculadoraPerformance(self)
        self.valor = calculadora.valor
        self.creditos = calculadora.creditos
