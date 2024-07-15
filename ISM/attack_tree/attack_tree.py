import json
import networkx as nx
from pyvis.network import Network
import tkinter as tk
from tkinter import simpledialog, messagebox

# Import explanations
"""
json: A module for parsing JSON data, used to load attack tree structures from JSON files.
networkx: A library for creating and manipulating complex networks, used to create and manage the attack tree graph.
pyvis.network: A module from the PyVis library for visualizing network graphs in a web browser.
tkinter: A standard GUI library for Python, used to create dialogs for user input.
simpledialog: A submodule of tkinter for simple dialog boxes, used to prompt the user for input values.
messagebox: A submodule of tkinter for message boxes, used to display information to the user.
"""

def parse_attack_tree(data, parent=None, G=None):
    """
    Parses the attack tree JSON data and return populated NetworkX graph.    
        data (dict): JSON data representing the attack tree.
        parent (str): Parent node name.
        G (networkx.DiGraph): NetworkX graph object.
    """
    # Initialize the graph if it is None (not exist)
    if G is None:
        G = nx.DiGraph()  
    
    # Adds node to graph with default value=0    
    G.add_node(data["name"], value=0)
    
    if parent:
        # Adds directed edge from parent node to current node
        G.add_edge(parent, data["name"])
        
    for child in data.get("children", []):
        # Recursively parse each child
        parse_attack_tree(child, data["name"], G)  
    return G

def visualize_attack_tree(G, filename="attack_tree.html"):
    """
    Visualizes attack tree using PyVis and output HTML file.
    """
    # Create PyVis Network object for visualization
    net = Network(notebook=False) 
    
    # Load NetworkX graph into PyVis network
    net.from_nx(G)  
    
    for node in G.nodes:
        # Retrieve node data from PyVis network
        node_data = net.get_node(node)
        
        # Check if node_data is not None
        if node_data:  
            # Set title attribute of node to display its value on hover
            node_data['title'] = f"Value: {G.nodes[node]['value']}"
            # Set label attribute to display the name and value of node
            node_data['label'] = f"{node}\nValue: {G.nodes[node]['value']}"
    try:
        # Save the network visualization to HTML file
        net.write_html(filename)  
        print(f"Visualization saved to {filename}")
    except Exception as e:
        # Output error message if visualization fail
        print(f"Error rendering visualization: {e}")  

def input_values(G):
    """
    Prompts the user to input values for leaf nodes using Tkinter dialogs.
    """
    root = tk.Tk()   # Create the root window for Tkinter dialogs
    root.withdraw()  # Hide the root window as we only need the dialogs
    for node in G.nodes:
        if G.out_degree(node) == 0:  # Leaf node
            value = simpledialog.askfloat("Input", f"Enter value for {node} (monetary amount or probability):")
            G.nodes[node]['value'] = value
    root.destroy()  # Destroy the root window after input is done

def aggregate_values(G):
    """
    Aggregates values from leaf nodes and return the aggregated value of the root node.
    """
    def aggregate(node):
        if G.out_degree(node) == 0:  # Leaf node
            return G.nodes[node]['value']
        else:
            return sum(aggregate(child) for child in G.successors(node))
    
    for node in nx.dfs_postorder_nodes(G):
        if G.out_degree(node) > 0:  # Non-leaf node
            G.nodes[node]['value'] = aggregate(node)
    
    root_value = G.nodes[list(nx.topological_sort(G))[0]]['value']
    return root_value

def main():
    """
    Main function to run the application
    """
    # Load and process the first attack tree
    with open('pre_digitalisation.json') as f:
        data = json.load(f)
    G1 = parse_attack_tree(data)
    visualize_attack_tree(G1, "attack_tree_initial_pre_digitalisation.html")
    input_values(G1)
    total_value_1 = aggregate_values(G1)
    messagebox.showinfo("Total Value for Pre-digitalisation", f"The total aggregated value is: {total_value_1}")
    visualize_attack_tree(G1, "attack_tree_final_pre_digitalisation.html")

    # Load and process the second attack tree
    with open('post_digitalisation.json') as f:
        data = json.load(f)
    G2 = parse_attack_tree(data)
    visualize_attack_tree(G2, "attack_tree_initial_post_digitalisation.html")
    input_values(G2)
    total_value_2 = aggregate_values(G2)
    messagebox.showinfo("Total Value for Post-digitalisation", f"The total aggregated value is: {total_value_2}")
    visualize_attack_tree(G2, "attack_tree_final_post_digitalisation.html")

if __name__ == "__main__":
    main()