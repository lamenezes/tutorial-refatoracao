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
        return max(self.performance.espectadores - 30, 0)


class CalculadoraComedia(CalculadoraPerformance):
    def calcula_valor(self):
        valor_atual = 30_000
        if self.performance.espectadores > 20:
            valor_atual += 10000 + 500 * (self.performance.espectadores - 20)
        valor_atual += 300 * self.performance.espectadores
        return valor_atual

    def calcula_creditos(self):
        # soma um crédito extra para cada dez espectadores de comédia
        total_creditos = super().calcula_creditos()
        total_creditos += self.performance.espectadores // 5
        return total_creditos


class CalculadoraTragedia(CalculadoraPerformance):
    def calcula_valor(self):
        valor_atual = 40_000
        if self.performance.espectadores > 30:
            valor_atual += 1000 * (self.performance.espectadores - 30)
        return valor_atual
