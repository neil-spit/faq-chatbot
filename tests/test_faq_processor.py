import unittest
from unittest.mock import patch, Mock
from app.faq_processor import FAQProcessor

class TestFAQProcessor(unittest.TestCase):
    @patch('app.faq_processor.get_embedding')
    @patch('app.faq_processor.cosine_similarity')
    def setUp(self, mock_cosine_similarity, mock_get_embedding):
        # Mock embeddings
        mock_get_embedding.return_value = [0.1, 0.2, 0.3]
        mock_cosine_similarity.return_value = 0.9

        # Sample FAQ data
        self.faqs = [
            {'question': 'What is AI?', 'answer': 'Artificial Intelligence'},
            {'question': 'What is Python?', 'answer': 'A programming language'}
        ]
        self.processor = FAQProcessor(self.faqs)

    def test_compute_embeddings(self):
        embeddings = self.processor.embeddings
        self.assertEqual(len(embeddings), 2)
        self.assertEqual(embeddings[0][0], 'What is AI?')
        self.assertEqual(embeddings[0][1], 'Artificial Intelligence')
        self.assertEqual(embeddings[0][2], [0.1, 0.2, 0.3])

    @patch('app.faq_processor.get_embedding')
    @patch('app.faq_processor.cosine_similarity')
    def test_find_most_relevant(self, mock_cosine_similarity, mock_get_embedding):
        mock_get_embedding.return_value = [0.1, 0.2, 0.3]
        mock_cosine_similarity.return_value = 0.9

        result = self.processor.find_most_relevant('What is AI?')
        self.assertEqual(result['question'], 'What is AI?')
        self.assertEqual(result['answer'], 'Artificial Intelligence')

    @patch('app.faq_processor.get_embedding', side_effect=Exception('API Error'))
    def test_find_most_relevant_api_error(self, mock_get_embedding):
        with self.assertRaises(Exception) as context:
            self.processor.find_most_relevant('What is AI?')
        self.assertTrue('API Error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
