def map_coloring(graph):
    colors = {}
    available_colors = set(['Red', 'Green', 'Blue', 'Yellow'])

    for region in graph:
        used_colors = {colors[neighbor] for neighbor in graph[region] if neighbor in colors}
        available_colors -= used_colors
        if available_colors:
            colors[region] = min(available_colors)
        else:
            raise ValueError("No available colors for region {}".format(region))

    return colors

example_graph = {
    'A': ['C', 'B', 'D'],
    'B': ['B', 'C'],
    'C': ['A', 'C', 'D'],
    'D': ['B', 'A']
}

try:
    result = map_coloring(example_graph)
    print("Assigned colors:", result)
except ValueError as e:
    print(e)
