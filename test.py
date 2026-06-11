def process_user(users, user_id):

    user = users[user_id]

    if user["age"] > 18:
        return user["name"].upper()

    return None


def get_last_user(users):
    return users[-1]


def calculate_average(values):
    return sum(values) / len(values)
