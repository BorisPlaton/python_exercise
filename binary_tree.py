class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def add_child(self, child_value: int):
        """Добавляет ребенка"""

        if child_value < self.value:
            if self.left_child:
                return self.left_child.add_child(child_value)
            self.left_child = Node(child_value, self)
        else:
            if self.right_child:
                return self.right_child.add_child(child_value)
            self.right_child = Node(child_value, self)

    def find_child(self, child_value: int):
        """
        Ищет потомка

        В случае успеха возвращает экземпляр потомка, иначе возвращает None.
        """

        if child_value < self.value:
            return self.left_child.find_child(child_value) if self.left_child else None
        elif child_value == self.value:
            return self
        else:
            return self.right_child.find_child(child_value) if self.right_child else None


class Tree:

    def __init__(self, root=None):
        self.root = root

    def find_node(self, child_value: int):
        """
        Ищет узел в дереве

        В случае успеха возвращает экземпляр класса Node, иначе возвращает None.
        """

        if not self.root:
            return None

        return self.root.find_child(child_value)

    def view_tree(self, tab=3):
        """Выводит структуру дерево"""

        tab = tab
        if self.root:
            return self._check_tree(self.root, tab=tab)

    def add_node(self, value):
        """Добавляет узел в дерево"""

        if self.root:
            self.root.add_child(value)
        else:
            self.root = Node(value)

    def _check_tree(self, root, level=0, tab=2, additional_string=""):
        """Печатает узел и если есть, переходит к потомкам"""

        print(self._get_line(level, tab) + str(root.value) + additional_string)

        left_child = root.left_child
        right_child = root.right_child

        if left_child:
            self._check_tree(
                left_child,
                level + 1,
                tab,
                ' L'
            )

        if right_child:
            self._check_tree(
                right_child,
                level + 1,
                tab,
                ' R'
            )

    @staticmethod
    def _get_line(level, tab):

        if not level:
            return ""

        line_length = (level - 1) * tab

        return " " * line_length + "|__"


child_values = [5, 2, 3, 4, 9, 1]
tree = Tree()

for num in child_values:
    tree.add_node(num)

tree.view_tree()
elem = tree.find_node(35)
