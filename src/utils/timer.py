from datetime import datetime
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def timer(func):
    """记录函数执行时间的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        duration = datetime.now() - start_time
        logger.info(f"{func.__name__} executed in {duration.total_seconds():.4f} seconds")
        return result
    return wrapper