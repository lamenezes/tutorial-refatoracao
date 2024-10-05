from dataclasses import dataclass


def fatura(dados_demonstrativo, obras):
    fatura = Fatura(
        cliente=dados_demonstrativo["cliente"],
        performances=Performance.cria_varias(
            dados_demonstrativo["performances"], obras
        ),
    )
    return renderiza_texto_plano(fatura, obras)


def renderiza_texto_plano(fatura, obras):
    resultado = f"Recibo para {fatura.cliente}\n"

    for performance in fatura.performances:
        resultado += f"  {performance.obra['nome']}: {brl(performance.calcula_valor() / 100)} ({performance.espectadores} lugares)\n"

    resultado += f"Valor a pagar é de {brl(fatura.calcula_valor_total() / 100)}\n"
    resultado += f"Você ganhou {fatura.calcula_creditos()} créditos\n"
    return resultado


@dataclass
class Performance:
    id_obra: str
    espectadores: int
    obras: list[dict]

    @classmethod
    def cria_varias(cls, dados_performances, obras):
        performances = []
        for dados in dados_performances:
            performances.append(cls(**dados, obras=obras))
        return performances

    @property
    def obra(self):
        return self.obras[self.id_obra]

    def calcula_valor(self):
        resultado = 0
        if self.obra["tipo"] == "tragédia":
            resultado = 40_000
            if self.espectadores > 30:
                resultado += 1000 * (self.espectadores - 30)
        elif self.obra["tipo"] == "comédia":
            resultado = 30_000
            if self.espectadores > 20:
                resultado += 10000 + 500 * (self.espectadores - 20)
            resultado += 300 * self.espectadores
        else:
            raise ValueError(f"Tipo de obra desconhecido {self.obra['tipo']}")

        return resultado

    def calcula_creditos(self):
        resultado = max(self.espectadores - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if self.obra["tipo"] == "comédia":
            resultado += self.espectadores // 5
        return resultado


@dataclass
class Fatura:
    cliente: str
    performances: list[Performance]

    def calcula_creditos(self):
        resultado = 0
        for performance in self.performances:
            # soma créditos por volume
            resultado += performance.calcula_creditos()
        return resultado

    def calcula_valor_total(self):
        resultado = 0
        for performance in self.performances:
            resultado += performance.calcula_valor()
        return resultado


def brl(numero):
    return f"R$ {numero:.2f}"
