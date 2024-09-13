from tortoise import fields
from .base import Base
from typing import ClassVar

class UserModel(Base):
    serializable_keys: ClassVar[set] = {"id", "gmail", "name"}

    gmail = fields.TextField()
    name= fields.TextField()

    class Meta:
        table = "users"