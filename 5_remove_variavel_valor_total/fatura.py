def fatura(dados_demonstrativo, obras):
    resultado = f"Recibo para {dados_demonstrativo['cliente']}\n"

    def obra_da(performance):
        return obras[performance["id_obra"]]

    def calcula_valor(performance):
        resultado = 0
        if obra_da(performance)["tipo"] == "tragédia":
            resultado = 40_000
            if performance["espectadores"] > 30:
                resultado += 1000 * (performance["espectadores"] - 30)
        elif obra_da(performance)["tipo"] == "comédia":
            resultado = 30_000
            if performance["espectadores"] > 20:
                resultado += 10000 + 500 * (performance["espectadores"] - 20)
            resultado += 300 * performance["espectadores"]
        else:
            raise ValueError(
                f"Tipo de obra desconhecido {obra_da(performance)['tipo']}"
            )

        return resultado

    def creditos_da(performance):
        resultado = max(performance["espectadores"] - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if obra_da(performance)["tipo"] == "comédia":
            resultado += performance["espectadores"] // 5
        return resultado

    def creditos_totais(performances):
        resultado = 0
        for performance in performances:
            # soma créditos por volume
            resultado += creditos_da(performance)
        return resultado

    def valor_total(performances):
        resultado = 0
        for performance in performances:
            resultado += calcula_valor(performance)
        return resultado

    for performance in dados_demonstrativo["performances"]:
        resultado += f"  {obra_da(performance)['nome']}: {brl(calcula_valor(performance) / 100)} ({performance['espectadores']} lugares)\n"

    valor_total = valor_total(dados_demonstrativo["performances"])
    resultado += f"Valor a pagar é de {brl(valor_total / 100)}\n"
    resultado += (
        f"Você ganhou {creditos_totais(dados_demonstrativo['performances'])} créditos\n"
    )
    return resultado


def brl(numero):
    return f"R$ {numero:.2f}"
