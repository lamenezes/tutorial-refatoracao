from dataclasses import dataclass


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


def cria_calculadora(performance):
    if performance.obra["tipo"] == "tragédia":
        return CalculadoraTragedia(performance)
    elif performance.obra["tipo"] == "comédia":
        return CalculadoraComedia(performance)
    raise ValueError(f"Tipo de obra desconhecido {performance.obra['tipo']}")


class CalculadoraPerformance:
    def __init__(self, performance):
        self.performance = performance
        self.valor = self.calcula_valor()
        self.creditos = self.calcula_creditos()

    def calcula_creditos(self):
        total_créditos = 0
        total_créditos += max(self.performance.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.performance.obra["tipo"] == "comédia":
            total_créditos += self.performance.espectadores // 5
        return total_créditos

    def calcula_valor(self):
        valor_atual = 0
        if self.performance.obra["tipo"] == "tragédia":
            valor_atual = 40_000
            if self.performance.espectadores > 30:
                valor_atual += 1000 * (self.performance.espectadores - 30)
        elif self.performance.obra["tipo"] == "comédia":
            valor_atual = 30_000
            if self.performance.espectadores > 20:
                valor_atual += 10000 + 500 * (self.performance.espectadores - 20)
            valor_atual += 300 * self.performance.espectadores
        else:
            raise ValueError(f"Tipo de obra desconhecido {self.performance.obra['tipo']}")
        return valor_atual


class CalculadoraComedia(CalculadoraPerformance):
    pass


class CalculadoraTragedia(CalculadoraPerformance):
    pass
