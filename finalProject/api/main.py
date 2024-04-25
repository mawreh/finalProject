import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .routers.supportTicket import router as support_tickets_router
from .routers.ratings import router as ratings_router
from .models import model_loader
from .dependencies.config import conf

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)

app.include_router(support_tickets_router, prefix="/api/v1")
app.include_router(ratings_router, prefix="/api/v1/ratings")


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
