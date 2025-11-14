from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Hybrid WMS Minimal Backend v5", version="0.1.0")

# CORS (required for Streamlit Cloud)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Hybrid WMS Backend v5 Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/warehouse/info")
def warehouse_info():
    return {"warehouse": "Demo Warehouse", "zones": 3, "bays": 12}
