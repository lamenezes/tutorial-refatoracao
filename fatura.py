def gera_fatura(performance, obras):
    valor_total = 0
    créditos = 0
    resultado = f"Recibo para {performance['cliente']}\n"

    for performance in performance["performances"]:
        peça = obras[performance["id_obra"]]
        valor_atual = 0

        if peça["tipo"] == "tragédia":
            valor_atual = 40_000
            if performance["espectadores"] > 30:
                valor_atual += 1000 * (performance["espectadores"] - 30)
        elif peça["tipo"] == "comédia":
            valor_atual = 30_000
            if performance["espectadores"] > 20:
                valor_atual += 10000 + 500 * (performance["espectadores"] - 20)
            valor_atual += 300 * performance["espectadores"]
        else:
            raise ValueError(f"Tipo de peça desconhecido {peça['tipo']}")

        # soma créditos por volume
        créditos += max(performance["espectadores"] - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if peça["tipo"] == "comédia":
            créditos += performance["espectadores"] // 5

        resultado += f"  {peça['nome']}: R$ {valor_atual / 100:.2f} ({performance['espectadores']} lugares)\n"
        valor_total += valor_atual

    resultado += f"Valor a pagar é de R$ {valor_total / 100:.2f}\n"
    resultado += f"Você ganhou {créditos} créditos\n"
    return resultado
