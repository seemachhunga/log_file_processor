from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path


app = FastAPI()


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


log_file_path = None

@app.get("/")
def root():
    return {"message": "Welcome to the Log File Processor API!"}

@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    global log_file_path

    
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only text files are allowed.")
    
    
    log_file_path = UPLOAD_DIR / file.filename
    with open(log_file_path, "wb") as f:
        f.write(await file.read())
    
    
    return {"message": "File uploaded successfully!", "last_10_lines": get_last_lines(log_file_path, 10)}

@app.get("/last-lines/{line_count}")
def get_last_lines_route(line_count: int):
    global log_file_path

    
    if not log_file_path or not log_file_path.exists():
        raise HTTPException(status_code=404, detail="No log file has been uploaded yet.")
    
    
    return {"last_lines": get_last_lines(log_file_path, line_count)}


def get_last_lines(file_path: Path, line_count: int):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines[-line_count:] if len(lines) >= line_count else lines
