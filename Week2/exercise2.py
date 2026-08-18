import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)
MODEL = "gemini-flash-latest"

print("=== EXERCISE 2 RESULT ===")

class ResumeLine(BaseModel):
    role: str
    company: str
    years: float

text_line = "Senior backend engineer at Northwind Traders for 3.5 years"

try:
    response = client.models.generate_content(
        model=MODEL,
        contents=text_line,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ResumeLine,
        ),
    )
    
    print(f"Original Text: {text_line}")
    if getattr(response, "parsed", None):
        parsed: ResumeLine = response.parsed
        print(f"Parsed JSON:")
        print(f"  Role: {parsed.role}")
        print(f"  Company: {parsed.company}")
        print(f"  Years: {parsed.years}")
    else:
        out_text = response.text if getattr(response, 'text', None) else 'NO TEXT'
        print(f"Raw Output: {out_text}")
except Exception as e:
    print(f"ERROR: {e}")

time.sleep(4)
