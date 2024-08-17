from typing import List, Tuple
from openai.embeddings_utils import get_embedding, cosine_similarity

class FAQProcessor:
    def __init__(self, faqs: List[dict]):
        """
        Initialize with a list of FAQs.

        :param faqs: List of dictionaries containing 'question' and 'answer'.
        """
        self.faqs = faqs
        self.embeddings = self._compute_embeddings()

    def _compute_embeddings(self) -> List[Tuple[str, str, List[float]]]:
        """
        Computes embeddings for all FAQs.

        :return: List of tuples containing (question, answer, embedding).
        """
        return [(faq['question'], faq['answer'], get_embedding(faq['question'])) for faq in self.faqs]

    def find_most_relevant(self, query: str) -> dict:
        """
        Find the most relevant FAQ based on the query.

        :param query: The user query.
        :return: The most relevant FAQ as a dictionary.
        """
        query_embedding = get_embedding(query)
        similarities = [
            (cosine_similarity(query_embedding, faq_embedding), question, answer)
            for question, answer, faq_embedding in self.embeddings
        ]
        most_similar = max(similarities, key=lambda x: x[0])
        return {"question": most_similar[1], "answer": most_similar[2]}
