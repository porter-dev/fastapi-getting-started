from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"author": "rudimk", "message": "in remembrance of earth's past."}

@app.get("/info")
async def root():
    return {"author": "rudimk", "message": "สวัสดี"}
