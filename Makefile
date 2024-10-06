test:
	pytest test_fatura.py
	pytest 01_decompondo/test_fatura.py
	pytest 02_removendo_obra/test_fatura.py
	pytest 03_extrai_creditos/test_fatura.py
	pytest 04_remove_variavel_creditos/test_fatura.py
	pytest 05_remove_variavel_valor_total/test_fatura.py
	pytest 06_separa_em_fases_objeto_fatura/test_fatura.py
	pytest 07_separa_em_fases_objeto_performance/test_fatura.py
	pytest 08_implementa_renderizacao_html/test_fatura.py
	pytest 09_calculadora_de_performance/test_fatura.py
	pytest 10_calculadora_polimorfica/test_fatura.py

lint:
	ruff check . --fix
	black .

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" | xargs rm -rf
	find . -name ".pytest-cache" | xargs rm -rf
