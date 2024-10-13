from fatura import Fatura, Performance


def gera_relatorio(dados_demonstrativo, obras, tipo_relatorio):
    fatura = Fatura(
        cliente=dados_demonstrativo["cliente"],
        performances=Performance.cria_varios(dados_demonstrativo, obras),
    )
    return renderiza_texto_plano(fatura)


def renderiza_texto_plano(fatura):
    resultado = f"Recibo para {fatura.cliente}\n"

    for performance in fatura.performances:
        resultado += f"  {performance.obra['nome']}: {formata_brl(performance.valor)} ({performance.espectadores} lugares)\n"

    resultado += f"Valor a pagar é de {formata_brl(fatura.calcula_valor_total())}\n"
    resultado += f"Você ganhou {fatura.calcula_creditos_totais()} créditos\n"
    return resultado


def gera_relatorio_fatura_html(dados_demonstrativo, obras):
    fatura = Fatura(
        cliente=dados_demonstrativo["cliente"],
        performances=Performance.cria_varios(dados_demonstrativo, obras),
    )
    return renderiza_html(fatura)


def renderiza_html(fatura):
    resultado = f"<h1>Recibo para {fatura.cliente}</h1>\n"
    resultado += "<table>\n"
    resultado += "<tr><th>obra</th><th>espectadores</th><th>valor</th></tr>\n"

    for performance in fatura.performances:
        resultado += f"<tr><td>{performance.obra['nome']}</td><td>{performance.espectadores}</td><td>{formata_brl(performance.valor)}</td></tr>\n"

    resultado += "</table>\n"
    resultado += (
        f"<p>Valor a pagar é de {formata_brl(fatura.calcula_valor_total())}</p>\n"
    )
    resultado += f"<p>Você ganhou {fatura.calcula_creditos_totais()} créditos</p>\n"
    return resultado


def formata_brl(valor):
    return f"R$ {valor / 100:.2f}"
