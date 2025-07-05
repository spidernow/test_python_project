import asyncio
from fastapi import APIRouter
from ..utils.logger import log_execution_time, timer

router = APIRouter()

@router.get("/hello")
@log_execution_time  # 使用日志装饰器
async def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@router.get("/calculate")
@timer  # 使用单独的计时装饰器
async def calculate(x: int, y: int):
    """模拟耗时计算"""
    await asyncio.sleep(1)
    return {"result": x + y}