import os
import zipfile
import json
from pathlib import Path
from typing import List

def extract_faqs(zip_path: str, extract_to: str = "./extracted_faqs") -> Path:
    """
    Extracts the FAQs from a zip file and returns the path to the extracted folder.

    :param zip_path: Path to the zip file containing FAQs.
    :param extract_to: Directory where the zip file contents will be extracted.
    :return: Path to the directory containing extracted files.
    """
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found at {zip_path}")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    return Path(extract_to)


def load_faq_data(extracted_folder: Path) -> List[dict]:
    """
    Loads FAQ data from JSON files within the subdirectories of the given folder.

    :param extracted_folder: Path to the directory containing extracted files.
    :return: List of FAQ dictionaries.
    """
    faq_data = []
    
    # Traverse through all subdirectories
    for subdir in extracted_folder.iterdir():
        if subdir.is_dir():
            for file in subdir.glob("*.json"):
                with open(file, 'r') as f:
                    data = json.load(f)
                    faq_data.extend(data.get("faqs", []))

    if not faq_data:
        raise ValueError("No FAQs found in the extracted files.")

    return faq_data
