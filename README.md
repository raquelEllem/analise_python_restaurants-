# 1. Problema de negócio
A Fome Zero é uma empresa de tecnologia que desenvolveu um aplicativo que permite avaliar restaurantes em diversas localidades do mundo, levando em consideração suas culinárias, cidades e países.

Com o auxílio desse aplicativo, é possível conferir a pontuação dos estabelecimentos, o preço médio para duas pessoas e ainda ter acesso a uma lista dos melhores e piores restaurantes de cada cidade.

A companhia atua no ramo gastronômico, coletando uma vasta quantidade de informações sobre preços, culinárias, avaliações e outros aspectos relacionados aos restaurantes. Apesar do crescimento da empresa e da abundância de dados disponíveis, o CEO enfrenta dificuldades em visualizar integralmente os indicadores-chave de desempenho que medem o progresso da organização.

Nesse sentido, você foi contratado como um Cientista de Dados com o objetivo de desenvolver soluções para avaliar os restaurantes. No entanto, antes de treinar algoritmos, a necessidade imediata da empresa é contar com uma ferramenta que concentre os principais KPIs estratégicos em um único lugar, permitindo ao CEO consultar informações relevantes e tomar decisões importantes com facilidade.

A empresa Fome Zero adota um modelo de negócio que funciona como intermediário entre os estabelecimentos gastronômicos e os consumidores finais. Como forma de acompanhar o desenvolvimento dessas operações, o CEO tem interesse em monitorar algumas métricas de crescimento fundamentais, tais como:


### Do lado dos Países:

Quantidade de restaurantes registrados por país.

Quantidade de cidades registradas por país.

Média de avaliações feitas por país.

Média de preço de um prato para duas pessoas por país.


### Do lado das cidades:
Top 10 cidades com mais restaurantes na base de dados.

Top 7 cidades com restaurantes com média de avaliação acima de 4.

Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5.

Top 10 cidades com mais restaurantes com tipos culinários distintos.


### Do lado dos restaurantes:
Melhores restaurantes dos principais tipos culinários.

Top 10 restaurantes.

Top 10 melhores tipos de culinárias.

Top 10 piores tipos de culinárias.


# 2. Premissas assumidas para a análise
A análise foi realizada com dados entre 22/02/2023 e 28/02/2023.
Os 3 principais visões do negócio foram: Visão dos países, visão das cidades e visão dos tipos de culinária.


# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:

  -Visão de todos os restaurantes cadastrados
  
  -Visão das avaliações feitas por país
  
  -Visão das avaliações feitas por cidade
  
  -Visão dos tipos de culinária

Cada visão é representada pelo seguinte conjunto de métricas:


### Do lado dos Países:
Quantidade de restaurantes registrados por país.

Quantidade de cidades registradas por país.

Média de avaliações feitas por país.

Média de preço de um prato para duas pessoas por país.


### Do lado das cidades:
Top 10 cidades com mais restaurantes na base de dados.

Top 7 cidades com restaurantes com média de avaliação acima de 4.

Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5.

Top 10 cidades com mais restaurantes com tipos culinários distintos.


### Do lado dos restaurantes:
Melhores restaurantes dos principais tipos culinários.

Top 10 restaurantes.

Top 10 melhores tipos de culinárias.

Top 10 piores tipos de culinárias.


# 4. Top 3 Insights de dados
  -A Indonésia é o 11º país com maior quantidadade de restaurantes, mas é o primeiro em quantidade média de avaliações e também o que possui o maior preço médio em um prato para duas pessoas.
  
  -Na Inglaterra e no Brasil há uma grande concentração de restaurantes por cidade.
  
  -Abu Dhabi é uma das cidades com a maior quantidade de restaurantes.
  
  -Na Inglaterra estão os dois restaurantes com melhores avaliações em comida americana. 
  
  -Ramen é considerada a melhor culinária.
 
 
# 5. O produto final do projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: https://raquelellem-fome-zero.streamlit.app

# 6. Conclusão
O propósito deste projeto é desenvolver um conjunto otimizado de gráficos e/ou tabelas para apresentar essas métricas ao CEO de forma mais eficiente. 

Com base na perspectiva da empresa, podemos concluir a qualidade dos restaurantes pode variar significativamente de um lugar para outro, o que pode ser influenciado por fatores como a cultura culinária local, a competição no mercado, os padrões de higiene e também pela segurança alimentar.

# 7. Próximo passos
Reduzir o número de métricas.

Criar novos filtros.

Adicionar novas visões de negócio.



