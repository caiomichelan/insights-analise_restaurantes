# Insights - Análise de Restaurantes

## Data Science Project - Análise de Restaurantes

<div align='center'>

![Restaurants](https://user-images.githubusercontent.com/104601836/233802619-2704ce2e-9689-47fe-93df-2b7b58c64a20.jpg)

</div>


<p align='justify'> </p>


# 1. Problema do Negócio
<p align='justify'>Uma grande empresa de Marketplace de restaurantes, onde o objetivo principal é facilitar o encontro e negociações entre clientes e restaurantes, sendo que os restaurantes fazem o cadastro na plataforma da empresa, fornecendo informações como nome do restaurante, cidade, país, tipo de culinária servida, valores, notas de avaliação, dentre outras informações.</p>
<p align='justify'>Foi identificada a necessidade de melhor entendimento das informações disponibilizadas na plataforma para que haja a possibilidade de fomentar tomadas de decisões mais assertivas com base no negócio em si, contribuindo para sua alavancagem. Desta forma, se faz necessário a análise dos dados da empresa com a elaboração de um dashboard geral para identificação de possíveis Insights, onde foram propostas as seguintes questões:</p>

Dados gerais:
1. Quantos restaurantes estão registrados?
2. Quantos países estão registrados?
3. Quantas cidades estão registradas?
4. Qual o total de tipos de culinária registrados?
5. Qual o total de avaliações registradas na plataforma?

País:
1. Qual a distribuição da quantidade total de restaurantes por país?
2. Quais os 10 países com mais restaurantes registrados?
3. Quais os países com maior número de tipos de culinária?
4. Quais os países que apresentam maior média de preços, referente aos pratos que servem duas pessoas?
5. Quais os países que apresentam maior média de avaliações na plataforma?

Cidades:
1. Quais as 10 cidades com maior número de restaurantes registrados?
2. Quais as 5 cidades com mais avaliações acima de 4,6 e sua quantidade?
3. Quais as 5 cidades com mais avaliações abaixo de 2,0 e sua quantidade?
4. Quais as 10 cidades com maior variedade de tipos de culinária e sua quantidade?
5. Qual a quantidade total de restaurantes registrados na plataforma para cada cidade?

Tipos de Culinária
1. Quais os 10 tipos de culinária com maior número de restaurantes registrados?
2. Quais os 10 tipos culinários com mais avaliações acima de 4,6 e sua representatividade entre os mesmos?
3. Quais os 10 tipos culinários com mais avaliações abaixo de 2,0 e sua representatividade entre os mesmos?
4. Qual a quantidade de restaurantes registrados subdivididos por tipos de culinária e país?

# 2. Premissas do Negócio
<p align='justify'>Como premissa foram consideradas a Base de Dados da referida empresa (neste projeto foram utilizados dados públicos) e a necessidade de disponibilização das informações solicitadas em ambiente com infraestrutura em nuvem.</p>
<p align='justify'>Modelo de negócio identificado como Marketplace.</p>
<p align='justify'>Foram consideradas as 4 principais visões de negócio, sendo o Acompanhamento Geral, somado à Visão por País, Visão por Cidades e Visão por Tipos de Culinária.</p>

# 3. Estratégia da Solução
<p align='justify'>Foi desenvolvido um Painel Gerencial estratégico com as métricas, dados para análises e Acompanhamento Geral, como também das 3 principais visões do modelo de negócio da empresa.</p>
<p align='justify'>Na Visão de Acompanhamento Geral foram disponibilizadas visões das principais métricas questionadas no âmbito geral.</p>
<p align='justify'>Para as visões por Países, Cidades e Tipos de Culinária foram considerados os questionamentos realizados para cada visão estratégica.</p>
<p align='justify'>Em todas as visões foi disponibilizado um filtro geral, o qual pode ser aplicado para seleção dos dados referentes a um ou mais países registrados, por padrão essa opção contempla todos os países registrados na base de dados.</p>

# 4. Insights de Dados
<p align='justify'>Como ponto principal, foi identificado que a grande maioria dos restaurantes cadastrados estão localizados na Índia, com 44,9% do total, seguida pelos Estados Unidos e Inglaterra, com 19,8% e 5,8% respectivamente.</p>
<p align='justify'>Apesar da Índia ser o país com mais restaurantes cadastrados, o número médio de avaliações registradas aos restaurantes deste país não se diferencia de maneira muito expressiva aos demais, ficando em segundo lugar, sendo ainda que no comparativo geral os Estados Unidos ficaram apenas na oitava posição, e a Inglaterra na décima terceira, o que indica que a quantidade de restaurantes registrados por países não implica na quantidade média de avaliações.</p>
<p align='justify'>Diversas cidades cadastraram um total de 80 restaurantes na plataforma.</p>

# 5. Produto Final
<p align='justify'>Painel Gerencial para análises estratégicas com o objetivo de fornecer Insights valiosos para tomada de decisões baseadas em dados.</p>
<p align='justify'>O produto foi disponibilizado em ambiente em nuvem, com garantia de acesso a qualquer horário, em qualquer dia da semana, salvo interrupções no sistema de hospedagem.</p>
<p align='justify'>O Relatório pode ser visualizado no seguinte link: <a href="https://caiomichelan-insights-analise-restaurantes-pgina-inicial-dkbwh0.streamlit.app/"> World Restaurants - Painel Gerencial</a></p>

# 6. Conclusão
<p align='justify'>O principal objetivo deste projeto foi criar um relatório que possibilite análises estratégicas e forneça Insights valiosos para tomadas de decisões por parte da gestão da empresa. Desta forma podemos concluir que com base nos dados dispostos a empresa pode focar em ações específicas de marketing voltadas a certos países, cidades e tipos de culinária, podendo trazer um incremento considerável na receita, bem como aquisição de mais clientes e posterior maior adesão à plataforma.</p>
<p align='justify'>Do ponto de vista da empresa, podemos concluir que a Índia é o país que mais contém restaurantes cadastrados (44,9%) na base de dados, seguidos pelos Estados Unidos (19,8%) e Inglaterra (5,8%).</p>

# 7. Próximos Passos
<p align='justify'>Como próximos passos será implementado um estudo para inclusão de mais filtros no relatório, bem como a inclusão de outras visões em conformidade com a necessidade da gestão.</p>

