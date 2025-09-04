import tkinter as tk
from tkinter import ttk
import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load dummy graph from JSON
def load_dummy_graph():
    with open("dummy_graph.json", "r") as f:
        data = json.load(f)
    G = nx.Graph()
    for node in data["nodes"]:
        G.add_node(node)
    for edge in data["edges"]:
        G.add_edge(edge["from"], edge["to"], weight=edge["distance"])
    return G

# Draw graph on canvas
def draw_graph(frame, G):
    fig, ax = plt.subplots(figsize=(5, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800, font_size=10, ax=ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Main GUI setup
def main():
    root = tk.Tk()
    root.title("EV Route Planner - Prototype")
    root.geometry("1100x650")

    # Frames
    graph_frame = tk.Frame(root, width=700, height=650)
    graph_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    control_frame = tk.Frame(root, width=400, bg="#f0f0f0")
    control_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Sidebar controls with larger fonts
    heading_font = ("Arial", 16, "bold")
    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)

    ttk.Label(control_frame, text="Route Settings", font=heading_font, background="#f0f0f0").pack(pady=15)

    ttk.Label(control_frame, text="Source:", font=label_font).pack(pady=5)
    ttk.Combobox(control_frame, values=["A", "B", "C", "D"], font=entry_font).pack(pady=5)

    ttk.Label(control_frame, text="Destination:", font=label_font).pack(pady=5)
    ttk.Combobox(control_frame, values=["A", "B", "C", "D"], font=entry_font).pack(pady=5)

    ttk.Label(control_frame, text="Battery Capacity (kWh):", font=label_font).pack(pady=5)
    tk.Entry(control_frame, font=entry_font).pack(pady=5)

    ttk.Label(control_frame, text="Current Charge (%):", font=label_font).pack(pady=5)
    tk.Entry(control_frame, font=entry_font).pack(pady=5)

    ttk.Label(control_frame, text="Consumption Rate (kWh/km):", font=label_font).pack(pady=5)
    tk.Entry(control_frame, font=entry_font).pack(pady=5)

    ttk.Button(control_frame, text="Run Algorithm").pack(pady=20)
    ttk.Button(control_frame, text="Edit Graph").pack(pady=10)
    ttk.Button(control_frame, text="Load Graph").pack(pady=10)
    ttk.Button(control_frame, text="Save Graph").pack(pady=10)

    # Load and draw dummy graph
    G = load_dummy_graph()
    draw_graph(graph_frame, G)

    root.mainloop()

if __name__ == "__main__":
    main()
