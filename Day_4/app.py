import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from ucs import uniform_cost_search

st.title("🌟 Uniform Cost Search (UCS) Visualizer")

# Example graph
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 3)],
    'F': []
}

start_node = st.selectbox("Select Start Node", list(graph.keys()), index=0)
goal_node = st.selectbox("Select Goal Node", list(graph.keys()), index=5)

if st.button("Run UCS"):
    path, cost = uniform_cost_search(graph, start_node, goal_node)

    st.write(f"**Path:** {path}")
    st.write(f"**Total Cost:** {cost}")

    # Draw graph
    G = nx.DiGraph()
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=12, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    if path:
        # Highlight path
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="r", width=2.5, ax=ax)

    st.pyplot(fig)
