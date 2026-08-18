import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)
MODEL = "gemini-flash-latest"

print("=== EXERCISE 1 RESULT ===")

zero_shot_prompt = 'Classify this email as "Priority High" or "Priority Low": "{email}"'
few_shot_prompt = '''Classify this email as "Priority High" or "Priority Low".

Email: "Server is down and clients are complaining"
Priority: Priority High

Email: "Hey, do you want to grab lunch later?"
Priority: Priority Low

Email: "The database migration failed, we need to rollback ASAP"
Priority: Priority High

Email: "{email}"
Priority:'''

test_inputs = [
    "I'll be out of office next week.",
    "Critical bug in production, payment gateway is failing.",
    "Can someone review my PR when they have time?"
]

print("--- Zero-shot ---")
for text in test_inputs:
    try:
        response = client.models.generate_content(model=MODEL, contents=zero_shot_prompt.format(email=text))
        out_text = response.text.strip() if getattr(response, 'text', None) else 'NO TEXT'
        print(f"Input: {text!r}\nPrediction: {out_text}\n")
    except Exception as e:
        print(f"Input: {text!r}\nERROR: {e}\n")
    time.sleep(4)

print("--- Few-shot ---")
for text in test_inputs:
    try:
        response = client.models.generate_content(model=MODEL, contents=few_shot_prompt.format(email=text))
        out_text = response.text.strip() if getattr(response, 'text', None) else 'NO TEXT'
        print(f"Input: {text!r}\nPrediction: {out_text}\n")
    except Exception as e:
        print(f"Input: {text!r}\nERROR: {e}\n")
    time.sleep(4)
