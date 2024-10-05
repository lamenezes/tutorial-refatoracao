def fatura(dados_demonstrativo, obras):
    valor_total = 0
    total_créditos = 0
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

    for performance in dados_demonstrativo["performances"]:
        # soma créditos por volume
        total_créditos += creditos_da(performance)
        resultado += f"  {obra_da(performance)['nome']}: {brl(calcula_valor(performance) / 100)} ({performance['espectadores']} lugares)\n"
        valor_total += calcula_valor(performance)

    resultado += f"Valor a pagar é de {brl(valor_total / 100)}\n"
    resultado += f"Você ganhou {total_créditos} créditos\n"
    return resultado


def brl(numero):
    return f"R$ {numero:.2f}"
