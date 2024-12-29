# -*- coding: utf-8 -*-

class Chord:
    def __init__(self, nodes):
        self.nodes = sorted(nodes)

    def find_successor(self, key):
        """
        Tìm successor của khóa key trong danh sách self.nodes
        """
        for node_id in self.nodes:
            if key <= node_id:
                return node_id
        return self.nodes[0]

    def add_node(self, new_node):
        """
        Thêm nút mới vào vòng Chord
        """
        self.nodes.append(new_node)
        self.nodes.sort()


if __name__ == "__main__":
    nodes = [0, 14, 21, 32, 38, 42, 48, 56, 60]
    chord = Chord(nodes)
    keys = [10, 24, 30, 38, 54]

    print("=== Trước khi thêm nút 26 ===")
    for key in keys:
        successor = chord.find_successor(key)
        print(f"Key {key:2d} -> Successor: {successor}")

    new_node = 26
    chord.add_node(new_node)

    print("\n=== Sau khi thêm nút 26 ===")
    for key in keys:
        successor = chord.find_successor(key)
        print(f"Key {key:2d} -> Successor: {successor}")



