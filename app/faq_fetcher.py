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
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found at {zip_path}")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    return pathlib.Path(extract_to)

def load_faq_data(extracted_folder: pathlib.Path) -> List[dict]:
    """
    Loads FAQ data from text files within the subdirectories of the given folder.

    :param extracted_folder: Path to the directory containing extracted files.
    :return: List of FAQ dictionaries with 'question' and 'answer' fields.
    :raises ValueError: If no FAQs are found in the extracted files.
    """
    faq_data = []

    for subdir in extracted_folder.iterdir():
        if subdir.is_dir():
            for file in subdir.glob("*.txt"):
                try:
                    with open(file, 'r') as f:
                        lines = f.readlines()
                        if len(lines) >= 2:
                            question = lines[0].strip()
                            answer = ''.join(lines[1:]).strip()
                            faq_data.append({'question': question, 'answer': answer})
                except Exception as e:
                    print(f"Error reading file {file}: {e}")

    if not faq_data:
        raise ValueError("No FAQs found in the extracted files.")

    return faq_data
