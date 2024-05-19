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

# @app.post("/post_example")
# async def post_example_function(post_input: dict) -> dict[str, str]:
#     return {
#         "status": "ok",
#         "type": "post",
#         "additional_parameter": "additional_parameter_value",
#         "input_content": post_input
#     }

# @app.post("/post_example_with_parameter/{parameter}")
# async def post_example_with_parameter_function(parameter: str, post_with_parameter_input: dict) -> dict[str, str]:
#     return {
#         "parameter": parameter,
#         "input_content": post_with_parameter_input,
#     }


# @app.delete("/delete_example/{parameter}")
# async def delete_example(parameter: str) -> dict[str, str]:
#     return {
#         "parameter": parameter
#     }
