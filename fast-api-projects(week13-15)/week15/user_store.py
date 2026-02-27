import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            return [json.loads(line) for line in f if line.strip()]

    def save(self, users):
        with open(self.file_path, "w") as f:
            for user in users:
                f.write(json.dumps(user) + "\n")

    def find_by_id(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None