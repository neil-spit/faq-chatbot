import os
import pathlib
import zipfile
from typing import List

def extract_faqs(zip_path: str, extract_to: str = "./extracted_faqs") -> pathlib.Path:
    """
    Extracts the FAQs from a zip file and returns the path to the extracted folder.

    :param zip_path: Path to the zip file containing FAQs.
    :param extract_to: Directory where the zip file contents will be extracted.
    :return: Path to the directory containing extracted files.
    :raises FileNotFoundError: If the zip file does not exist.
    """
    # Check if the zip file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found at {zip_path}")

    # Extract the contents of the zip file to the specified directory
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Return the path to the directory containing extracted files
    return pathlib.Path(extract_to)

def load_faq_data(extracted_folder: pathlib.Path) -> List[dict]:
    """
    Loads FAQ data from text files within the subdirectories of the given folder.

    :param extracted_folder: Path to the directory containing extracted files.
    :return: List of FAQ dictionaries with 'question' and 'answer' fields.
    :raises ValueError: If no FAQs are found in the extracted files.
    """
    faq_data = []

    # Walk through all directories and subdirectories
    for root, _, files in os.walk(extracted_folder):
        for file in files:
            if file.endswith(".txt"):
                file_path = pathlib.Path(root) / file
                try:
                    with open(file_path, 'r') as f:
                        lines = f.readlines()
                        if len(lines) >= 2:  # Ensure there are at least two lines (question + answer)
                            question = lines[0].strip()  # First line is the question
                            answer = ''.join(lines[1:]).strip()  # Remaining lines form the answer
                            faq_data.append({'question': question, 'answer': answer})
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    # Raise an error if no FAQ data was loaded
    if not faq_data:
        raise ValueError("No FAQs found in the extracted files.")

    return faq_data

