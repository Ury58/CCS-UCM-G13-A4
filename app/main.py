#app/main.py

from fastapi import FastAPI
from app.auth.api.router import router as auth_router
#from app.files.api.router import router as files_router

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
     return {"status": "ok"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])
#app.include_router(files_router, prefix="/files", tags=["files"])
