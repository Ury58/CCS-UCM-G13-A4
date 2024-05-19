#app/main.py

from fastapi import FastAPI
from app.auth.api.router import router as test2_router
from app.files.api.router import router as test_router

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
     return {"status": "ok"}

app.include_router(test_router, prefix="/files", tags=["files"])
app.include_router(test2_router, prefix="/auth", tags=["auth"])