
class BaseRepository:
    MODEL_CLASS = None

    @classmethod
    async def create(cls, payload):
        await cls.MODEL_CLASS.create(**payload)
       

    @classmethod
    async def get(cls, id):
        note = await cls.MODEL_CLASS.filter(id=id).first()
        return note