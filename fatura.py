def fatura(dados_demonstrativo, obras):
    resultado = f"Recibo para {dados_demonstrativo['cliente']}\n"

    for performance in dados_demonstrativo["performances"]:
        performance["obra"] = obras[performance["id_obra"]]
        valor_atual = calcula_valor(performance)
        resultado += f"  {performance['obra']['nome']}: {formata_brl(valor_atual)} ({performance['espectadores']} lugares)\n"

    resultado += f"Valor a pagar é de {formata_brl(calcula_valor_total(dados_demonstrativo))}\n"
    resultado += f"Você ganhou {calcula_creditos_totais(dados_demonstrativo)} créditos\n"
    return resultado


def calcula_creditos_totais(dados_demonstrativo):
    total_créditos = 0
    for performance in dados_demonstrativo["performances"]:
        total_créditos += calcula_creditos(performance)
    return total_créditos


def calcula_valor_total(dados_demonstrativo):
    valor_total = 0
    for performance in dados_demonstrativo["performances"]:
        valor_total += calcula_valor(performance)
    return valor_total


def calcula_valor(performance):
    valor_atual = 0
    if performance["obra"]["tipo"] == "tragédia":
        valor_atual = 40_000
        if performance["espectadores"] > 30:
            valor_atual += 1000 * (performance["espectadores"] - 30)
    elif performance["obra"]["tipo"] == "comédia":
        valor_atual = 30_000
        if performance["espectadores"] > 20:
            valor_atual += 10000 + 500 * (performance["espectadores"] - 20)
        valor_atual += 300 * performance["espectadores"]
    else:
        raise ValueError(f"Tipo de obra desconhecido {performance['obra']['tipo']}")
    return valor_atual


def calcula_creditos(performance):
    total_créditos = 0
    # soma créditos por volume
    total_créditos += max(performance["espectadores"] - 30, 0)
    # soma um crédito extra para cada dez espectadores de comédia
    if performance["obra"]["tipo"] == "comédia":
        total_créditos += performance["espectadores"] // 5
    return total_créditos


def formata_brl(valor):
    return f"R$ {valor / 100:.2f}"
