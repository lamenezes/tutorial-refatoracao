testall:
	pytest test_fatura.py
	pytest 1_decompondo/test_fatura.py
	pytest 2_removendo_obra/test_fatura.py
	pytest 3_extrai_creditos/test_fatura.py
