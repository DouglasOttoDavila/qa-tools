import os
from dotenv import load_dotenv
from google import genai
from helpers.general_helpers import clean_and_parse_json, get_dynamic_values

load_dotenv()

def get_gemini_response(prompt: str) -> dict:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    try:
        clean_response = clean_and_parse_json(response.text)
        print('### GEMINI RESPONSE:', clean_response)
        return clean_response
    except:
        clean_response = response.text
        return clean_response
    