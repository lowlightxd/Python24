import pytest
from perfect_sandwich import perfect_sandwich

data1 = {
    1: {
        0: "rye toast",
        1: "smoked ham",
        2: "mayonnaise",
        3: "pickled onions",
        4: "Parmesan cheese"
    },

    2: {
        0: "white toast",
        1: "fried chicken",
        2: "chopped lettuce",
        3: "salad dressing",
        4: "gouda cheese"
    },

    3: {
        0: "rye toast",
        1: "smoked ham",
        2: "chopped lettuce",
        3: "pickled onions",
        4: "Parmesan cheese"
    },

    4: {
        0: "rye toast",
        1: "smoked ham",
        2: "chopped lettuce",
        3: "pickled onions",
        4: "Parmesan cheese"
    },

    5: {
        0: "white american bread",
        1: "ham",
        2: "garlic sauce",
        3: "fried onions",
        4: "gouda cheese"
    }
}


def test_perfect_sandwich():
    data = data1.copy()

    expected = "Sandwich on a rye toast, with smoked ham, chopped lettuce, pickled onions and Parmesan cheese"
    actual = perfect_sandwich(data)

    assert expected == actual

