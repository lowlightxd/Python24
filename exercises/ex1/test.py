import pytest

from internet_provider import database_update


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


def test_database_simple_add():
    this_database = database.copy()

    database_update(this_database, "add-crazy_mike-Premium")

    expected = {"days_left": 365, "subscription_type": "Premium"}
    actual = this_database.get("crazy_mike", None)
    assert expected == actual


def test_database_simple_remove_cannot():
    this_database = database.copy()

    expected = False
    actual = database_update(this_database, "remove-sam")

    assert expected == actual


def test_database_simple_remove_can():
    this_database = database.copy()

    expected = True
    actual = database_update(this_database, "remove-peter")

    assert expected == actual
