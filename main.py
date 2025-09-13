from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

from routes import router as api_router

app = FastAPI()

app.include_router(api_router)


templates = Jinja2Templates(directory="templates")
@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

