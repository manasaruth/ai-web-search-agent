from duckduckgo_search import DDGS
from google import genai

# API key should be set as environment variable (not hardcoded for security)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def search_web(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "title": r["title"],
                "link": r["href"],
                "snippet": r["body"]
            })
    return results

def generate_answer(query, search_results):
    sources = [r["link"] for r in search_results]

    answer = f"""
    This is a simulated AI response.

    Based on current trends, AI in 2026 focuses on:
    - Generative AI advancements
    - AI agents and automation
    - Multimodal AI systems
    - AI in healthcare and finance

    (Note: API quota exceeded, so this is a fallback response.)
    """

    return answer, sources

def main():
    query = input("Enter your question: ")

    results = search_web(query)
    answer, sources = generate_answer(query, results)

    print("\nAnswer:\n", answer)
    print("\nSources:")
    for s in sources:
        print(s)

if __name__ == "__main__":
    main()
