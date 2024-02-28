import unittest

from internet_provider import database_update
from unittest import TestCase


database = {
        "michael": {
            "days_left": 40,
            "subscription_type": "Standard"
        },

        "sam": {
            "days_left": 362,
            "subscription_type": "Premium"
        },

        "peter": {
            "days_left": 1,
            "subscription_type": "Premium"
        }
    }


class TestUpdateDB(TestCase):
    def test_database_simple_add(self):
        this_database = database.copy()

        database_update(this_database, "add-crazy_mike-Premium")

        expected = {"days_left": 365, "subscription_type": "Premium"}
        actual = this_database.get("crazy_mike", None)
        self.assertEqual(expected, actual)

    def test_database_simple_remove_cannot(self):
        this_database = database.copy()

        expected = False
        actual = database_update(this_database, "remove-sam")

        self.assertEqual(expected, actual)

    def test_database_simple_remove_can(self):
        this_database = database.copy()

        expected = True
        actual = database_update(this_database, "remove-peter")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
