from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.config import settings
from presentation import router as ApiRouter
from repositories.base.exceptions import BaseException
from core.middlware import LoggingMiddlaware

app = FastAPI(
    title="Military Online Shop",
)
app.include_router(ApiRouter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)
app.add_middleware(LoggingMiddlaware)
@app.exception_handler(BaseException)
def exception_handler(req, exc: BaseException):
    raise HTTPException(
        status_code=exc.status,
        detail=exc.detail
    )

@app.get("/")
def index():
    return {
        "message": "Welcome!"
    }


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.runcfg.port), reload=settings.runcfg.reload)