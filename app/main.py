
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import time

app = FastAPI(title="Shopping API")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Shopping API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/products")
def products():
    time.sleep(0.2)
    return {
        "products": [
            {"id": 1, "name": "Laptop", "price": 50000},
            {"id": 2, "name": "Mobile", "price": 20000}
        ]
    }
@app.get("/error")
def error():
    from fastapi import HTTPException
    raise HTTPException(status_code=500, detail="Simulated server error")