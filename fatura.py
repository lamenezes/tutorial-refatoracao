from dataclasses import dataclass


@dataclass
class Fatura:
    cliente: str
    performances: list['Performance']

    def calcula_creditos_totais(self):
        total_créditos = 0
        for performance in self.performances:
            total_créditos += performance.calcula_creditos()
        return total_créditos

    def calcula_valor_total(self):
        valor_total = 0
        for performance in self.performances:
            valor_total += performance.calcula_valor()
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

    def calcula_valor(self):
        valor_atual = 0
        if self.obra["tipo"] == "tragédia":
            valor_atual = 40_000
            if self.espectadores > 30:
                valor_atual += 1000 * (self.espectadores - 30)
        elif self.obra["tipo"] == "comédia":
            valor_atual = 30_000
            if self.espectadores > 20:
                valor_atual += 10000 + 500 * (self.espectadores - 20)
            valor_atual += 300 * self.espectadores
        else:
            raise ValueError(f"Tipo de obra desconhecido {self.obra['tipo']}")
        return valor_atual

    def calcula_creditos(self):
        total_créditos = 0
        # soma créditos por volume
        total_créditos += max(self.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.obra["tipo"] == "comédia":
            total_créditos += self.espectadores // 5
        return total_créditos
