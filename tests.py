import unittest
from copy import copy, deepcopy

import binary_search_tree


class BinarySearchTreeTestCase(unittest.TestCase):
    def test_read_from_empty_tree(self):
        tree = binary_search_tree.BinarySearchTree()

        actual = tree.get_item(0)

        expected = None
        self.assertEqual(expected, actual)

    def test_get_item_from_tree_of_size_one(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 1)

        actual = tree.get_item(0)

        expected = 1
        self.assertEqual(expected, actual)

    def test_get_item_from_tree_with_several_nodes(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 1)
        tree.set_item(1, 2)
        tree.set_item(2, 3)
        tree.set_item(0.5, 4)
        tree.set_item(-1, 5)

        actual = tree.get_item(2)

        expected = 3
        self.assertEqual(expected, actual)

    def test_overwrite_item(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 1)
        tree.set_item(1, 2)
        tree.set_item(0, 3)

        actual = tree.get_item(0)

        expected = 3
        self.assertEqual(expected, actual)

    def test_copy(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.set_item(100, 'b')
        tree.set_item(-100, 'c')

        tree_copy = copy(tree)
        tree_copy.set_item(0, 'd')

        actual = tree.get_item(0)

        expected = 'a'
        self.assertEqual(expected, actual)

    def test_deepcopy(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.set_item(100, 'b')
        tree.set_item(-100, ['c', 'd', 'e'])

        tree_copy = deepcopy(tree)
        tree_copy.get_item(-100)[0] = 'z'

        actual = tree.get_item(-100)[0]

        expected = 'c'
        self.assertEqual(expected, actual)

    def test_remove_node_from_tree_of_size_one(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.remove_item(0)

        actual = tree.get_item(0)

        expected = None
        self.assertEqual(expected, actual)

    def test_remove_node_from_tree_with_several_nodes(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.set_item(1, 'b')
        tree.set_item(2, 'c')
        tree.set_item(-1, 'd')
        tree.set_item(1.5, 'e')
        tree.remove_item(1.5)

        actual = tree.get_item(1.5)

        expected = None
        self.assertEqual(expected, actual)

    def test_get_item_after_removing_node(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.set_item(1, 'b')
        tree.set_item(2, 'c')
        tree.set_item(-1, 'd')
        tree.set_item(1.5, 'e')
        tree.remove_item(1.5)

        actual = tree.get_item(2)

        expected = 'c'
        self.assertEqual(expected, actual)

    def test_pre_order_traversal(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.set_item(1, 'c')
        tree.set_item(2, 'd')
        tree.set_item(-1, 'b')
        tree.set_item(1.5, 'e')

        actual = list(tree.traverse('pre'))

        expected = ['a', 'b', 'c', 'd', 'e']
        self.assertListEqual(expected, actual)

    def test_in_order_traversal(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'b')
        tree.set_item(1, 'c')
        tree.set_item(2, 'e')
        tree.set_item(-1, 'a')
        tree.set_item(1.5, 'd')

        actual = list(tree.traverse('in'))

        expected = ['a', 'b', 'c', 'd', 'e']
        self.assertListEqual(expected, actual)

    def test_post_order_traversal(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'e')
        tree.set_item(1, 'd')
        tree.set_item(2, 'c')
        tree.set_item(-1, 'a')
        tree.set_item(1.5, 'b')

        actual = list(tree.traverse('post'))

        expected = ['a', 'b', 'c', 'd', 'e']
        self.assertListEqual(expected, actual)

    def test_reversed_pre_order_traversal(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'a')
        tree.set_item(1, 'b')
        tree.set_item(2, 'c')
        tree.set_item(-1, 'e')
        tree.set_item(1.5, 'd')

        actual = list(tree.traverse('pre reversed'))

        expected = list(['a', 'b', 'c', 'd', 'e'])
        self.assertListEqual(expected, actual)

    def test_reversed_in_order_traversal(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'd')
        tree.set_item(1, 'c')
        tree.set_item(2, 'a')
        tree.set_item(-1, 'e')
        tree.set_item(1.5, 'b')

        actual = list(tree.traverse('in reversed'))

        expected = list(['a', 'b', 'c', 'd', 'e'])
        self.assertListEqual(expected, actual)

    def test_reversed_post_order_traversal(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'e')
        tree.set_item(1, 'c')
        tree.set_item(2, 'b')
        tree.set_item(-1, 'd')
        tree.set_item(1.5, 'a')

        actual = list(tree.traverse('post reversed'))

        expected = list(['a', 'b', 'c', 'd', 'e'])
        self.assertListEqual(expected, actual)

    def test_check_for_present_key(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'e')
        tree.set_item(1, 'd')
        tree.set_item(2, 'c')
        tree.set_item(-1, 'a')
        tree.set_item(1.5, 'b')

        actual = tree.has_key(-1)

        expected = True
        self.assertEqual(expected, actual)

    def test_check_for_not_present_key(self):
        tree = binary_search_tree.BinarySearchTree()
        tree.set_item(0, 'e')
        tree.set_item(1, 'd')
        tree.set_item(2, 'c')
        tree.set_item(-1, 'a')
        tree.set_item(1.5, 'b')

        actual = tree.has_key(-2)

        expected = False
        self.assertEqual(expected, actual)

    def test_traverse_empty_tree(self):
        tree = binary_search_tree.BinarySearchTree()

        actual = list(tree.traverse('in'))

        expected = []
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
