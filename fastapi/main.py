from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"i'm fast'fuck'boy"}














































