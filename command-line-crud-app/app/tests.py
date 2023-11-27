from django.test import TestCase
from app import models


# Create your tests here.

class TestCRUDFunctions(TestCase):
    def test_create_item(self):
        test = models.create_item('testing one', 'testing one desc')
        self.assertEqual(test.name, 'testing one')
        self.assertEqual(test.description, 'testing one desc')

    def test_read_all(self):
        test = models.create_item('testing one', 'testing one desc')
        testtwo = models.create_item('testing two', 'testing two desc')
        testthree = models.create_item('testing three', 'testing three desc')

        allvar = models.read_all_items()

        self.assertEqual(len(allvar), 3)

    def test_search_items(self):
        test = models.create_item('testing one', 'testing one desc')
        testtwo = models.create_item('testing two', 'testing two desc')
        testthree = models.create_item('testing three', 'testing three desc')

        var = models.search_items("testing two")

        self.assertEqual(var.name, 'testing two')

    def test_search_item_by_id(self):
        test = models.create_item('testing one', 'testing one desc')
        testtwo = models.create_item('testing two', 'testing two desc')
        testthree = models.create_item('testing three', 'testing three desc')

        var = models.search_items("testing two")

        self.assertEqual(var.id, 2)

    def test_update_item(self):
        test = models.create_item('testing two', 'testing two desc')
        test = models.update_item('testing two', 'thanks micah')

        self.assertEqual(test.description, 'thanks micah')

    def test_delete_item(self):
        test = models.create_item('hello', 'hello desc')
        testtwo = models.create_item('hello', 'hello desc')
        testthree = models.create_item('hello', 'hello desc')
        test = models.delete_item(1)

        self.assertEqual(len(models.read_all_items()), 2)

