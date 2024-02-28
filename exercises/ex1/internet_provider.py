"""KT Exercise Internet Provided."""


def database_update(database: dict, command_string: str) -> bool:
    """
    Update database.

    Keys are usernames and values are dicts with values: days_left and subscription_type.

    Example of how a database looks like
    {
    "michael": {
            "days_left": 40,
            "subscription_type": "Standard"
        },

        "sam": {
            "days_left": 362,
            "subscription_type": "Premium"
        }
    }

    You need to parse the command string to modify the database.

    For example:
        command string -> "add-crazy_mike-Premium"
        will add a new user with the name "crazy_mike" to the database, and the "days_left"
        value will be of 365, "subscription_type" will be of "Premium"

    return True if modification was successful and False otherwise
    """
    command_list = command_string.split("-")
    user_name = command_list[1]
    command = command_list[0]
    subscription = None
    if len(command_list) == 3:
        subscription = command_list[2]

    if command == "add" and user_name not in database.keys():
        database.update({user_name:
                        {"days_left": 90 if subscription == "Standard" else 365, "subscription_type": subscription}})
        return True
    if command == "remove" and user_name in database.keys() and database[user_name]["days_left"] <= 1:
        database.pop(user_name)
        return True
    return False
