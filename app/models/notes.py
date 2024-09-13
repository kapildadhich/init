from tortoise import fields
from .base import Base
from typing import ClassVar

class NotesModel(Base):
    serializable_keys: ClassVar[set] = {"id", "user_id", "heading", "preview", "update_time_key"}

    user_id = fields.IntField()
    heading = fields.TextField()
    preview = fields.TextField()
    update_time_key =  fields.IntField()

    class Meta:
        table = "notes"