from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.settings import settings
from api import router as ApiRouter


app = FastAPI()
app.include_router(router=ApiRouter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)


@app.get("/")
def index():
    return {
        "message": "Welcome!"
    }


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.runcfg.port), reload=settings.runcfg.reload)