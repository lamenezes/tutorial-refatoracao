from dataclasses import dataclass


def fatura(dados_demonstrativo, obras):
    performances = []
    for perf in dados_demonstrativo["performances"]:
        performance = Performance(obra=obras[perf["id_obra"]], espectadores=perf["espectadores"])
        performances.append(performance)

    fatura = Fatura(
        cliente=dados_demonstrativo["cliente"],
        performances=performances,
    )
    return renderiza_texto_plano(fatura, obras)


def renderiza_texto_plano(fatura, obras):
    resultado = f"Recibo para {fatura.cliente}\n"

    for performance in fatura.performances:
        valor_atual = calcula_valor(performance)
        resultado += f"  {performance.obra['nome']}: {formata_brl(valor_atual)} ({performance.espectadores} lugares)\n"

    resultado += f"Valor a pagar é de {formata_brl(calcula_valor_total(fatura))}\n"
    resultado += f"Você ganhou {calcula_creditos_totais(fatura)} créditos\n"
    return resultado


@dataclass
class Fatura:
    cliente: str
    performances: list['Performance']


@dataclass
class Performance:
    espectadores: int
    obra: dict


def calcula_creditos_totais(fatura):
    total_créditos = 0
    for performance in fatura.performances:
        total_créditos += calcula_creditos(performance)
    return total_créditos


def calcula_valor_total(fatura):
    valor_total = 0
    for performance in fatura.performances:
        valor_total += calcula_valor(performance)
    return valor_total


def calcula_valor(performance):
    valor_atual = 0
    if performance.obra["tipo"] == "tragédia":
        valor_atual = 40_000
        if performance.espectadores > 30:
            valor_atual += 1000 * (performance.espectadores - 30)
    elif performance.obra["tipo"] == "comédia":
        valor_atual = 30_000
        if performance.espectadores > 20:
            valor_atual += 10000 + 500 * (performance.espectadores - 20)
        valor_atual += 300 * performance.espectadores
    else:
        raise ValueError(f"Tipo de obra desconhecido {performance.obra['tipo']}")
    return valor_atual


def calcula_creditos(performance):
    total_créditos = 0
    # soma créditos por volume
    total_créditos += max(performance.espectadores - 30, 0)
    # soma um crédito extra para cada dez espectadores de comédia
    if performance.obra["tipo"] == "comédia":
        total_créditos += performance.espectadores // 5
    return total_créditos


def formata_brl(valor):
    return f"R$ {valor / 100:.2f}"
