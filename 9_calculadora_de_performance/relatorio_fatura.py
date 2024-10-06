from fatura import Fatura, Performance


def gera_relatorio_fatura(dados_demonstrativo, obras):
    fatura = Fatura.cria(dados_demonstrativo, obras)
    return renderiza_texto_plano(fatura, obras)


def renderiza_texto_plano(fatura, obras):
    resultado = f"Recibo para {fatura.cliente}\n"

    for performance in fatura.performances:
        resultado += f"  {performance.obra['nome']}: {brl(performance.valor / 100)} ({performance.espectadores} lugares)\n"

    resultado += f"Valor a pagar é de {brl(fatura.calcula_valor_total() / 100)}\n"
    resultado += f"Você ganhou {fatura.calcula_creditos()} créditos\n"
    return resultado


def gera_relatorio_fatura_html(dados_demonstrativo, obras):
    fatura = Fatura.cria(dados_demonstrativo, obras)
    return renderiza_texto_html(fatura, obras)


def renderiza_texto_html(fatura, obras):
    resultado = f"<h1>Recibo para {fatura.cliente}</h1>\n"
    resultado += "<table>\n"
    resultado += "<tr><th>obra</th><th>espectadores</th><th>valor</th>\n"

    for performance in fatura.performances:
        resultado += f"<tr><td>{performance.obra['nome']}</td>"
        resultado += f"<td>{performance.espectadores}</td><td>{brl(performance.valor / 100)}</td></tr>\n"

    resultado += "</table>\n"
    resultado += f"<p>Valor a pagar é de {brl(fatura.calcula_valor_total() / 100)}</p>\n"
    resultado += f"<p>Você ganhou {fatura.calcula_creditos()} créditos</p>\n"
    return resultado



def brl(numero):
    return f"R$ {numero:.2f}"
