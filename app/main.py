from fastapi import FastAPI, HTTPException, Query
from .faq_fetcher import load_faq_data
from .faq_processor import FAQProcessor
from pathlib import Path

app = FastAPI()

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
