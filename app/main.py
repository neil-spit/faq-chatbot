from fastapi import FastAPI, HTTPException, Query
from .faq_fetcher import extract_faqs, load_faq_data
from fastapi.middleware.cors import CORSMiddleware
from .faq_processor import FAQProcessor

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. For production, specify allowed origins explicitly.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# Paths to the FAQ zip file and where to extract it
faqs_zip_path = "app/funderpro_faqs.zip"  # Path to the zip file containing FAQs
extracted_faqs_path = extract_faqs(faqs_zip_path)  # Extract the FAQs and get the path to the extracted folder

# Load FAQ data from the extracted files and initialize the FAQ processor
faq_data = load_faq_data(extracted_faqs_path)  # Load FAQ data from the extracted files
faq_processor = FAQProcessor(faq_data)  # Initialize the processor with loaded FAQ data

@app.get("/faq/")
async def get_faq_response(query: str = Query(..., min_length=1)):
    """
    Endpoint to get the most relevant FAQ response based on the user's query.

    :param query: The user's query string.
    :return: A JSON response containing the user's query and the most relevant FAQ.
    """
    try:
        # Find the most relevant FAQ based on the query
        result = faq_processor.find_most_relevant(query)
        return {"query": query, "result": result}
    except Exception as e:
        # Return an error response in case of any issues during processing
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """
    Root endpoint for the API.

    :return: A welcome message as a JSON response.
    """
    return {"message": "Welcome to the FAQ Chatbot API"}
