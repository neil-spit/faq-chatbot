import requests

API_URL = "http://localhost:8000/faq/"

def get_faq_response(query):
    try:
        response = requests.get(API_URL, params={"query": query})
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    print("Welcome to the FAQ Chatbot CLI")
    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        result = get_faq_response(query)
        if result:
            print("\nResponse:")
            print(f"Question: {result['result']['question']}")
            print(f"Answer: {result['result']['answer']}")
        print()

if __name__ == "__main__":
    main()
