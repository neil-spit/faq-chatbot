import unittest
import pathlib
from unittest.mock import patch, mock_open
import zipfile
import os

from app.faq_fetcher import extract_faqs, load_faq_data

class TestFAQFetcher(unittest.TestCase):
    @patch('app.faq_fetcher.zipfile.ZipFile')
    @patch('app.faq_fetcher.os.path.exists', return_value=True)
    def test_extract_faqs(self, mock_exists, mock_zipfile):
        mock_zip = mock_zipfile.return_value
        mock_zip.extractall.return_value = None
        result = extract_faqs('path/to/zipfile.zip')
        self.assertEqual(result, pathlib.Path('./extracted_faqs'))
        mock_zip.extractall.assert_called_once_with('./extracted_faqs')

    @patch('app.faq_fetcher.pathlib.Path.iterdir')
    @patch('app.faq_fetcher.open', new_callable=mock_open, read_data="Question\nAnswer\n")
    def test_load_faq_data(self, mock_open, mock_iterdir):
        mock_subdir = pathlib.Path('./subdir')
        mock_file = pathlib.Path('./subdir/file.txt')
        mock_iterdir.return_value = [mock_subdir]
        mock_subdir.glob.return_value = [mock_file]
        mock_file.is_dir.return_value = True
        
        faq_data = load_faq_data(pathlib.Path('./extracted_faqs'))
        self.assertEqual(len(faq_data), 1)
        self.assertEqual(faq_data[0]['question'], 'Question')
        self.assertEqual(faq_data[0]['answer'], 'Answer')

if __name__ == '__main__':
    unittest.main()
