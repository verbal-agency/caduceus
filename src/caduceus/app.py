"""Local HTTP application boundary for Caduceus."""

from fastapi import FastAPI


app = FastAPI(title="Caduceus", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Return the stable local-process health contract."""
    return {"status": "healthy"}

