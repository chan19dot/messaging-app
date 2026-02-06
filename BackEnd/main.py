from fastapi import FastAPI

app = FastAPI(title="Local Chat API")

@app.get("/health")
def health():
    return {"status": "ok"}