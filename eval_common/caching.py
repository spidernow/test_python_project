import redis.asyncio as redis
from typing import Optional

REDIS_URL = "redis://localhost:6379/0"

class RedisCache:
    def __init__(self):
        self.redis_client = None

    async def connect(self):
        """初始化 Redis 连接"""
        self.redis_client = redis.from_url(REDIS_URL)

    async def set(self, key: str, value: str, expire: int = 60):
        """设置缓存"""
        await self.redis_client.set(key, value, ex=expire)

    async def get(self, key: str) -> Optional[str]:
        """获取缓存"""
        return await self.redis_client.get(key)

    async def close(self):
        """关闭连接"""
        await self.redis_client.close()

# 全局缓存实例
cache = RedisCache()