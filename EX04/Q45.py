class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key

    def insert(self, value):

        new_key = self.key(value)

        if self.root is None:
            self.root = Node(value)
            return

        current = self.root

        while True:
            cur_key = self.key(current.value)

            if new_key < cur_key:
                # לכיוון שמאל
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                # לכיוון ימין (כולל שוויון)
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right




# תרגיל 5

def build_mermaid(node, node_id, lines):
    # מדפיסים את הצומת עצמו
    lines.append(f"{node_id}(({node.value}))")

    left_id = node_id + "l"
    right_id = node_id + "r"

    # בן שמאלי
    if node.left:
        lines.append(f"{node_id} --> {left_id}")
        build_mermaid(node.left, left_id, lines)
    elif node.right:
        # אין שמאל אבל יש ימין – מוסיפים צומת ריק
        lines.append(f"{node_id} ~~~ {left_id}")
        lines.append(f"{left_id}(( ))")
        lines.append(f"style {left_id} fill:#fff,stroke-width:0px")

    # בן ימני
    if node.right:
        lines.append(f"{node_id} --> {right_id}")
        build_mermaid(node.right, right_id, lines)
    elif node.left:
        # יש שמאל ואין ימין – מוסיפים צומת ריק
        lines.append(f"{node_id} ~~~ {right_id}")
        lines.append(f"{right_id}(( ))")
        lines.append(f"style {right_id} fill:#fff,stroke-width:0px")


def tree_to_mermaid(tree: Tree) -> str:
    if tree.root is None:
        return "graph TD"

    lines = ["graph TD"]
    build_mermaid(tree.root, "t", lines)
    return "\n".join(lines)


def main():
    tree = Tree()

    # בונים את אותו העץ כמו בדוגמה בשאלה
    for n in [10, 2, 16, 4, 15, 17, 20]:
        tree.insert(n)

    mermaid = tree_to_mermaid(tree)
    print(mermaid)


if __name__ == "__main__":
    main()