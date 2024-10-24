# Install dependencies
# pip install fastapi uvicorn python-multipart pytesseract pillow

from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract

app = FastAPI()

@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    # Baca gambar yang diunggah
    image = Image.open(file.file)

    # Jalankan OCR
    text = pytesseract.image_to_string(image)

    return {"extracted_text": text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
