"""Database helpers for the DevForge demo."""


class UserStore:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        self.users[user_id] = name

    def get_user(self, user_id):
        # TODO: return a clear error for unknown users.
        return self.users.get(user_id)

    def delete_user(self, user_id):
        return self.users.pop(user_id)
