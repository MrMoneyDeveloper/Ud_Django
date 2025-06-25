from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")  # type: ignore[misc]
def ping() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "ingestion.adapters.main:app",
        host="0.0.0.0",
        port=8000,
        limit_max_requests=1000,
    )
