import json
import os

__user_path = "../data/users/users.json"

__default = {'users': ['用户1'], 'last_user': '用户1'}


def load_user():
    if os.path.exists(__user_path):
        with open(__user_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('users')
    with open(__user_path, 'w', encoding='utf-8') as f:
        json.dump(__default, f)
        return ["用户1"]


def add_user(username):
    user_list = load_user()
    if username not in user_list:
        user_list.append(username)
        with open(__user_path, 'w', encoding='utf-8') as f:
            json.dump({"users": user_list, "last_user": username}, f)


def remove_user(username):
    user_list = load_user()
    if username in user_list:
        user_list.remove(username)
        with open(__user_path, 'w', encoding='utf-8') as f:
            if len(user_list) == 0:
                last_user = "用户1"
                user_list.append(last_user)
            else:
                last_user = user_list[0]
            json.dump({"users": user_list, "last_user": last_user}, f)


def modify_user(old_name, new_name):
    if old_name == new_name:
        return
    user_list = load_user()
    if old_name in user_list and new_name not in user_list:
        user_list[user_list.index(old_name)] = new_name
        with open(__user_path, 'w', encoding='utf-8') as f:
            json.dump({"users": user_list, "last_user": new_name}, f)


def get_record():
    if not os.path.exists(__user_path):
        with open(__user_path, 'w', encoding='utf-8') as f:
            json.dump(__default, f)
    with open(__user_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('last_user')
