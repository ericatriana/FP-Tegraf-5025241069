"""
Longest Monotonically Increasing Subsequence (LMIS) Implementation
Menggunakan pendekatan Dynamic Programming dan Tree Visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import networkx as nx
from collections import deque

class Node:
    """Representasi node untuk tree visualization"""
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []
        self.level = 0 if parent is None else parent.level + 1

    def add_child(self, child_node):
        """Menambahkan child node"""
        self.children.append(child_node)

    def __repr__(self):
        return f"Node({self.value})"


class LMISolver:
    """
    Solver untuk mencari Longest Monotonically Increasing Subsequence
    menggunakan pendekatan tree-based dynamic programming
    """

    def __init__(self, sequence):
        """
        Inisialisasi solver dengan sequence input

        Args:
            sequence: List of integers
        """
        self.sequence = sequence
        self.n = len(sequence)
        self.tree_root = None
        self.all_nodes = []

    def build_tree(self):
        """
        Membangun tree untuk visualisasi semua kemungkinan subsequence
        Root node adalah placeholder, children-nya adalah semua elemen sequence
        """
        # Create root node (placeholder)
        self.tree_root = Node(None)
        self.all_nodes = [self.tree_root]

        # Build tree recursively
        self._build_tree_recursive(self.tree_root, -1, float('-inf'))

    def _build_tree_recursive(self, parent_node, start_idx, last_value):
        """
        Rekursif membangun tree dari semua kemungkinan subsequence

        Args:
            parent_node: Node parent saat ini
            start_idx: Index mulai pencarian di sequence
            last_value: Nilai terakhir dalam subsequence saat ini
        """
        for i in range(start_idx + 1, self.n):
            current_value = self.sequence[i]

            # Hanya tambahkan jika nilai lebih besar (monotonically increasing)
            if current_value > last_value:
                new_node = Node(current_value, parent_node)
                parent_node.add_child(new_node)
                self.all_nodes.append(new_node)

                # Lanjutkan build tree untuk subsequence yang lebih panjang
                self._build_tree_recursive(new_node, i, current_value)

    def find_longest_path(self):
        """
        Mencari path terpanjang dalam tree (LMIS)

        Returns:
            Tuple (longest_sequence, length)
        """
        if not self.tree_root:
            self.build_tree()

        longest_sequence = []
        max_length = 0

        # DFS untuk mencari path terpanjang
        def dfs(node, current_path):
            nonlocal longest_sequence, max_length

            if node.value is not None:
                current_path.append(node.value)

            if not node.children:  # Leaf node
                if len(current_path) > max_length:
                    max_length = len(current_path)
                    longest_sequence = current_path.copy()
            else:
                for child in node.children:
                    dfs(child, current_path)

            if node.value is not None:
                current_path.pop()

        dfs(self.tree_root, [])
        return longest_sequence, max_length

    def solve_dp(self):
        """
        Solusi alternatif menggunakan Dynamic Programming klasik
        Lebih efisien untuk sequence yang panjang

        Returns:
            Tuple (longest_sequence, length)
        """
        if self.n == 0:
            return [], 0

        # dp[i] menyimpan panjang LMIS yang berakhir di index i
        dp = [1] * self.n
        # parent[i] menyimpan index elemen sebelumnya dalam LMIS
        parent = [-1] * self.n

        # Compute dp values
        for i in range(1, self.n):
            for j in range(i):
                if self.sequence[j] < self.sequence[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

        # Find index with maximum length
        max_length = max(dp)
        max_idx = dp.index(max_length)

        # Reconstruct sequence
        longest_sequence = []
        idx = max_idx
        while idx != -1:
            longest_sequence.append(self.sequence[idx])
            idx = parent[idx]

        longest_sequence.reverse()
        return longest_sequence, max_length

    def print_tree(self, max_depth=None):
        """
        Mencetak tree dalam format hierarkis

        Args:
            max_depth: Kedalaman maksimum untuk dicetak (None = semua)
        """
        if not self.tree_root:
            self.build_tree()

        def print_node(node, prefix="", is_last=True, depth=0):
            if max_depth is not None and depth > max_depth:
                return

            if node.value is not None:
                connector = "└── " if is_last else "├── "
                print(prefix + connector + str(node.value))
                new_prefix = prefix + ("    " if is_last else "│   ")
            else:
                print("ROOT")
                new_prefix = ""

            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                print_node(child, new_prefix, is_last_child, depth + 1)

        print("\nTree Visualization:")
        print("=" * 50)
        print_node(self.tree_root)
        print("=" * 50)

    def get_statistics(self):
        """
        Mendapatkan statistik dari tree yang dibangun

        Returns:
            Dictionary berisi statistik
        """
        if not self.tree_root:
            self.build_tree()

        total_nodes = len(self.all_nodes) - 1  # Exclude root
        max_depth = max(node.level for node in self.all_nodes)

        return {
            'total_nodes': total_nodes,
            'max_depth': max_depth,
            'sequence_length': self.n
        }

    def visualize_tree(self, highlight_path=None, save_path='tree_visualization.png'):
        """
        Visualisasi tree menggunakan matplotlib

        Args:
            highlight_path: List nilai untuk di-highlight sebagai longest path
            save_path: Path untuk menyimpan gambar
        """
        if not self.tree_root:
            self.build_tree()

        G = nx.DiGraph()
        pos = {}
        labels = {}
        node_colors = []
        edge_colors = []

        # Build graph dan assign positions
        level_counts = {}
        level_positions = {}

        def add_to_graph(node, node_id=0):
            if node.value is None:
                current_id = 'root'
                labels[current_id] = 'ROOT'
            else:
                current_id = node_id
                labels[current_id] = str(node.value)
                G.add_node(current_id)

            level = node.level
            if level not in level_counts:
                level_counts[level] = 0
                level_positions[level] = []

            level_positions[level].append(current_id)
            level_counts[level] += 1

            child_id = node_id + 1
            for child in node.children:
                if node.value is None:
                    parent_id = 'root'
                else:
                    parent_id = current_id

                G.add_edge(parent_id, child_id)
                child_id = add_to_graph(child, child_id)

            return child_id

        add_to_graph(self.tree_root)

        # Calculate positions
        max_width = max(len(nodes) for nodes in level_positions.values())
        for level, nodes in level_positions.items():
            y = -level * 2
            width = len(nodes)
            start_x = -(width - 1) / 2 * 3
            for i, node_id in enumerate(nodes):
                pos[node_id] = (start_x + i * 3, y)

        # Determine colors
        highlight_set = set(highlight_path) if highlight_path else set()
        for node_id in G.nodes():
            if node_id == 'root':
                node_colors.append('#FFD700')  # Gold for root
            elif labels[node_id].isdigit() and int(labels[node_id]) in highlight_set:
                node_colors.append('#FF6B6B')  # Red for highlighted path
            else:
                node_colors.append('#87CEEB')  # Sky blue for others

        # Create figure
        plt.figure(figsize=(16, 10))

        # Draw edges
        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True,
                              arrowsize=15, width=1.5, alpha=0.6)

        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_color=node_colors,
                              node_size=800, alpha=0.9, edgecolors='black', linewidths=2)

        # Draw labels
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')

        # Add title and legend
        plt.title(f'Tree Visualization - LMIS Problem\nInput: {self.sequence}',
                 fontsize=14, fontweight='bold', pad=20)

        legend_elements = [
            mpatches.Patch(color='#FFD700', label='Root Node'),
            mpatches.Patch(color='#FF6B6B', label='Longest Path'),
            mpatches.Patch(color='#87CEEB', label='Other Nodes')
        ]
        plt.legend(handles=legend_elements, loc='upper right', fontsize=10)

        plt.axis('off')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\nTree visualization saved to: {save_path}")
        plt.close()

    def visualize_dp_process(self, save_path='dp_process.png'):
        """
        Visualisasi proses Dynamic Programming

        Args:
            save_path: Path untuk menyimpan gambar
        """
        if self.n == 0:
            return

        # Compute DP
        dp = [1] * self.n
        parent = [-1] * self.n

        for i in range(1, self.n):
            for j in range(i):
                if self.sequence[j] < self.sequence[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

        # Find longest sequence
        max_length = max(dp)
        max_idx = dp.index(max_length)

        # Reconstruct path
        path_indices = []
        idx = max_idx
        while idx != -1:
            path_indices.append(idx)
            idx = parent[idx]
        path_indices.reverse()

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

        # Plot 1: Sequence with DP values
        x_pos = range(self.n)
        colors = ['#FF6B6B' if i in path_indices else '#87CEEB' for i in range(self.n)]

        bars = ax1.bar(x_pos, self.sequence, color=colors, alpha=0.7, edgecolor='black', linewidth=2)

        # Add value labels on bars
        for i, (bar, val) in enumerate(zip(bars, self.sequence)):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{val}\ndp={dp[i]}',
                    ha='center', va='bottom', fontweight='bold', fontsize=9)

        ax1.set_xlabel('Index', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Value', fontsize=12, fontweight='bold')
        ax1.set_title('Input Sequence with DP Values', fontsize=14, fontweight='bold')
        ax1.set_xticks(x_pos)
        ax1.grid(axis='y', alpha=0.3)

        # Plot 2: DP array visualization
        dp_colors = ['#FF6B6B' if i in path_indices else '#87CEEB' for i in range(self.n)]
        bars2 = ax2.bar(x_pos, dp, color=dp_colors, alpha=0.7, edgecolor='black', linewidth=2)

        # Add arrows showing parent connections for path
        for i in range(len(path_indices) - 1):
            curr_idx = path_indices[i]
            next_idx = path_indices[i + 1]
            ax2.annotate('', xy=(next_idx, dp[next_idx] - 0.2),
                        xytext=(curr_idx, dp[curr_idx] + 0.2),
                        arrowprops=dict(arrowstyle='->', color='red', lw=2))

        # Add value labels
        for i, (bar, val) in enumerate(zip(bars2, dp)):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{val}',
                    ha='center', va='bottom', fontweight='bold', fontsize=10)

        ax2.set_xlabel('Index', fontsize=12, fontweight='bold')
        ax2.set_ylabel('DP Value (Length of LMIS)', fontsize=12, fontweight='bold')
        ax2.set_title(f'DP Array - Longest Path: {[self.sequence[i] for i in path_indices]}',
                     fontsize=14, fontweight='bold')
        ax2.set_xticks(x_pos)
        ax2.grid(axis='y', alpha=0.3)

        # Add legend
        legend_elements = [
            mpatches.Patch(color='#FF6B6B', label='Part of LMIS'),
            mpatches.Patch(color='#87CEEB', label='Not in LMIS')
        ]
        ax2.legend(handles=legend_elements, loc='upper left', fontsize=10)

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"DP process visualization saved to: {save_path}")
        plt.close()

    def visualize_comparison(self, save_path='comparison.png'):
        """
        Visualisasi perbandingan input sequence dan LMIS hasil

        Args:
            save_path: Path untuk menyimpan gambar
        """
        longest_seq, length = self.solve_dp()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Plot 1: Original sequence
        x_pos = range(self.n)
        ax1.plot(x_pos, self.sequence, 'o-', color='#87CEEB',
                linewidth=2, markersize=10, label='Original Sequence')

        for i, val in enumerate(self.sequence):
            ax1.text(i, val + 0.5, str(val), ha='center', va='bottom',
                    fontweight='bold', fontsize=10)

        ax1.set_xlabel('Index', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Value', fontsize=12, fontweight='bold')
        ax1.set_title(f'Original Sequence (Length: {self.n})', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=10)

        # Plot 2: LMIS
        lmis_x = range(len(longest_seq))
        ax2.plot(lmis_x, longest_seq, 'o-', color='#FF6B6B',
                linewidth=2, markersize=12, label='LMIS')

        for i, val in enumerate(longest_seq):
            ax2.text(i, val + 0.5, str(val), ha='center', va='bottom',
                    fontweight='bold', fontsize=11)

        ax2.set_xlabel('Position', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Value', fontsize=12, fontweight='bold')
        ax2.set_title(f'Longest Monotonically Increasing Subsequence (Length: {length})',
                     fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.legend(fontsize=10)

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Comparison visualization saved to: {save_path}")
        plt.close()


def main():
    """Fungsi utama untuk menjalankan program"""

    # Contoh dari gambar: 4, 1, 13, 7, 0, 2, 8, 11, 3
    sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

    print("=" * 70)
    print("LONGEST MONOTONICALLY INCREASING SUBSEQUENCE (LMIS)")
    print("=" * 70)
    print(f"\nInput Sequence: {sequence}")
    print(f"Length: {len(sequence)}")

    # Inisialisasi solver
    solver = LMISolver(sequence)

    # Metode 1: Tree-based approach
    print("\n" + "-" * 70)
    print("METODE 1: TREE-BASED APPROACH")
    print("-" * 70)

    solver.build_tree()
    longest_seq_tree, length_tree = solver.find_longest_path()

    print(f"\nLongest Monotonically Increasing Subsequence:")
    print(f"Sequence: {longest_seq_tree}")
    print(f"Length: {length_tree}")

    # Statistik tree
    stats = solver.get_statistics()
    print(f"\nTree Statistics:")
    print(f"- Total nodes explored: {stats['total_nodes']}")
    print(f"- Maximum depth: {stats['max_depth']}")

    # Visualisasi tree (dibatasi untuk sequence panjang)
    if len(sequence) <= 10:
        solver.print_tree()
    else:
        print("\n(Tree visualization skipped for long sequences)")

    # Metode 2: Dynamic Programming
    print("\n" + "-" * 70)
    print("METODE 2: DYNAMIC PROGRAMMING APPROACH")
    print("-" * 70)

    longest_seq_dp, length_dp = solver.solve_dp()

    print(f"\nLongest Monotonically Increasing Subsequence:")
    print(f"Sequence: {longest_seq_dp}")
    print(f"Length: {length_dp}")

    # Verifikasi kedua metode memberikan hasil yang sama
    print("\n" + "-" * 70)
    print("VERIFICATION")
    print("-" * 70)

    if length_tree == length_dp:
        print(f"Both methods agree: Length = {length_tree}")
        if set(longest_seq_tree) == set(longest_seq_dp):
            print("Sequences are equivalent (same elements)")
        else:
            print("Note: Different valid sequences with same length may exist")
    else:
        print("Warning: Methods produced different results!")

    # Visualisasi grafis
    print("\n" + "=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)

    try:
        import os
        os.makedirs('visualizations', exist_ok=True)

        # Visualisasi 1: Tree visualization
        print("\n1. Creating tree visualization...")
        solver.visualize_tree(highlight_path=longest_seq_dp, save_path='visualizations/tree_visualization.png')

        # Visualisasi 2: DP process
        print("2. Creating DP process visualization...")
        solver.visualize_dp_process(save_path='visualizations/dp_process.png')

        # Visualisasi 3: Comparison
        print("3. Creating comparison visualization...")
        solver.visualize_comparison(save_path='visualizations/comparison.png')

        print("\nAll visualizations have been generated successfully!")
        print("Files created in 'visualizations/' folder:")
        print("  - tree_visualization.png")
        print("  - dp_process.png")
        print("  - comparison.png")

    except ImportError as e:
        print(f"\nWarning: Could not generate visualizations.")
        print(f"Please install required packages: pip install matplotlib networkx")
        print(f"Error: {e}")

    # Test dengan contoh lain
    print("\n" + "=" * 70)
    print("ADDITIONAL TEST CASES")
    print("=" * 70)

    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]

    for i, test_seq in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_seq}")
        test_solver = LMISolver(test_seq)
        result, length = test_solver.solve_dp()
        print(f"LMIS: {result} (Length: {length})")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
