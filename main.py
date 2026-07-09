import uvicorn
from fastapi import FastAPI
from settings import settings
from api_router import router as tour_router

app = FastAPI(title="Tour Agency API")

app.include_router(tour_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)
