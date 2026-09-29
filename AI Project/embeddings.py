import os
import math

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")



client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=30000)
)


with open("document.txt", "r", encoding="utf-8") as file:
    document = file.read().strip()

if not document:
    raise ValueError("document.txt is empty")


chunks = [
    chunk.strip()
    for chunk in document.split("\n\n")
    if chunk.strip()
]

print("Document loaded")
print("Number of chunks:", len(chunks))


print("Generating document embeddings...")

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=chunks,
    config=types.EmbedContentConfig(
        task_type="RETRIEVAL_DOCUMENT",
        output_dimensionality=768
    )
)

document_embeddings = [
    item.values
    for item in result.embeddings
]

print("Document embeddings created")


def cosine_similarity(a, b):

    dot_product = sum(
        x * y
        for x, y in zip(a, b)
    )

    magnitude_a = math.sqrt(
        sum(x * x for x in a)
    )

    magnitude_b = math.sqrt(
        sum(y * y for y in b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


while True:

    question = input("\nQuestion: ").strip()

    if question.lower() == "exit":
        print("Program ended.")
        break

    if not question:
        continue


    query_result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=768
        )
    )

    query_embedding = query_result.embeddings[0].values


    best_score = -1
    best_chunk = ""

    for i in range(len(chunks)):

        score = cosine_similarity(
            query_embedding,
            document_embeddings[i]
        )

        if score > best_score:
            best_score = score
            best_chunk = chunks[i]


    prompt = f"""
Answer the question using ONLY the context below.

If the answer is not available in the context, say:

The information is not available in the document.

Do not make up information.

Context:
{best_chunk}

Question:
{question}

Give a simple and clear answer.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )


    print()
    print("Question:", question)
    print("AI Answer:", response.text)