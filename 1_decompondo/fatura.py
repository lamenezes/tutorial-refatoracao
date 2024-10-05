def fatura(demonstrativo, obras):
    valor_total = 0
    créditos = 0
    resultado = f"Recibo para {demonstrativo['cliente']}\n"

    def valor_da(performance, obra):
        resultado = 0
        if obra["tipo"] == "tragédia":
            resultado = 40_000
            if performance["espectadores"] > 30:
                resultado += 1000 * (performance["espectadores"] - 30)
        elif obra["tipo"] == "comédia":
            resultado = 30_000
            if performance["espectadores"] > 20:
                resultado += 10000 + 500 * (performance["espectadores"] - 20)
            resultado += 300 * performance["espectadores"]
        else:
            raise ValueError(f"Tipo de obra desconhecido {obra['tipo']}")

        return resultado

    for performance in demonstrativo["performances"]:
        obra = obras[performance["id_obra"]]

        # soma créditos por volume
        créditos += max(performance["espectadores"] - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if obra["tipo"] == "comédia":
            créditos += performance["espectadores"] // 5

        resultado += f"  {obra['nome']}: R$ {valor_da(performance, obra)/ 100:.2f} ({performance['espectadores']} lugares)\n"
        valor_total += valor_da(performance, obra)

    resultado += f"Valor a pagar é de R$ {valor_total / 100:.2f}\n"
    resultado += f"Você ganhou {créditos} créditos\n"
    return resultado
