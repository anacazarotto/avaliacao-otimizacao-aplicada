import csv
from math import inf

nodes = ['V0', 'V1', 'V2', 'V3', 'V4', 'V5']
index = {v: i for i, v in enumerate(nodes)}
n = len(nodes)

edges = [
    ('V1', 'V0', 1.0),
    ('V0', 'V2', 5.0),
    ('V0', 'V3', 5.3),
    ('V2', 'V1', 0.3),
    ('V1', 'V4', 1.9),
    ('V2', 'V3', 0.5),
    ('V2', 'V4', 0.3),
    ('V5', 'V2', 9.1),
    ('V3', 'V5', 5.0),
    ('V4', 'V5', 1.3),
]

D = [[inf] * n for _ in range(n)]  
P = [[None] * n for _ in range(n)] 

for i in range(n):
    D[i][i] = 0.0
    P[i][i] = None

for u, v, w in edges:
    i, j = index[u], index[v]
    if w < D[i][j]:
        D[i][j] = w
        P[i][j] = u

for k in range(n):
    for i in range(n):
        for j in range(n):
            if D[i][k] + D[k][j] < D[i][j]:
                D[i][j] = D[i][k] + D[k][j]
                P[i][j] = P[k][j] 

def fmt_num(x):
    return "INF" if x == inf else f"{x:.1f}"

def print_distance_matrix(D, nodes):
    print("\nMatriz de distâncias (linhas=origem, colunas=destino):")
    hdr = ["    "] + [f"{v:>6}" for v in nodes]
    print(" ".join(hdr))
    for i, v in enumerate(nodes):
        row = [f"{v:>4}"] + [f"{fmt_num(D[i][j]):>6}" for j in range(len(nodes))]
        print(" ".join(row))

def print_predecessor_matrix(P, nodes):
    print("\nMatriz de predecessores (predecessor imediato de j no caminho i->j):")
    hdr = ["    "] + [f"{v:>6}" for v in nodes]
    print(" ".join(hdr))
    for i, v in enumerate(nodes):
        row_items = []
        for j in range(len(nodes)):
            if i == j:
                row_items.append(f"{'-':>6}")
            else:
                pred = P[i][j]
                row_items.append(f"{(pred if pred is not None else 'None'):>6}")
        print(f"{v:>4} " + " ".join(row_items))

def reconstruct_path(i_name, j_name):
    """Reconstrói o caminho mínimo i_name -> j_name como lista de nós (ou None se não existir)."""
    if i_name not in index or j_name not in index:
        raise ValueError("Nó inválido")
    i = index[i_name]; j = index[j_name]
    if D[i][j] == inf:
        return None
    path = [j_name]
    cur = j
    
    while cur != i:
        pred = P[i][cur]
        if pred is None:
            return None
        path.append(pred)
        cur = index[pred]
    path.reverse()
    return path

def save_csvs(D, P, nodes, dist_file='distances.csv', pred_file='predecessors.csv'):
    
    with open(dist_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(nodes)
        for i, v in enumerate(nodes):
            row = [f"{D[i][j]:.1f}" if D[i][j] != inf else "INF" for j in range(len(nodes))]
            writer.writerow([v] + row)
            
    with open(pred_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(nodes)
        for i, v in enumerate(nodes):
            row = []
            for j in range(len(nodes)):
                if i == j:
                    row.append('-')
                else:
                    row.append(P[i][j] if P[i][j] is not None else '')
            writer.writerow([v] + row)
    print(f"\nArquivos salvos: {dist_file}, {pred_file}")

if __name__ == "__main__":
    print("Nós na ordem:", nodes)
    print_distance_matrix(D, nodes)
    print_predecessor_matrix(P, nodes)

    examples = [('V0', 'V5'), ('V3', 'V0'), ('V5', 'V2')]
    print("\nExemplos de caminhos mínimos:")
    for a, b in examples:
        path = reconstruct_path(a, b)
        dist = D[index[a]][index[b]]
        print(f"{a} -> {b} : {path} (dist = {'INF' if dist == inf else f'{dist:.1f}'})")

    save_csvs(D, P, nodes)