from fastapi import FastAPI
from .routes.api import router as api_router
from .utils.logger import setup_logger

# 初始化日志
setup_logger()

app = FastAPI(
    title="My FastAPI App",
    description="A demo FastAPI project with logging and timing decorators",
    version="0.1.0",
)

# 注册路由
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to My FastAPI App!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")