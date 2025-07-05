import logging
from functools import wraps
from datetime import datetime
import time

# 配置日志
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger(__name__)

# 日志装饰器（记录函数执行）
def log_execution_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Executing {func.__name__}...")
        result = await func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Finished {func.__name__} in {end_time - start_time:.4f}s")
        return result
    return wrapper

# 单独的时间装饰器（可复用）
def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = datetime.now()
        result = await func(*args, **kwargs)
        duration = datetime.now() - start
        logger.info(f"{func.__name__} took {duration.total_seconds():.4f}s")
        return result
    return wrapper