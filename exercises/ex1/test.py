import pytest

from internet_provider import database_update


database1 = {
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

database2 = {
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
        },

        "anna": {
            "days_left": 23,
            "subscription_type": "premium"
        }
}


def test_database_simple_add():
    this_database = database1.copy()

    database_update(this_database, "add-crazy_mike-Premium")

    expected = {"days_left": 365, "subscription_type": "Premium"}
    actual = this_database.get("crazy_mike", None)
    assert expected == actual


def test_database_simple_remove_cannot():
    this_database = database1.copy()

    expected = False
    actual = database_update(this_database, "remove-sam")

    assert expected == actual


def test_database_simple_remove_can():
    this_database = database1.copy()

    expected = True
    actual = database_update(this_database, "remove-peter")

    assert expected == actual


def test_database_add_removes_corrupted_entries():
    this_database = database2.copy()
    database_update(this_database, "add-kevin-Standard")

    expected = True
    actual = "anna" not in this_database.keys()

    assert expected == actual


def test_database_remove_removes_corrupted_entries():
    this_database = database2.copy()
    database_update(this_database, "remove-peter")

    expected = True
    actual = "anna" not in this_database.keys()

    assert expected == actual
