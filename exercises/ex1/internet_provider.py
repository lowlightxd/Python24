"""KT Exercise Internet Provided."""


def remove_corrupted_users(database: dict) -> None:
    """
    Remove corrupted user entries from the database.

    Corruption is apparent when the user entry has an invalid subscription type.
    Valid subscription types are Standard and Premium (case-sensitive)
    """
    list_users_to_remove = []

    for user in database:
        if database[user]["subscription_type"] not in ["Standard", "Premium"]:
            list_users_to_remove.append(user)

    for user in list_users_to_remove:
        database.pop(user)


def database_update(database: dict, command_string: str) -> bool:
    """
    Update database.

    Keys are usernames and values are dicts with values: days_left and subscription_type.

    Example of how a database looks like
    db = {
    "michael": {
            "days_left": 40,
            "subscription_type": "Standard"
        },

        "sam": {
            "days_left": 362,
            "subscription_type": "Premium"
        }
    }
    "michael" and "sam" are users and "days_left", "subscription_type" are their properties

    You need to parse the command string to modify the database.

    For example:
        command string -> "add-crazy_mike-Premium"
        will add a new user with the name "crazy_mike" to the database, and the "days_left"
        value will be of 365, "subscription_type" will be of "Premium".
        since the modification was performed it is successful

        add, remove, subscription_type keywords should be case-insensitive.
        In the resulting database, subscription types should be capitalised.

    Another example:
        command string -> "add-sam-Standard"
        since there is already an entry with the key "sam" in the database,
        the command should not be executed, and the modification is unsuccessful

    return True if modification was successful and False otherwise
    """

    command_list = command_string.split("-")
    user_name = command_list[1]
    command = command_list[0]
    subscription = None

    if len(command_list) == 3:
        subscription = command_list[2]

    if command.casefold() == "add" and user_name not in database.keys():
        database.update({user_name:
                        {"days_left": 90 if subscription.casefold == "standard" else 365,
                            "subscription_type": subscription.capitalize()}})
        remove_corrupted_users(database)
        return True

    if command.casefold() == "remove" and user_name in database.keys() and database[user_name]["days_left"] <= 1:
        database.pop(user_name)
        remove_corrupted_users(database)
        return True

    return False
