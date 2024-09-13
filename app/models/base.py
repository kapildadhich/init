from tortoise import fields, models
from typing import ClassVar

class Base(models.Model):
    non_serializable_keys: ClassVar[set]= {"id", "updated_at", "created_at"}

    id = fields.IntField(pk=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add= True)

