```markdown
# Algoritmos de Grafos — Exercícios (Prim, Kruskal, Floyd-Warshall, Bellman-Ford, Dijkstra)

Este repositório contém um script Python genérico que resolve as questões do trabalho:
- Questão 1 — Árvore geradora de custo mínimo (Algoritmo de Prim)
- Questão 2 — Árvore geradora de custo mínimo (Algoritmo de Kruskal)
- Questão 3 — Floyd–Warshall: matriz de distâncias e matriz de predecessores
- Questão 4 — Bellman–Ford: arranjo de distâncias, predecessores e árvore de caminhos de menor custo (SPT)
- Questão 5 — Dijkstra: arranjo de distâncias, predecessores e árvore de caminhos de menor custo (SPT)

O objetivo é ser genérico: o mesmo script calcula e imprime os resultados para todas as questões, com opções de configurar a origem (source) para os algoritmos single-source.

Instalação
1) Baixe os arquivos

2) Instale o python e as biblioteca networkx e matplotlib

3) Entre na pasta onde baixou
Abra o terminal
Teste exercício por exercício
Exemplo: 'python questao01.py' 

Saídas geradas:
- Impressões no terminal:
  - Aretes e custo total das MSTs (Prim e Kruskal)
  - Matriz de distâncias e matriz de predecessores do Floyd–Warshall
  - Arranjos de distância e predecessores (Bellman–Ford e Dijkstra)
  - Árvore de caminhos de menor custo (arestas do SPT) para Bellman–Ford e Dijkstra com soma dos pesos
  - As imagens em png das AGM em suas respectivas questões.
