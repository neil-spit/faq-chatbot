import openai
import os
import numpy as np
from typing import List, Dict, Any

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class FAQProcessor:
    def __init__(self, faqs: List[Dict[str, str]], threshold: float = 0.8):
        """
        Initialize the FAQProcessor with a list of FAQs and a similarity threshold.
        Compute the embeddings for all FAQ questions during initialization.

        :param faqs: A list of dictionaries containing 'question' and 'answer' pairs.
        :param threshold: A float value that determines the minimum similarity score to consider a match.
        """
        self.faqs = faqs
        self.threshold = threshold
        self.embeddings = self._compute_embeddings()  # Precompute embeddings for all questions

    def _compute_embeddings(self) -> List[tuple]:
        """
        Compute the embeddings for all FAQ questions.

        :return: A list of tuples containing the question, answer, and their corresponding embeddings.
        """
        return [(faq['question'], faq['answer'], self.get_embedding(faq['question'])) for faq in self.faqs]

    def get_embedding(self, text: str) -> List[float]:
        """
        Generate an embedding for a given text using the OpenAI API.

        :param text: The text to be embedded.
        :return: A list representing the embedding vector.
        """
        try:
            # Use the "text-embedding-ada-002" model to generate embeddings
            response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
            return response['data'][0]['embedding']
        except Exception as e:
            print(f"Error getting embedding: {e}")
            return []

    def find_most_relevant(self, question: str) -> Dict[str, Any]:
        """
        Find the most relevant FAQ based on the similarity of the question embedding.

        :param question: The user's question to be matched against the FAQs.
        :return: A dictionary containing the 'question' and 'answer' of the most relevant FAQ.
        """
        question_embedding = self.get_embedding(question)
        if not question_embedding:
            return {'question': 'Error', 'answer': 'Unable to process the question.'}

        # Calculate similarity between the input question and all FAQ questions
        similarities = []
        for faq in self.embeddings:
            similarity = self.cosine_similarity(question_embedding, faq[2])
            similarities.append((faq[0], faq[1], similarity))
        
        # Filter out results below the threshold
        relevant_faqs = [faq for faq in similarities if faq[2] >= self.threshold]
        if relevant_faqs:
            # Sort by similarity and return the most relevant one
            most_relevant = max(relevant_faqs, key=lambda x: x[2])
            return {'question': most_relevant[0], 'answer': most_relevant[1]}
        else:
            return {'question': 'No relevant answer', 'answer': "I'm unable to answer that question."}

    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        Calculate the cosine similarity between two vectors.

        :param vec1: The first vector.
        :param vec2: The second vector.
        :return: A float representing the cosine similarity between the two vectors.
        """
        vec1, vec2 = np.array(vec1), np.array(vec2)
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        return dot_product / (norm_vec1 * norm_vec2) if norm_vec1 and norm_vec2 else 0.0
