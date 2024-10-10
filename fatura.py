def fatura(dados_demonstrativo, obras):
    valor_total = 0
    total_créditos = 0
    resultado = f"Recibo para {dados_demonstrativo['cliente']}\n"

    for performance in dados_demonstrativo["performances"]:
        obra = obras[performance["id_obra"]]

        def calcula_valor(performance, obra):
            valor_atual = 0
            if obra["tipo"] == "tragédia":
                valor_atual = 40_000
                if performance["espectadores"] > 30:
                    valor_atual += 1000 * (performance["espectadores"] - 30)
            elif obra["tipo"] == "comédia":
                valor_atual = 30_000
                if performance["espectadores"] > 20:
                    valor_atual += 10000 + 500 * (performance["espectadores"] - 20)
                valor_atual += 300 * performance["espectadores"]
            else:
                raise ValueError(f"Tipo de obra desconhecido {obra['tipo']}")
            return valor_atual

        # soma créditos por volume
        total_créditos += max(performance["espectadores"] - 30, 0)
        # soma um crédito extra para cada dez espectadores de comédia
        if obra["tipo"] == "comédia":
            total_créditos += performance["espectadores"] // 5

        valor_atual = calcula_valor(performance, obra)
        resultado += f"  {obra['nome']}: R$ {valor_atual / 100:.2f} ({performance['espectadores']} lugares)\n"
        valor_total += valor_atual

    resultado += f"Valor a pagar é de R$ {valor_total / 100:.2f}\n"
    resultado += f"Você ganhou {total_créditos} créditos\n"
    return resultado
