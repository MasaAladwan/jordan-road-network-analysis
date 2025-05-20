import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Load the Amman network
G_amman = ox.graph_from_place("Amman, Jordan", network_type='drive', simplify=True)
G_undirected_amman = G_amman.to_undirected()

# Compute betweenness centrality
betweenness_centrality_amman = nx.betweenness_centrality(G_undirected_amman, weight='length', normalized=True, k=1000)

# Get the top 5 nodes
top_btwn_amman = sorted(betweenness_centrality_amman.items(), key=lambda x: x[1], reverse=True)[:5]

# Create a new figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the base network
ox.plot_graph(G_undirected_amman, 
             ax=ax,
             node_size=0,
             edge_linewidth=0.5,
             edge_color='gray',
             bgcolor='white',
             show=False)

# Plot each top node
for i, (node, score) in enumerate(top_btwn_amman, 1):
    x = G_undirected_amman.nodes[node]['x']
    y = G_undirected_amman.nodes[node]['y']
    ax.scatter(x, y, c='red', s=100, zorder=3)
    ax.annotate(f'#{i}\nScore: {score:.3f}', 
                (x, y), 
                xytext=(10, 10),
                textcoords='offset points',
                fontsize=8,
                bbox=dict(facecolor='white', alpha=0.7))

plt.title('Top 5 Nodes by Betweenness Centrality in Amman')
plt.savefig('results/visualizations/top_5_nodes.png', dpi=300, bbox_inches='tight')
plt.show()

# Print detailed information
print("\nTop 5 Nodes by Betweenness Centrality in Amman:")
for i, (node, score) in enumerate(top_btwn_amman, 1):
    print(f"\nNode #{i}:")
    print(f"  Betweenness Score: {score:.3f}")
    print(f"  Latitude: {G_undirected_amman.nodes[node]['y']:.6f}")
    print(f"  Longitude: {G_undirected_amman.nodes[node]['x']:.6f}") 