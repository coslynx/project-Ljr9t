# warning_system.py (Python)

# Import necessary libraries
import discord

class WarningSystem:
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}

    async def warn_user(self, user_id, reason):
        if user_id not in self.warnings:
            self.warnings[user_id] = []
        self.warnings[user_id].append(reason)
        await self.bot.send_message(discord.User(id=user_id), f"You have been warned for: {reason}")

    async def check_warnings(self, user_id):
        if user_id in self.warnings:
            return len(self.warnings[user_id])
        return 0

    async def clear_warnings(self, user_id):
        if user_id in self.warnings:
            del self.warnings[user_id]
            await self.bot.send_message(discord.User(id=user_id), "Your warnings have been cleared.")

    async def display_warnings(self, user_id):
        if user_id in self.warnings:
            warnings = self.warnings[user_id]
            message = "Your warnings:\n"
            for idx, warning in enumerate(warnings, start=1):
                message += f"{idx}. {warning}\n"
            await self.bot.send_message(discord.User(id=user_id), message)
        else:
            await self.bot.send_message(discord.User(id=user_id), "You have no warnings.")

    async def remove_warning(self, user_id, warning_number):
        if user_id in self.warnings and warning_number <= len(self.warnings[user_id]):
            del self.warnings[user_id][warning_number - 1]
            await self.bot.send_message(discord.User(id=user_id), f"Warning {warning_number} has been removed.")
        else:
            await self.bot.send_message(discord.User(id=user_id), "Invalid warning number.")