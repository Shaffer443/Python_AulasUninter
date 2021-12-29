# Acesso aos Dados.

import pandas

# Carregando dados. QUe podem ser de um endereço local ou um html. sempre entre aspas. e .arquivo(csv,xlsx, outros)
# Pegar dados com permissão de acesso ou o mais bruto.
dadosprincipal = pandas.read_csv('https://raw.githubusercontent.com/leonhgomes/Pandas/main/pokemon_data.csv')

# print(dadosprincipal.columns) # print apenas das colunas do arquivo.

# print(dadosprincipal.head)
# Carrega as informações totais do arquivo.

# print(dadosprincipal.head(3)) # quantidade de linhas iniciais (3) + todas as colunas

# Pode-se passar uma quantidade de linhas para abrir do arquivo, caso seja estenso em númeor de linhas e colunas.

# print(dadosprincipal.tail(3)) # quantidade de linhas Finais (3) + todas as colunas

# Acessando Colunas Individuais:

# print(dadosprincipal['Nome']) # mostra apenas a coluna 'Nome' do arquivo.

# print(dadosprincipal[['Nome','Tipo 1']]) # mostra mais de uma coluna. 'Nome' e 'Tipo1' do arquivo.
# OBS: Tive que usar um colchete para cada coluna que quis mostrar. Ou seja, Duas.

# Acessando Colunas e linhas específicas:

# print(dadosprincipal[['Nome', 'Tipo 1']][5:10]) # Coluna 'NOME" + 'TIPO 1', da linha 5 a 9
# print(dadosprincipal[['Nome', 'Tipo 1']][5:250:5]) # Coluna 'NOME" + 'TIPO 1', da linha 5 a 249, pulando de 2 em 2

# Acessando linhas específicas:

# print(dadosprincipal.iloc[:4]) # localizar da início até a linha 4.

# Acessando linhas e colunas específicas:

# print(dadosprincipal.iloc[2,1]) # localizar da Linha: 2, Coluna: 1.

# Busca por Nome, ou outro reconhecimento:

# print(dadosprincipal.loc[dadosprincipal['Tipo 1'] == 'Fogo']) # localizar da Linha: 2, Coluna: 1.

# Acessar Linha por Nome:

# indice e linha foi nomeado ao meu gosto.
# iterrows - Gera uma lista de linhas, interação pelas linhas do arquivo
#for indice, linha in dadosprincipal.iterrows():
#    print(indice, linha['Nome']) # coluna alvo para retorno do s dados.
#    if linha['#'] == 150: # uma marcação, coluna contida na planilha, pdoeria ser qualquer outra referencia ao meu gosto.
#        break               # usar [] para delimitar paramentros em um arquivo

# Programação retornará o itens de da coluna NOME até a macação númerica, contida na planilha, de 150. e vai parar.

# Valores Estatisticos Básicos:

# print(dadosprincipal.describe())

# Ordenação de Dados:

#print(dadosprincipal.sort_values('Nome'))
# Organizado de forma ascendente (a-z)
# nomedavariavel.sort_values('coluna para organização dentrod o arquivo')

print(dadosprincipal.sort_values('Nome',ascending=False))
# Organizado de forma descendente (Z-A)
# "F" maiúsculo.