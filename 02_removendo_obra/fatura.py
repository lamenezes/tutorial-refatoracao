def gera_fatura(dados_demonstrativo, obras):
    valor_total = 0
    total_creditos = 0
    resultado = f"Recibo para {dados_demonstrativo['cliente']}\n"

    for performance in dados_demonstrativo["performances"]:
        performance["obra"] = obras[performance["id_obra"]]
        # soma créditos por volume
        total_creditos += max(performance["espectadores"] - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if performance["obra"]["tipo"] == "comédia":
            total_creditos += performance["espectadores"] // 5

        resultado += f"  {performance['obra']['nome']}: R$ {calcula_valor(performance) / 100:.2f} ({performance['espectadores']} lugares)\n"
        valor_total += calcula_valor(performance)

    resultado += f"Valor a pagar é de R$ {valor_total / 100:.2f}\n"
    resultado += f"Você ganhou {total_creditos} créditos\n"
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
        raise ValueError(f"Tipo de obra desconhecido {performance['obra']['tipo']}")

    return resultado
