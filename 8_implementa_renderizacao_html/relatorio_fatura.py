from fatura import Fatura, Performance


def gera_relatorio_fatura(dados_demonstrativo, obras):
    fatura = Fatura(
        cliente=dados_demonstrativo["cliente"],
        performances=Performance.cria_varias(
            dados_demonstrativo["performances"], obras
        ),
    )
    return renderiza_texto_plano(fatura, obras)


def renderiza_texto_plano(fatura, obras):
    resultado = f"Recibo para {fatura.cliente}\n"

    for performance in fatura.performances:
        resultado += f"  {performance.obra['nome']}: {brl(performance.calcula_valor() / 100)} ({performance.espectadores} lugares)\n"

    resultado += f"Valor a pagar é de {brl(fatura.calcula_valor_total() / 100)}\n"
    resultado += f"Você ganhou {fatura.calcula_creditos()} créditos\n"
    return resultado



def brl(numero):
    return f"R$ {numero:.2f}"
