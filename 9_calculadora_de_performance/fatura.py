from dataclasses import dataclass


@dataclass
class Fatura:
    cliente: str
    performances: list['Performance']

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
            resultado += performance.calcula_creditos()
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

    @classmethod
    def cria_varias(cls, dados_performances, obras):
        performances = []
        for dados in dados_performances:
            performance = cls(**dados, obra=obras[dados["id_obra"]])
            performances.append(performance)
        return performances

    def __post_init__(self):
        self.valor = CalculadoraPerformance(self).valor

    def calcula_creditos(self):
        resultado = max(self.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.obra["tipo"] == "comédia":
            resultado += self.espectadores // 5
        return resultado


class CalculadoraPerformance:
    def __init__(self, performance):
        self.performance = performance

    @property
    def valor(self):
        resultado = 0
        if self.performance.obra["tipo"] == "tragédia":
            resultado = 40_000
            if self.performance.espectadores > 30:
                resultado += 1000 * (self.performance.espectadores - 30)
        elif self.performance.obra["tipo"] == "comédia":
            resultado = 30_000
            if self.performance.espectadores > 20:
                resultado += 10000 + 500 * (self.performance.espectadores - 20)
            resultado += 300 * self.performance.espectadores
        else:
            raise ValueError(f"Tipo de obra desconhecido {self.performance.obra['tipo']}")

        return resultado

    @property
    def creditos(self):
        resultado = max(self.performance.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.performance.obra["tipo"] == "comédia":
            resultado += self.performance.espectadores // 5
        return resultado
