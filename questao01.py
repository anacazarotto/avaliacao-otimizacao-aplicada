import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edges = [
    ('V0','V1',1.0), ('V0','V2',5.0), ('V0','V3',5.3),
    ('V1','V2',0.3), ('V1','V4',1.9),
    ('V2','V3',0.5), ('V2','V4',0.3), ('V2','V5',9.1),
    ('V3','V5',5.0), ('V4','V5',1.3)
]
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G, algorithm='prim')

mst_edges = list(mst.edges(data=True))
print("Arestas da MST (Prim):")
for u, v, d in mst_edges:
    print(f"  {u} - {v} (peso = {d['weight']})")

total_cost = sum(d['weight'] for _, _, d in mst_edges)
print(f"Custo total da MST: {total_cost:.2f}")

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='lightgray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw(mst, pos, with_labels=True, edge_color='red', width=2)
plt.title(f"Árvore Geradora Mínima (Prim) — custo = {total_cost:.2f}")
plt.show()