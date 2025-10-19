# kruskal_steps.py
import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ('V0','V1',1.0), ('V0','V2',5.0), ('V0','V3',5.3),
    ('V1','V2',0.3), ('V1','V4',1.9),
    ('V2','V3',0.5), ('V2','V4',0.3), ('V2','V5',9.1),
    ('V3','V5',5.0), ('V4','V5',1.3)
]

edges_sorted = sorted(edges, key=lambda e: e[2])

class UnionFind:
    def __init__(self, nodes):
        self.parent = {n:n for n in nodes}
        self.rank = {n:0 for n in nodes}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

nodes = sorted({u for u,_,_ in edges} | {v for _,v,_ in edges})
uf = UnionFind(nodes)

mst_edges = []
mst_cost = 0.0

print("Iter | Aresta (peso)  | Decisão           | Componentes (representantes)")
print("-----+-----------------+-------------------+-----------------------------")
iter_no = 0

print(f"{iter_no:4d} | {'-':15} | {'-':17} | " + ", ".join(f"{{{n}}}" for n in nodes))

for e in edges_sorted:
    iter_no += 1
    u, v, w = e
    ru, rv = uf.find(u), uf.find(v)
    decision = "adicionada" if uf.union(u, v) else "ignorad (ciclo)"
    if decision == "adicionada":
        mst_edges.append((u, v, w))
        mst_cost += w

    reps = {}
    for n in nodes:
        r = uf.find(n)
        reps.setdefault(r, []).append(n)
    comps_str = " | ".join(f"{r}:{sorted(m)}" for r, m in reps.items())
    print(f"{iter_no:4d} | {u+'-'+v+' ('+str(w)+')':15} | {decision:17} | {comps_str}")

print("\nArestas escolhidas na MST:")
for u, v, w in mst_edges:
    print(f"- {u} - {v}  (peso {w})")
print(f"Custo total = {mst_cost}")


G = nx.Graph()
G.add_weighted_edges_from(edges)
mst = nx.Graph()
mst.add_weighted_edges_from(mst_edges)

pos = nx.spring_layout(G, seed=42) 
plt.figure(figsize=(7,5))
nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw(mst, pos, with_labels=True, edge_color='red', width=2)
plt.title("Grafo com MST (arestas em vermelho)")
plt.axis('off')
plt.show()