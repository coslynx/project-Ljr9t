# File: moderation.py (Python)

class ModerationBot:
    def __init__(self):
        self.profane_words = ['bad_word1', 'bad_word2']
        self.users_warnings = {}
    
    def filter_message(self, message):
        for word in self.profane_words:
            if word in message:
                return True
        return False
    
    def warn_user(self, user_id):
        if user_id in self.users_warnings:
            self.users_warnings[user_id] += 1
            if self.users_warnings[user_id] == 3:
                self.mute_user(user_id)
        else:
            self.users_warnings[user_id] = 1
    
    def mute_user(self, user_id):
        # Logic to mute user
        pass
    
    def kick_user(self, user_id):
        # Logic to kick user
        pass
    
    def ban_user(self, user_id):
        # Logic to ban user
        pass

# Instantiate the ModerationBot class
bot = ModerationBot()

# Sample usage
message = "Hey, watch your language!"
if bot.filter_message(message):
    bot.warn_user(user_id)