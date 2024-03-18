"""KT exercises Perfect Sandwich"""


def perfect_sandwich(data: dict) -> str:
    """
    Fetch the given data and figure out which toppings create a perfect sandwich.

    Example of data:
    data = {
        1: {
            0: "rye toast",
            1: "smoked ham",
            2: "mayonnaise",
            3: "pickled onions"
            4: "Parmesan cheese"
        },

        2: {
            0: "white toast",
            1: "fried chicken",
            2: "chopped lettuce",
            3: "salad dressing",
            4: "gouda cheese"
        }

        3: {
            0: "rye toast",
            1: "smoked ham",
            2: "chopped lettuce",
            3: "pickled onions",
            4: "gouda cheese"
        }
    }

    For each layer there would be the most used topping, that is the perfect topping for the given layer. When
    you figure out the most used bread, that is the perfect bread for the sandwich. Result will be the sandwich
    constructed on a perfect bread, with perfect toppings in order from layer 1 to 4. If there are two candidates
    for the perfect topping, then the one that occurred first will be chosen.
    Resulting string should have the following format:

        'Sandwich on a [bread] with [layer_0_perfect_topping], [layer_1_perfect_topping], [layer_3_perfect_topping] and
        [layer_0_perfect_topping]'
    """

    return "Perfect sandwich"
