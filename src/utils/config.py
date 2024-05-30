import json
import os

__user_path = "../data/users/users.json"

__default = {'users': ['用户1'], 'last_user': '用户1'}


def load_user():
    if os.path.exists(__user_path):
        with open(__user_path, 'r') as f:
            data = json.load(f)
            return data.get('users')
    with open(__user_path, 'w') as f:
        json.dump(__default, f)
        return ["musician1"]


def add_user(username):
    user_list = load_user()
    if username not in user_list:
        user_list.append(username)
        with open(__user_path, 'w') as f:
            json.dump({"users": user_list, "last_user": username}, f)


def remove_user(username):
    user_list = load_user()
    if username in user_list:
        user_list.remove(username)
        with open(__user_path, 'w') as f:
            json.dump({"users": user_list, "last_user": "musician1"}, f)


def modify_user(old_name, new_name):
    if old_name == new_name:
        return
    user_list = load_user()
    if old_name in user_list and new_name not in user_list:
        user_list[user_list.index(old_name)] = new_name
        with open(__user_path, 'w') as f:
            json.dump({"users": user_list, "last_user": new_name}, f)


def get_record():
    with open(__user_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('last_user')


if __name__ == '__main__':
    print(load_user())
    add_user("musician2")
    print(load_user())
    add_user("musician3")
    print(load_user())
    add_user("musician4")
    print(load_user())
    remove_user("musician4")
    print(load_user())
    modify_user("musician3", "musician4")
    print(load_user())
    print(get_record())