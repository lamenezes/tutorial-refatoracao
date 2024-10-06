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
            raise ValueError(
                f"Tipo de obra desconhecido {self.performance.obra['tipo']}"
            )

        return resultado

    @property
    def creditos(self):
        resultado = max(self.performance.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.performance.obra["tipo"] == "comédia":
            resultado += self.performance.espectadores // 5
        return resultado
