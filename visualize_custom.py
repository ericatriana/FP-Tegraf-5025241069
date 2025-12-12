"""
Script untuk membuat visualisasi kustom dari sequence yang diinginkan
Anda dapat memodifikasi sequence di bawah ini untuk membuat visualisasi sendiri
"""

from lmis import LMISolver

def visualize_custom_sequence(sequence, prefix='custom'):
    """
    Membuat visualisasi dari sequence kustom

    Args:
        sequence: List of integers untuk dianalisis
        prefix: Prefix nama file output
    """
    print("=" * 70)
    print(f"Visualizing Custom Sequence: {sequence}")
    print("=" * 70)

    # Inisialisasi solver
    solver = LMISolver(sequence)

    # Solve dengan DP
    longest_seq, length = solver.solve_dp()

    print(f"\nLongest Monotonically Increasing Subsequence:")
    print(f"Sequence: {longest_seq}")
    print(f"Length: {length}")

    # Build tree untuk visualisasi
    solver.build_tree()
    stats = solver.get_statistics()

    print(f"\nTree Statistics:")
    print(f"- Total nodes: {stats['total_nodes']}")
    print(f"- Max depth: {stats['max_depth']}")

    # Generate visualizations
    print(f"\nGenerating visualizations with prefix '{prefix}'...")

    try:
        import os
        os.makedirs('visualizations', exist_ok=True)

        # Tree visualization
        tree_path = f'visualizations/{prefix}_tree.png'
        solver.visualize_tree(highlight_path=longest_seq, save_path=tree_path)
        print(f"1. Tree visualization saved to: {tree_path}")

        # DP process
        dp_path = f'visualizations/{prefix}_dp.png'
        solver.visualize_dp_process(save_path=dp_path)
        print(f"2. DP process saved to: {dp_path}")

        # Comparison
        comp_path = f'visualizations/{prefix}_comparison.png'
        solver.visualize_comparison(save_path=comp_path)
        print(f"3. Comparison saved to: {comp_path}")

        print("\nAll visualizations generated successfully!")

    except Exception as e:
        print(f"Error generating visualizations: {e}")

    print("=" * 70)


if __name__ == "__main__":
    # Contoh 1: Sequence dari tugas praktikum
    print("\nEXAMPLE 1: Praktikum Sequence")
    sequence1 = [4, 1, 13, 7, 0, 2, 8, 11, 3]
    visualize_custom_sequence(sequence1, prefix='praktikum')

    # Contoh 2: Sequence dengan banyak kemungkinan
    print("\n\nEXAMPLE 2: Multiple Possibilities")
    sequence2 = [10, 9, 2, 5, 3, 7, 101, 18]
    visualize_custom_sequence(sequence2, prefix='multiple')

    # Contoh 3: Sequence yang sudah sorted
    print("\n\nEXAMPLE 3: Already Sorted")
    sequence3 = [1, 2, 3, 4, 5, 6, 7]
    visualize_custom_sequence(sequence3, prefix='sorted')

    # Contoh 4: Sequence dengan duplikat
    print("\n\nEXAMPLE 4: With Duplicates")
    sequence4 = [1, 3, 2, 3, 4, 2, 5]
    visualize_custom_sequence(sequence4, prefix='duplicates')

    # Untuk sequence kustom Anda sendiri, uncomment baris di bawah:
    # print("\n\nCUSTOM SEQUENCE")
    # my_sequence = [5, 2, 8, 6, 3, 6, 9, 7]  # Ganti dengan sequence Anda
    # visualize_custom_sequence(my_sequence, prefix='my_custom')

    print("\n" + "=" * 70)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 70)
    print("\nCheck the generated PNG files in the current directory.")
    print("You can open them with any image viewer.")
