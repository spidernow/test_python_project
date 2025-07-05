import json
from typing import Any, Dict

def parse_json(data: str) -> Dict[str, Any]:
    """安全解析 JSON 字符串"""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {}

def generate_uuid() -> str:
    """生成 UUID（需安装 uuid 库）"""
    import uuid
    return str(uuid.uuid4())

def validate_email(email: str) -> bool:
    """简单邮箱验证"""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None