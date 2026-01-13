def is_vertex_cover(edges, cover):
    cover = set(cover)
    for (u, v) in edges:
        if u not in cover and v not in cover:
            return False
    return True

def generate_subsets(vertices, k, start, current, all_subsets):
    if len(current) == k:
        all_subsets.append(current[:])
        return

    for i in range(start, len(vertices)):
        current.append(vertices[i])
        generate_subsets(vertices, k, i + 1, current, all_subsets)
        current.pop()

def optimal_vertex_cover(vertices, edges):
    n = len(vertices)

    for k in range(1, n + 1):
        subsets = []
        generate_subsets(vertices, k, 0, [], subsets)

        for subset in subsets:
            if is_vertex_cover(edges, subset):
                return set(subset)

    return set()

def greedy_vertex_cover(vertices, edges):
    remaining_edges = edges[:]
    cover = set()

    while remaining_edges:
        u, v = remaining_edges[0]
        cover.add(u)
        cover.add(v)

        remaining_edges = [
            (x, y) for (x, y) in remaining_edges
            if x != u and x != v and y != u and y != v
        ]

    return cover

def compare_vertex_cover(vertices, edges):
    opt = optimal_vertex_cover(vertices, edges)
    greedy = greedy_vertex_cover(vertices, edges)

    print("Optimal Vertex Cover:", opt, "Size:", len(opt))
    print("Greedy Vertex Cover :", greedy, "Size:", len(greedy))
    print("Approximation Ratio :", len(greedy) / len(opt))

V = [0, 1, 2, 3]
E = [(0, 1), (1, 2)]

compare_vertex_cover(V, E)
