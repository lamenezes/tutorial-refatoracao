test:
	pytest test_fatura.py
	pytest 1_decompondo/test_fatura.py
	pytest 2_removendo_obra/test_fatura.py
	pytest 3_extrai_creditos/test_fatura.py
	pytest 4_remove_variavel_creditos/test_fatura.py
	pytest 5_remove_variavel_valor_total/test_fatura.py

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" | xargs rm -rf
	find . -name ".pytest-cache" | xargs rm -rf
