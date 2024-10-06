from fatura import fatura

OBRAS = {
    "hamlet": {"nome": "Hamlet", "tipo": "tragédia"},
    "sonho-verão": {"nome": "Sonho de uma noite de verão", "tipo": "comédia"},
    "otelo": {"nome": "Otelo", "tipo": "tragédia"},
}


def test_fatura():
    perf = {
        "cliente": "Clientíssimo",
        "performances": [
            {"id_obra": "hamlet", "espectadores": 81},
            {"id_obra": "sonho-verão", "espectadores": 52},
            {"id_obra": "hamlet", "espectadores": 63},
        ],
    }

    assert fatura(perf, OBRAS) == (
        "Recibo para Clientíssimo\n"
        "  Hamlet: R$ 910.00 (81 lugares)\n"
        "  Sonho de uma noite de verão: R$ 716.00 (52 lugares)\n"
        "  Hamlet: R$ 730.00 (63 lugares)\n"
        "Valor a pagar é de R$ 2356.00\n"
        "Você ganhou 116 créditos\n"
    )


def test_fatura_lendo_arquivo():
    import json

    dados_demonstrativo = json.load(open("demonstrativo.json"))
    obras = json.load(open("obras.json"))

    assert fatura(dados_demonstrativo[0], obras) == (
        "Recibo para Empresão\n"
        "  Hamlet: R$ 650.00 (55 lugares)\n"
        "  Sonho de uma noite de verão: R$ 580.00 (35 lugares)\n"
        "  Otelo: R$ 500.00 (40 lugares)\n"
        "Valor a pagar é de R$ 1730.00\n"
        "Você ganhou 47 créditos\n"
    )
