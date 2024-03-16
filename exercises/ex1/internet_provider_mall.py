"""KT Exercise Internet Provided."""


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
    return True
