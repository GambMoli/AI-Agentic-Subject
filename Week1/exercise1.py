import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)
MODEL = "gemini-flash-latest"

print("=== EXERCISE 1 RESULT ===")
MY_PROMPT = "Write a short poem about a robot learning to love."

for temp in [0.0, 0.4, 0.9, 1.5]:
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=MY_PROMPT,
            config=types.GenerateContentConfig(temperature=temp, max_output_tokens=50),
        )
        text = response.text.strip() if getattr(response, "text", None) else "NO TEXT GENERATED (Blocked or Empty)"
        print(f"Temperature={temp:<4} -> {text}\n")
    except Exception as e:
        print(f"Temperature={temp:<4} -> ERROR: {e}\n")
    time.sleep(4)
