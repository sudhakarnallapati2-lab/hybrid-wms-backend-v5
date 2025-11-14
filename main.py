from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Hybrid WMS Backend v5 Running"}
