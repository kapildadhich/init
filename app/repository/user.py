from .base import BaseRepository
from ..models.user import UserModel


class UserRepository(BaseRepository):
    MODEL_CLASS = UserModel

    @classmethod
    async def get_by_gmail(cls, gmail):
        note = await cls.MODEL_CLASS.filter(gmail=gmail).first()
        return note