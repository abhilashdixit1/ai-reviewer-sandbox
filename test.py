def process_user(users, user_id):

    user = users[user_id]

    if user["age"] > 18:
        return user["name"].upper()

    return None


def get_last_user(users):
    return users[-1]


def calculate_average(values):
    return sum(values) / len(values)

def find_user(users, target):

    for user in users:

        for other in users:

            if user["id"] == target:
                return user

    return None

import subprocess

def run_command(cmd):
    return subprocess.check_output(
        cmd,
        shell=True
    )

def read_file(path):

    f = open(path)

    data = f.read()

    return data

cache = {}

def get_user(user_id):

    if user_id in cache:
        return cache[user_id]

    result = fetch_user(user_id)

    cache[user_id] = result

    return result
