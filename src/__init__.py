"""
My Python Project - FastAPI Application
"""
__version__ = "0.1.0"
__author__ = "Your Name"

# 导入子模块（可选）
from .main import app
from .utils.logger import log_execution_time
from .utils.timer import timer