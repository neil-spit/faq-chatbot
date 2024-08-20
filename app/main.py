from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from .faq_fetcher import load_faq_data
from .faq_processor import FAQProcessor

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. For production, specify the allowed origins explicitly.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Initialize FAQ processor
faq_directory = Path("./app/funderpro_faqs")
faq_data = load_faq_data(faq_directory)
faq_processor = FAQProcessor(faq_data)

@app.get("/")
async def root():
    return {"message": "Welcome to the FAQ Chatbot API"}

@app.get("/faq/")
async def get_faq_response(query: str = Query(..., min_length=1)):
    """
    Endpoint to get the most relevant FAQ response.

    :param query: The user's query.
    :return: The most relevant FAQ as a JSON response.
    """
    try:
        result = faq_processor.find_most_relevant(query)
        return {"query": query, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
