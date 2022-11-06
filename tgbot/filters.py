import aiogram.types
import aiogram.dispatcher.filters
import bot


class UserStatus(aiogram.dispatcher.filters.BoundFilter):
    key = "check_by"

    def __init__(self, check_by):
        self.check_by = check_by

    async def check(self, message: aiogram.types.Message):
        return self.check_by in bot.user_status.get(message.from_user.id, '')
