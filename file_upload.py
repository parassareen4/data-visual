from fastapi import File , APIRouter , UploadFile
import pandas as pd
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok = True)

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR,file.filename)
    
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
        return {"filename": file.filename, "message":"File uploaded successfully"}
        