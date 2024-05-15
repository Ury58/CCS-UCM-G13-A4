from fastapi import FastAPI
from app.auth.router import router as test2
from app.files.router import router as test1

tags_metadata[
    {
        "name": "test1"
        "description": "desc test1"
    }
    {
        "name": "auth"
        "description": "A4 auth"
    }
]


app = FastAPI(
    Title="A4"
    Description="Activity 4"
    tags_metadata=tags_metadata
)

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
     return {"status": "ok"}

app.include_router(test_router, prefix="/files", tags=["files"])
app.include_router(test2_reouter, prefix="/auth", tags=["auth"])

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
