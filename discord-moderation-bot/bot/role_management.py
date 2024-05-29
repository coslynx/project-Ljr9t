role_management.py (Python):

class RoleManagement:
    def __init__(self):
        self.roles = {}

    def assign_role(self, user_id, role_name):
        if user_id in self.roles:
            self.roles[user_id].append(role_name)
        else:
            self.roles[user_id] = [role_name]

    def remove_role(self, user_id, role_name):
        if user_id in self.roles and role_name in self.roles[user_id]:
            self.roles[user_id].remove(role_name)
        else:
            print("User or role not found.")

    def get_user_roles(self, user_id):
        if user_id in self.roles:
            return self.roles[user_id]
        else:
            return []

    def get_all_roles(self):
        return self.roles

# Example of how to use the RoleManagement class
role_manager = RoleManagement()
role_manager.assign_role("123456789", "Moderator")
role_manager.assign_role("987654321", "Admin")
print(role_manager.get_user_roles("123456789"))
print(role_manager.get_all_roles())