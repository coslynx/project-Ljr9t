# user_management.py (Python)

class UserManagement:
    
    def __init__(self):
        self.users = {}  # Store user data
    
    def add_user(self, user_id, username):
        if user_id not in self.users:
            self.users[user_id] = username
            return True
        return False
    
    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
    
    def get_user(self, user_id):
        return self.users.get(user_id, None)
    
    def get_all_users(self):
        return self.users.items()
    
    def update_username(self, user_id, new_username):
        if user_id in self.users:
            self.users[user_id] = new_username
            return True
        return False

# End of user_management.py