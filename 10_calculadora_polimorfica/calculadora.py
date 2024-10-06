def cria_calculadora_performance(performance):
    if performance.obra["tipo"] == "comédia":
        return CalculadoraComedia(performance)
    if performance.obra["tipo"] == "tragédia":
        return CalculadoraTragedia(performance)
    return CalculadoraPerformance(performance)


class CalculadoraPerformance:
    def __init__(self, performance):
        self.performance = performance

    @property
    def valor(self):
        return NotImplementedError()

    @property
    def creditos(self):
        resultado = max(self.performance.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.performance.obra["tipo"] == "comédia":
            resultado += self.performance.espectadores // 5
        return resultado


class CalculadoraComedia(CalculadoraPerformance):
    @property
    def valor(self):
        resultado = 30_000
        if self.performance.espectadores > 20:
            resultado += 10000 + 500 * (self.performance.espectadores - 20)
        resultado += 300 * self.performance.espectadores
        return resultado


class CalculadoraTragedia(CalculadoraPerformance):
    @property
    def valor(self):
        resultado = 40_000
        if self.performance.espectadores > 30:
            resultado += 1000 * (self.performance.espectadores - 30)
        return resultado
