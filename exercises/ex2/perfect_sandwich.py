"""KT exercises Perfect Sandwich"""


def perfect_sandwich(data: dict) -> str:
    """
    Docstring
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
        },

        3: {
            0: "rye toast",
            1: "smoked ham",
            2: "chopped lettuce",
            3: "pickled onions",
            4: "gouda cheese"
        }
    }
    """

    breads = {}
    toppings = {1: "", 2: "", 3: "", 4: ""}

    for entry in data.keys():

        if data[entry][0] in breads.keys():
            breads[data[entry][0]] += 1
            continue

        breads[data[entry][0]] = 1

    for layer in [1, 2, 3, 4]:
        temp = []

        for entry in data.keys():
            temp.append(data[entry][layer])

        for topping in sorted(temp, key=lambda x: temp.count(x)):
            toppings[layer] = f"{topping} {temp.count(topping)}"

    return f"Sandwich on a {max(breads.keys(), key=lambda x: breads[x])}, with {toppings[1].rpartition(' ')[0]}, {toppings[2].rpartition(' ')[0]}, {toppings[3].rpartition(' ')[0]} and {toppings[4].rpartition(' ')[0]}"
