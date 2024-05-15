from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/post_example")
async def post_example_function(post_input: dict) -> dict[str, str]:
    return {
        "status": "ok",
        "type": "post",
        "additional_parameter": "additional_parameter_value",
        "input_content": post_input
    }

@app.post("/post_example_with_parameter/{parameter}")
async def post_example_with_parameter_function(parameter: str, post_with_parameter_input: dict) -> dict[str, str]:
    return {
        "parameter": parameter,
        "input_content": post_with_parameter_input,
    }


@app.delete("/delete_example/{parameter}")
async def delete_example(parameter: str) -> dict[str, str]:
    return {
        "parameter": parameter
    }
