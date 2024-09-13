import aioredis
from ..constants.config import CONFIG

class RedisClient:
    def __init__(self, host= CONFIG.config["REDIS_HOST"], port= CONFIG.config["REDIS_PORT"]):
        self.redis_url = f"redis://{host}:{port}"
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(self.redis_url)
                
    async def close(self):
        self.redis.close()

    async def set(self, key, value, expire = None):
        await self.connect()
        await self.redis.set(key, value, ex = expire)
        await self.close()

    async def get(self, key):
        await self.connect()
        value = await self.redis.get(key)
        await self.close()
        return value
