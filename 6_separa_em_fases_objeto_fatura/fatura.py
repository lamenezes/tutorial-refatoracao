from dataclasses import dataclass


def fatura(dados_demonstrativo, obras):
    fatura = Fatura(
        cliente=dados_demonstrativo["cliente"],
        performances=dados_demonstrativo["performances"],
    )
    return renderiza_texto_plano(fatura, obras)


def renderiza_texto_plano(fatura, obras):
    resultado = f"Recibo para {fatura.cliente}\n"

    for performance in fatura.performances:
        performance["obra"] = obras[performance["id_obra"]]
        resultado += f"  {performance['obra']['nome']}: {brl(calcula_valor(performance) / 100)} ({performance['espectadores']} lugares)\n"

    resultado += f"Valor a pagar é de {brl(calcula_valor_total(fatura) / 100)}\n"
    resultado += f"Você ganhou {calcula_creditos_totais(fatura)} créditos\n"
    return resultado


def calcula_valor(performance):
    resultado = 0
    if performance["obra"]["tipo"] == "tragédia":
        resultado = 40_000
        if performance["espectadores"] > 30:
            resultado += 1000 * (performance["espectadores"] - 30)
    elif performance["obra"]["tipo"] == "comédia":
        resultado = 30_000
        if performance["espectadores"] > 20:
            resultado += 10000 + 500 * (performance["espectadores"] - 20)
        resultado += 300 * performance["espectadores"]
    else:
        raise ValueError(
            f"Tipo de obra desconhecido {performance['obra']['tipo']}"
        )

    return resultado


def calcula_creditos(performance):
    resultado = max(performance["espectadores"] - 30, 0)
    # soma um crédito extra para cada dez espectadores de comédia
    if performance["obra"]["tipo"] == "comédia":
        resultado += performance["espectadores"] // 5
    return resultado


def calcula_creditos_totais(fatura):
    resultado = 0
    for performance in fatura.performances:
        # soma créditos por volume
        resultado += calcula_creditos(performance)
    return resultado


def calcula_valor_total(fatura):
    resultado = 0
    for performance in fatura.performances:
        resultado += calcula_valor(performance)
    return resultado


@dataclass
class Fatura:
    cliente: str
    performances: list[dict]


def brl(numero):
    return f"R$ {numero:.2f}"
