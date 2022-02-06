from __future__ import annotations

from copy import copy, deepcopy
from dataclasses import dataclass
from typing import Any, Optional


class BinarySearchTree:
    @dataclass
    class Node:
        key: Any
        value: Any
        left: Optional[BinarySearchTree.Node] = None
        right: Optional[BinarySearchTree.Node] = None

    def __init__(self):
        self._root: Optional[BinarySearchTree.Node] = None

    def set_item(self, key, value):
        if self._root is None:
            self._root = self.Node(key, value)
            return

        current_node = self._root
        while True:
            if current_node.key == key:
                current_node.value = value
                return

            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = self.Node(key, value)
                    return

                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = self.Node(key, value)
                    return

                current_node = current_node.right

    def get_item(self, key, default=None):
        if self._root is None:
            return default

        current_node = self._root
        while True:
            if current_node.key == key:
                return current_node.value

            if key < current_node.key:
                if current_node.left is None:
                    return default

                current_node = current_node.left
            else:
                if current_node.right is None:
                    return default

                current_node = current_node.right

    def remove_item(self, key):
        if self._root is None:
            return
        if self._root.key == key:
            node_to_insert = self._root.left
            self._root = self._root.right
            if node_to_insert:
                self.set_item(node_to_insert.key, node_to_insert.value)

            return

        for node in self.traverse('pre', values_only=False):
            if node.left and node.left.key == key:
                parent = node
                node = parent.left

                if node.left and node.right:
                    node_to_insert = node.left
                    parent.left = node.right
                    self.set_item(node_to_insert.key, node_to_insert.value)
                elif node.left:
                    parent.left = node.left
                else:
                    parent.left = node.right

                return
            elif node.right and node.right.key == key:
                parent = node
                node = parent.right

                if node.left and node.right:
                    node_to_insert = node.right
                    parent.right = node.right
                    self.set_item(node_to_insert.key, node_to_insert.value)
                elif node.left:
                    parent.right = node.left
                else:
                    parent.right = node.right

                return

    def has_key(self, key):
        for node in self.traverse('pre', values_only=False):
            if node.key == key:
                return True

        return False

    def traverse(self, order: str, root: Optional[BinarySearchTree.Node] = None, values_only: bool = True):
        """Generator to traverse the tree

        Possible traversal orders:
        'pre': root, left, right
        'post': left, right, root
        'in': left, root, right
        'pre reversed': root, right, left
        'post reversed': right, left, root
        'in reversed': right, root, left

        :param order: The order in which to traverse the tree. See possible traversal orders above.
        :param root: The root of the tree to traverse. Defaults to the root node of this tree.
        :param values_only: If True, only the value held in each node will be yielded. Else, the node objects will be
            yielded. Defaults to True.
        """
        if self._root is None:
            return
        if root is None:
            root = self._root

        orders = {
            'pre': ('root', 'left', 'right'),
            'post': ('left', 'right', 'root'),
            'in': ('left', 'root', 'right'),
            'pre reversed': ('root', 'right', 'left'),
            'post reversed': ('right', 'left', 'root'),
            'in reversed': ('right', 'root', 'left')
        }

        for node_name in orders[order]:
            if node_name == 'root':
                yield root.value if values_only else root
            elif node_name == 'left' and root.left is not None:
                yield from self.traverse(order, root.left, values_only=values_only)
            elif node_name == 'right' and root.right is not None:
                yield from self.traverse(order, root.right, values_only=values_only)

    @classmethod
    def _copy(cls, root: Optional[BinarySearchTree.Node]):
        if root is None:
            return None

        result = cls.Node(root.key, root.value)
        result.left = cls._copy(root.left)
        result.right = cls._copy(root.right)

        return result

    def __copy__(self):
        result = BinarySearchTree()
        result._root = self._copy(self._root)
        return result

    def __deepcopy__(self, memodict=None):
        memodict = memodict or {}

        result = copy(self)
        for node in result.traverse('pre', values_only=False):
            node.key = deepcopy(node.key, memodict)
            node.value = deepcopy(node.value, memodict)

        return result
