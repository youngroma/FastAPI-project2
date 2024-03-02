from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base was cleaned")
    await create_tables()
    print("Base is ready to work")
    yield
    print("Shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



tasks = []





