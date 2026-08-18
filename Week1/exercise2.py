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

print("=== EXERCISE 2 RESULT ===")
def estimate_tokens(text: str) -> float:
    return len(text) / 4.0

samples = [
    "Hi!",
    "The capital of France is Paris.",
    "AI Agentic Engineering is a course about building autonomous systems with large language models, "
    "retrieval-augmented generation, and multi-agent orchestration frameworks like Google ADK and LangGraph.",
]

for text in samples:
    try:
        real = client.models.count_tokens(model=MODEL, contents=text).total_tokens
        estimate = estimate_tokens(text)
        error_pct = abs(real - estimate) / real * 100 if real > 0 else 0
        print(f"Real: {real:4} | Est: {estimate:6.2f} | Error: {error_pct:5.2f}% | Text: {text[:40]!r}...")
    except Exception as e:
        print(f"Text: {text[:40]!r}... -> ERROR: {e}")
    time.sleep(4)
