import datetime

ano = 2025

def gerar_tabela_sabados(ano):
  """
  Gera uma tabela com todos os sábados do ano especificado, formatados como dd/mm/aaaa e divididos em grupos.

  Args:
    ano: O ano para o qual gerar a tabela.
  """

  data = datetime.date(ano, 1, 1)
  # Encontra o primeiro sábado do ano
  while data.weekday() != 5:
    data += datetime.timedelta(days=1)

  grupo = 1
  titulo = f"Escala de Limpeza - Sábados de {ano}:"
  contagem_titulo = len(titulo)
  print(titulo)
  
  print("-" * contagem_titulo)
  while data.year == ano:
    print(data.strftime("%d/%m/%Y"))
    print(f"Grupo {grupo}\n")
    data += datetime.timedelta(days=7)
    grupo = grupo % 3 + 1  # Alterna entre os grupos 1, 2 e 3

gerar_tabela_sabados(ano)

"""

Se você quiser gerar tabelas com anos diferentes basta alterar a variável ano
Pode-se alterar também o número de grupos alterando também o valor da variável grupo.

"""
