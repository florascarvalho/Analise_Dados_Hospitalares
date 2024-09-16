# %% [markdown]
# # Módulo 1: Análise exploratória de dados

# %% [markdown]
# ## Importando dados de Atendimento
# #### Etapas realizadas:
# 
# - Importada a biblioteca "PANDAS";
# - Realizada a leitura do arquido utilizando o "pd.read_csv";
# - Colar o caminho do arquivo (que deve ter sido previamente carregado);
# - Utilizar o "encoding" para dizer qual o formato do arquivo (Ex.: UTF-8, ISO-8859-1);
# - Utilizar o "skiprows" para indicar quantas linhas devem ser puladas para iniciar a leitura do código;
# - Utilizar "sep" para idicar qual o separador de dados está sendo utilizado (Ex.: vírgula, ponto e vírgula...);
# - Utilizar o "skipfooter" para indicar quantas linhas devem ser puladas no final;
# - Utilizar o "thousands" para idicar qual o separador de milhar está sendo utilizado no arquivo (se é vírgula ou ponto);
# - Utilizar o "decimal" para indicar o separador de casas decimai utilizado no arquivo (se ponto ou vírgula).

# %% [markdown]
# ## Importando dados de Atendimento
# #### Etapas realizadas:
# 
# - Importada a biblioteca "PANDAS";
# - Realizada a leitura do arquido utilizando o "pd.read_csv";
# - Colar o caminho do arquivo (que deve ter sido previamente carregado);
# - Utilizar o "encoding" para dizer qual o formato do arquivo (Ex.: UTF-8, ISO-8859-1);
# - Utilizar o "skiprows" para indicar quantas linhas devem ser puladas para iniciar a leitura do código;
# - Utilizar "sep" para idicar qual o separador de dados está sendo utilizado (Ex.: vírgula, ponto e vírgula...);
# - Utilizar o "skipfooter" para indicar quantas linhas devem ser puladas no final;
# - Utilizar o "thousands" para idicar qual o separador de milhar está sendo utilizado no arquivo (se é vírgula ou ponto);
# - Utilizar o "decimal" para indicar o separador de casas decimai utilizado no arquivo (se ponto ou vírgula).

# %% [markdown]
# ## Importando dados de Atendimento
# #### Etapas realizadas:
# 
# - Importada a biblioteca "PANDAS";
# - Realizada a leitura do arquido utilizando o "pd.read_csv";
# - Colar o caminho do arquivo (que deve ter sido previamente carregado);
# - Utilizar o "encoding" para dizer qual o formato do arquivo (Ex.: UTF-8, ISO-8859-1);
# - Utilizar o "skiprows" para indicar quantas linhas devem ser puladas para iniciar a leitura do código;
# - Utilizar "sep" para idicar qual o separador de dados está sendo utilizado (Ex.: vírgula, ponto e vírgula...);
# - Utilizar o "skipfooter" para indicar quantas linhas devem ser puladas no final;
# - Utilizar o "thousands" para idicar qual o separador de milhar está sendo utilizado no arquivo (se é vírgula ou ponto);
# - Utilizar o "decimal" para indicar o separador de casas decimai utilizado no arquivo (se ponto ou vírgula).

# %%
import pandas as pd

# %% [markdown]
# ## Analisando dados de produção hospitalar

# %%
#### Dados é um dataframe
dados = pd.read_csv('C:/Users/flora/OneDrive/Documentos/POS_GRADUCAO/Fase 01 - Data Analysis and Exploration/1 - Análise Exploratória de Dados/Aula 01/PROCEDIMENTOS_HOSPITALARES_DO_SUS-ANO_ATENDIMENTO.csv', encoding='ISO-8859-1', skiprows=3, sep=';', skipfooter=12, thousands='.', decimal=',', engine='python')

# %%
dados.head()

# %%
dados.tail()

# %%
dados.mean(numeric_only=True)

# %%
dados.info()

# %%
pd.options.display.float_format = "{:.2f}".format

# %%
dados.mean(numeric_only=True)

# %% [markdown]
# ## Importando dados de Processamento
# 
# ### Etapas realizadas:
# - Importada a biblioteca "PANDAS";
# - Realizada a leitura do arquido utilizando o "pd.read_csv";
# - Colar o caminho do arquivo (que deve ter sido previamente carregado);
# - Utilizar o "encoding" para dizer qual o formato do arquivo (Ex.: UTF-8, ISO-8859-1);
# - Utilizar o "skiprows" para indicar quantas linhas devem ser puladas para iniciar a leitura do código;
# - Utilizar "sep" para idicar qual o separador de dados está sendo utilizado (Ex.: vírgula, ponto e vírgula...);
# - Utilizar o "skipfooter" para indicar quantas linhas devem ser puladas no final;
# - Utilizar o "thousands" para idicar qual o separador de milhar está sendo utilizado no arquivo (se é vírgula ou ponto);
# - Utilizar o "decimal" para indicar o separador de casas decimai utilizado no arquivo (se ponto ou vírgula). vírgula).

# %%
dados_proc = pd.read_csv ('C:/Users/flora/OneDrive/Documentos/POS_GRADUCAO/Fase 01 - Data Analysis and Exploration/1 - Análise Exploratória de Dados/Aula 01/PROCEDIMENTOS_HOSPITALARES_DO_SUS-PROCESSAMENTO.csv', encoding='ISO-8859-1', skiprows=3, sep=';', skipfooter=12, thousands='.', decimal=',', engine='python')

# %%
dados_proc.head()

# %%
dados_proc.tail()

# %%
dados_proc.info()

# %%
dados_proc.mean(numeric_only = True)

# %%
dados.plot(x="Unidade da Federação", y = "2008/Ago")

# %%
dados.plot(x="Unidade da Federação", y = "2008/Ago", kind="bar")

# %%
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

axis = dados.plot(x="Unidade da Federação", y = "2008/Ago", kind="bar", figsize=(9,6))
axis.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.2f}"))

plt.title ("Valor por unidade da Federação")
plt.xticks(rotation=75)
plt.show ()

# %% [markdown]
# ## Aula 3.1

# %%
dados [["2008/Ago","2008/Set"]].head()

# %%
dados.head()

# %%
dados.columns

# %%
dados.mean(numeric_only=True).index.tolist()

# %%
dados[["2008/Ago", "2008/Set"]].head()

# %%
dados.columns

# %%
colunas_usaveis = dados.mean(numeric_only=True).index.tolist()
colunas_usaveis.insert(0, "Unidade da Federação")
colunas_usaveis[:5]

# %%
dados_usaveis = dados[colunas_usaveis]
dados_usaveis.head()

# %%
dados_usaveis = dados_usaveis.set_index("Unidade da Federação")
dados_usaveis.head()

# %%
dados_usaveis["2008/Ago"].head()

# %%
dados_usaveis.loc["12 Acre"]

# %%
dados_usaveis.iloc[1]

# %%
dados_usaveis.plot(figsize=(12,6))

# %%
dados_usaveis.T.plot(figsize=(12,6))
##o T é para transpor o gráfico entre x e y

# %%
dados_usaveis.T.tail()

# %% [markdown]
# #### O erro que aparece abaixo, ocorre à partir da segunda execução, pois a linha "Total" já foi removida e atualizada nos plots acimas.

# %%
dados_usaveis = dados_usaveis.drop("Total", axis =1)
dados_usaveis.head()

# %%
dados_usaveis.T.max()

# %% [markdown]
# ### Desafio: reposicionar a legenda e retocar o gráfico, e incluir títulos nos dois eixos.

# %%
import matplotlib.pyplot as plt 

dados = dados_usaveis.T.plot(figsize=(12,6))
dados.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 8.15})

plt.title ("Valor por período")

# %% [markdown]
# ## Aula 3.2

# %%
dados_usaveis.T.columns[:5]

# %%
dados_usaveis.index[:5]

# %%
dados_usaveis[:7].T.plot(figsize=(10,6))

# %%
dados_usaveis.sample(n=7)

# %%
dados_usaveis.sample(7).T.plot(figsize=(10,6))

# %%
# Algoritmo pseudo aleatório (pseudo randomness)

# 53874
# regra: dividir por 10

# 5387
# regra: dividir por 10

# 538
# regra: dividir por 10

# 53
# regra: dividir por 10

# 5

# %%
import numpy as np

np.random.seed(524387)
dados_usaveis.sample(n=7)

# %%
dados_usaveis.sample(n=7).T.plot(figsize=(10,6))

# %%
dados_usaveis["Total"] = dados_usaveis.sum(axis = 1)
dados_usaveis.head()

# %% [markdown]
# ## Aula 3.2

# %%
dados_usaveis.head()

# %%
dados_usaveis.sort_values(by="Total")

# %%
ordenados_por_total = dados_usaveis.sort_values(by="Total", ascending = False)
ordenados_por_total= ordenados_por_total.drop("Total", axis = 1)
## caso queira carregar apenas na tabela em questão: ordenados_por_total.drop("Total", axis = 1, inplace = True)
ordenados_por_total.head(5)

# %%
ordenados_por_total.head(5).T.plot(figsize=(10,6))

# %%
colunas_interessadas = ordenados_por_total.columns[6:]
ordenados_por_total = ordenados_por_total[colunas_interessadas]

# %%
ordenados_por_total.head(5).T.plot(figsize=(10,6))

# %% [markdown]
# ## Aula 4.1

# %%
ordenados_por_total = ordenados_por_total/1_000_000

# %%
axis = ordenados_por_total.head(5).T.plot(figsize=(10,6))
##axis.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
axis.set_ylabel("Gasto aprovado em milhões de reais")
axis.set_xlabel("Mês")

# %%
meses_filtrados = ordenados_por_total.columns[47:]
ordenados_por_total[meses_filtrados].head(3).T.plot(figsize=(10,6))

# %% [markdown]
# #### A célula abaixo mostra como definir uma função:

# %%
## Definindo uma função:

def plota_gastos_por_mes(dados, figsize=(10,6)): 
    axis = dados.T.plot(figsize=figsize)
    axis.set_ylabel("Gasto aprovado em milhões de reais")
    axis.set_xlabel("Mês")

# %%
plota_gastos_por_mes(ordenados_por_total[meses_filtrados].head(3))
plt.ylim(0,600)

# %%
plota_gastos_por_mes(ordenados_por_total[ordenados_por_total.columns[45:70]].head(3))
plt.ylim(0,320)

# %%
## Gráfico dos últimos meses
plota_gastos_por_mes(ordenados_por_total[ordenados_por_total.columns[-12:]].head(3))
plt.ylim(0,640)

# %%
## Gráfico dos últimos 5 anos
plota_gastos_por_mes(ordenados_por_total[ordenados_por_total.columns[-60:]].head(3))
plt.ylim(0,640)

# %%
plota_gastos_por_mes(ordenados_por_total.head(3))
plt.ylim(0,640)

# %%
plota_gastos_por_mes(ordenados_por_total.head(5))
plt.ylim(0,640)

# %%
plota_gastos_por_mes(ordenados_por_total.head(5), figsize=(6,6))
plt.ylim(0,640)
plt.xticks(rotation=75)

# %%
plota_gastos_por_mes(ordenados_por_total.head(5), figsize=(20,6))
plt.ylim(0,640)

# %% [markdown]
# ## Aula 5.1

# %%
mes_mais_recente = ordenados_por_total.columns[-1]
mes_mais_recente

# %%
gastos_do_mais_recente = ordenados_por_total[mes_mais_recente]
gastos_do_mais_recente.head()

# %%
gastos_do_mais_recente.plot()

# %%
gastos_do_mais_recente.plot(kind='pie')

# %%
gastos_do_mais_recente.sample(frac=1).plot(kind='pie')

# %%
gastos_do_mais_recente

# %%
gastos_do_mais_recente.loc["41 Paraná"]

# %%
## Tabela de proporção de gastos entre estados, usando como partida os valores do Paraná
gastos_do_mais_recente / gastos_do_mais_recente.loc["41 Paraná"]

# %%
tabela_de_comparacao = gastos_do_mais_recente / gastos_do_mais_recente.loc["41 Paraná"]
tabela_de_comparacao.head(5)

# %%
tabela_de_comparacao.plot(kind = "bar")

# %%
tabela_de_comparacao.plot(kind = "barh")

# %%
tabela_de_comparacao = tabela_de_comparacao.sort_values(ascending=False)
tabela_de_comparacao.plot(kind = "bar")

# %% [markdown]
# # Módulo 2: Visualização de dados

# %% [markdown]
# ### Aula 1.1

# %%
ibge_estimativa = pd.read_excel('C:/Users/flora/OneDrive/Documentos/POS_GRADUCAO/Fase 01 - Data Analysis and Exploration/2 - Visualização de Dados/estimativa_dou_2020.xlsx')
ibge_estimativa.head()


# %%
dados_da_populacao = """Posição	Unidade federativa	População	% da pop. total	País comparável
(habitantes)

1	 São Paulo	46 649 132	21,9%	Flag of Spain.svg Espanha (46 439 864)
2	 Minas Gerais	21 411 923	10,1%	 Sri Lanka (20 675 000)
3	 Rio de Janeiro	17 463 349	8,2%	 Países Baixos (16 922 900)
4	Bahia Bahia	14 985 284	7,1%	 Chade (14 037 000)
5	 Paraná	11 597 484	5,4%	 Bolívia (11 410 651)
6	 Rio Grande do Sul	11 466 630	5,4%	 Bélgica (11 250 659)
7	 Pernambuco	9 674 793	4,5%	 Bielorrússia (9 485 300)
8	 Ceará	9 240 580	4,3%	 Emirados Árabes Unidos (9 157 000)
9	Pará Pará	8 777 124	4,1%	 Áustria (8 602 112)
10	 Santa Catarina	7 338 473	3,4%	 Sérvia (7 114 393)
11	 Goiás	7 206 589	3,4%	 Paraguai (7 003 406)
12	 Maranhão	7 153 262	3,4%	 Paraguai (7 003 406)
13	 Amazonas	4 269 995	2,0%	 Líbano (4 168 000)
14	 Espírito Santo	4 108 508	1,9%	 Líbano (4 168 000)
15	 Paraíba	4 059 905	1,9%	 Líbano (4 168 000)
16	 Mato Grosso	3 567 234	1,7%	 Uruguai (3 415 866)
17	 Rio Grande do Norte	3 560 903	1,7%	 Uruguai (3 415 866)
18	 Alagoas	3 365 351	1,6%	 Uruguai (3 415 866)
19	 Piauí	3 289 290	1,6%	 Kuwait (3 268 431)
20	 Distrito Federal	3 094 325	1,4%	 Lituânia (2 900 787)
21	 Mato Grosso do Sul	2 839 188	1,3%	 Jamaica (2 717 991)
22	 Sergipe	2 338 474	1,1%	 Namíbia (2 280 700)
23	 Rondônia	1 815 278	0,8%	 Gabão (1 725 000)
24	 Tocantins	1 607 363	0,7%	 Bahrein (1 359 800)
25	 Acre	906 876	0,4%	 Fiji (859 178)
26	 Amapá	877 613	0,4%	 Fiji (859 178)
27	 Roraima	652 713	0,3%	 Luxemburgo (562 958)"""

# fonte https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o#cite_note-IBGE_POP-1
# fonte indireta IBGE

# %%
from io import StringIO
dados_da_populacao_io = StringIO(dados_da_populacao)

populacao = pd.read_csv(dados_da_populacao_io, sep="\t")
populacao = populacao.dropna()
populacao.head()

# %% [markdown]
# ### Aula 1.2

# %%
populacao.columns = ["posicao", "uf", "populacao", "porcentagem", "pais_comparavel"]
populacao["populacao"] = populacao["populacao"].str.replace(" ", "").astype(int)
populacao = populacao[["uf", "populacao"]]
populacao.head()

# %%
gastos_do_mais_recente.index = gastos_do_mais_recente.index.str[3:]
gastos_do_mais_recente.head()

# %%
populacao = populacao.set_index("uf")
populacao.head()

# %%
for estado in gastos_do_mais_recente.index:
  populacao.index = populacao.index.str.replace(f"{estado} {estado}", estado)
populacao.index

# %%
gastos_e_populacao = populacao.join(gastos_do_mais_recente)
gastos_e_populacao.head()

# %%
ultima_coluna = gastos_e_populacao.columns[-1]
gastos_e_populacao["gastos"] = gastos_e_populacao[ultima_coluna] * 1_000_000
gastos_e_populacao.plot()

# %%



