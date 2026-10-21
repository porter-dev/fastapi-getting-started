from fastapi import FastAPI

app = FastAPI(title="FastAPI on Porter")


@app.get("/")
async def root():
    return {"message": "FastAPI is running on Porter"}


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
