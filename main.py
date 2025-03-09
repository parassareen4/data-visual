from fastapi import FastAPI
from file_upload import router as file_upload_router

app = FastAPI()

app.include_router(file_upload_router)
