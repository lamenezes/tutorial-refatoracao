from relatorio_fatura import gera_relatorio_fatura, gera_relatorio_fatura_html

OBRAS = {
    "hamlet": {"nome": "Hamlet", "tipo": "tragédia"},
    "sonho-verão": {"nome": "Sonho de uma noite de verão", "tipo": "comédia"},
    "otelo": {"nome": "Otelo", "tipo": "tragédia"},
}


def test_gera_relatorio_fatura():
    perf = {
        "cliente": "Clientíssimo",
        "performances": [
            {"id_obra": "hamlet", "espectadores": 81},
            {"id_obra": "sonho-verão", "espectadores": 52},
            {"id_obra": "hamlet", "espectadores": 63},
        ],
    }

    assert gera_relatorio_fatura(perf, OBRAS) == (
        "Recibo para Clientíssimo\n"
        "  Hamlet: R$ 910.00 (81 lugares)\n"
        "  Sonho de uma noite de verão: R$ 716.00 (52 lugares)\n"
        "  Hamlet: R$ 730.00 (63 lugares)\n"
        "Valor a pagar é de R$ 2356.00\n"
        "Você ganhou 116 créditos\n"
    )


def test_gera_relatorio_fatura_html():
    perf = {
        "cliente": "Clientíssimo",
        "performances": [
            {"id_obra": "hamlet", "espectadores": 81},
            {"id_obra": "sonho-verão", "espectadores": 52},
            {"id_obra": "hamlet", "espectadores": 63},
        ],
    }

    assert gera_relatorio_fatura_html(perf, OBRAS) == (
        "<h1>Recibo para Clientíssimo</h1>\n"
        "<table>\n"
        "<tr><th>obra</th><th>espectadores</th><th>valor</th>\n"
        "<tr><td>Hamlet</td><td>81</td><td>R$ 910.00</td></tr>\n"
        "<tr><td>Sonho de uma noite de verão</td><td>52</td><td>R$ 716.00</td></tr>\n"
        "<tr><td>Hamlet</td><td>63</td><td>R$ 730.00</td></tr>\n"
        "</table>\n"
        "<p>Valor a pagar é de R$ 2356.00</p>\n"
        "<p>Você ganhou 116 créditos</p>\n"
    )


def test_gera_relatorio_fatura_do_arquivo():
    import json

    performances = json.load(open("demonstrativo.json"))
    obras = json.load(open("obras.json"))

    assert gera_relatorio_fatura(performances[0], obras) == (
        "Recibo para Empresão\n"
        "  Hamlet: R$ 650.00 (55 lugares)\n"
        "  Sonho de uma noite de verão: R$ 580.00 (35 lugares)\n"
        "  Otelo: R$ 500.00 (40 lugares)\n"
        "Valor a pagar é de R$ 1730.00\n"
        "Você ganhou 47 créditos\n"
    )
