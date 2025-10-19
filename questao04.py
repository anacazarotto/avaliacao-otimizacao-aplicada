from math import inf

edges = [
    ("V1", "V0", 1.0),
    ("V0", "V2", 5.0),
    ("V0", "V3", 5.3),
    ("V2", "V1", 0.3),
    ("V1", "V4", 1.9),
    ("V2", "V3", 0.5),
    ("V2", "V4", 0.3),
    ("V5", "V2", 9.1),
    ("V3", "V5", 5.0),
    ("V4", "V5", 1.3),
]

vertices = sorted({u for u,_,_ in edges} | {v for _,v,_ in edges})

def bellman_ford(vertices, edges, source):
    dist = {v: inf for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0.0

    n = len(vertices)
    for i in range(n-1):
        updated = False
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                updated = True
        if not updated:
            break

    for u, v, w in edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            raise ValueError("Grafo contém ciclo de peso negativo")

    return dist, pred

if __name__ == "__main__":
    source = "V0"
    dist, pred = bellman_ford(vertices, edges, source)

    print("Vértices:", vertices)
    print(f"Fonte: {source}\n")
    print("Distâncias finais (dist) e predecessores (pred):")
    print("{:<4} {:>8}   {:>8}".format("Vért", "Dist", "Pred"))
    for v in vertices:
        d = dist[v]
        p = pred[v] if pred[v] is not None else "-"
        print("{:<4} {:>8}   {:>8}".format(v, ("{:.1f}".format(d) if d != inf else "inf"), p))

    print("\nÁrvore de caminhos mínimos (arestas pred->v):")
    total_tree_cost = 0.0
    for v in vertices:
        if v == source:
            continue
        p = pred[v]
        if p is None:
            print(f"{v}: não alcançável")
        else:
            w = next(w for (a,b,w) in edges if a == p and b == v)
            print(f"{p} -> {v} (peso {w:.1f})")
            total_tree_cost += w
    print(f"\nCusto total da árvore (soma dos pesos das arestas da árvore): {total_tree_cost:.1f}")