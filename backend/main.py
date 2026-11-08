from fastapi import FastAPI

app = FastAPI(title="What's for Today")

@app.get("/")
def read_root():
    return {"message": "Backend dziala!"}