from fastapi import FastAPI

app = FastAPI(
    title="Insurance Management API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Insurance Management API is running"
    }