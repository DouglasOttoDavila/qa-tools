import re
import html2text
from flask import json
from configuration.config import MODE
from modules.user_story_analyzer.config.configuration import PROMPTS
from dotenv import load_dotenv
from services.infisical_sdk import get_infisical_secret

load_dotenv()

def get_dynamic_values(folder_path:str, secret_name:str, environment:str):
    """
    Gets a dynamic value from Infisical (if configured as the vault) or from an environment variable.
    
    Parameters:
    folder_path (str): The folder path of the secret to retrieve in Infisical.
    secret_name (str): The name of the secret to retrieve in Infisical or the environment variable to retrieve.
    environment (str): The environment slug in Infisical for the secret to retrieve.
    
    Returns:
    str: The dynamic value retrieved from Infisical or the environment variable.
    """
    try:
        if MODE == "vault":
            print(f"Getting {secret_name} from Infisical Vault...")
            return get_infisical_secret(folder_path, secret_name, environment)
        else:
            print(f"Getting {secret_name} from environment variable: {PROMPTS[secret_name]}")
            return PROMPTS[secret_name]
    except Exception as e:
        print(f"Error getting dynamic value: {e}")
        return None


def replace_placeholders(original_content, placeholders, replacements):
    """
    Replace placeholders with replacements in original_content.

    Parameters:
    original_content (str): The original content to be modified.
    placeholders (list): A list of placeholders to be replaced.
    replacements (list): A list of replacements to replace the placeholders.

    Returns:
    str: The modified content with placeholders replaced.
    """
    if len(placeholders) != len(replacements):
        raise ValueError("placeholders and replacements must be the same size")

    for i, (placeholder, replacement) in enumerate(zip(placeholders, replacements)):
        if not isinstance(placeholder, str):
            placeholders[i] = str(placeholder)
        if not isinstance(replacement, str):
            replacements[i] = str(replacement)

    for placeholder, replacement in zip(placeholders, replacements):
        original_content = original_content.replace(placeholder, replacement)

    return original_content


def clean_and_parse_json(text):
    """
    Cleans a JSON-like string by removing Markdown-style code block markers and parses it as a JSON object.
    
    :param text: JSON string with potential formatting issues.
    :return: Parsed JSON object (dict) or None if parsing fails.
    """
    
    try:
        # Remove leading/trailing code block markers
        cleaned_text = re.sub(r'^```json\n?|\n?```$', '', text.strip())
        return json.loads(cleaned_text)
    except:
        print(f"Failed to parse JSON: {text}")
        return text
    

def html_to_markdown(html_string):
    """
    Converts HTML to Markdown, preserving the structure of the given HTML.

    Args:
        html_string (str): The HTML string to convert.

    Returns:
        str: The Markdown equivalent of the HTML.
    """
    h = html2text.HTML2Text()
    h.ignore_links = False # Important for preserving links
    h.ignore_images = True
    h.ignore_tables = False # Important to properly format the table
    h.body_width = 0 # Prevent line wrapping
    markdown = h.handle(html_string)
    return markdown
