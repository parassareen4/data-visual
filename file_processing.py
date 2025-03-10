from fastapi import APIRouter, File, UploadFile, HTTPException
import pandas as pd 
import os 
router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/process/")
async def process_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file.filename.endswith(",json"):
            df = pd.read_json(file_path)
        elif file.filename.endswith((".xls",".xlsx")):
            df = pd.read_excel(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        data = df.to_dict(orient="records")
        return {"filename":file.filename,"data":data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file:{str(e)}")