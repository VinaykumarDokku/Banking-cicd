from fastapi import FastAPI

app = FastAPI(title="Banking API")


@app.get("/")
def home():
    return {"message": "Banking API running in Docker"}


@app.get("/accounts")
def get_accounts():
    return {
        "accounts": [
            {"id": 1, "name": "John", "balance": 10000},
            {"id": 2, "name": "David", "balance": 15000},
        ]
    }
