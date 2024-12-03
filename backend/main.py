from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.settings import settings



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
)


@app.get("/")
def index():
    return {
        "message": "Welcome"
    }


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.runcfg.port), reload=settings.runcfg.reload)