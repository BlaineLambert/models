import unittest
from run import create_item, read_all_items, search_items, read_item_by_id, update_item, delete_item

class TestCRUDFunctions(unittest.TestCase):
    def test_create_item(self):
        items = []
        new_item = create_item(items, "Test Item", "Description")
        self.assertEqual(new_item.name, "Test Item")
        self.assertEqual(new_item.description, "Description")

if __name__ == '__main__':
    unittest.main()
