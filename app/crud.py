fake_users_db = {}

def get_user_by_username(username: str):
    return fake_users_db.get(username)

