from tortoise import fields
from .base import Base
from typing import ClassVar

class NotesContentModel(Base):
    serializable_keys: ClassVar[set] = {"id", "notes_id", "heading", "preview", "content"}

    notes_id = fields.IntField()
    heading = fields.TextField()
    preview = fields.TextField()
    content = fields.TextField(null = True)

    class Meta:
        table = "notes_content"