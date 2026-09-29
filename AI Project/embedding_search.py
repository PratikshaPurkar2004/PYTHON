import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
import chromadb


# ==================================================
# 1. LOAD API KEY FROM .env
# ==================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found.")
    print("Please add GEMINI_API_KEY to your .env file.")
    exit()


# ==================================================
# 2. CONNECT TO GEMINI
# ==================================================

gemini_client = genai.Client(
    api_key=api_key
)

print("Gemini embedding model loaded!")


# ==================================================
# 3. CREATE DOCUMENT EMBEDDING
# ==================================================

def create_document_embedding(text):

    result = gemini_client.models.embed_content(

        model="gemini-embedding-001",

        contents=text,

        config=types.EmbedContentConfig(

            task_type="RETRIEVAL_DOCUMENT",

            output_dimensionality=768
        )
    )

    return result.embeddings[0].values


# ==================================================
# 4. CREATE QUERY EMBEDDING
# ==================================================

def create_query_embedding(text):

    result = gemini_client.models.embed_content(

        model="gemini-embedding-001",

        contents=text,

        config=types.EmbedContentConfig(

            task_type="RETRIEVAL_QUERY",

            output_dimensionality=768
        )
    )

    return result.embeddings[0].values


# ==================================================
# 5. READ DOCUMENT
# ==================================================

with open("document.txt", "r", encoding="utf-8") as file:

    text = file.read()


# ==================================================
# 6. SPLIT DOCUMENT INTO CHUNKS
# ==================================================

chunks = []

paragraphs = text.split("\n\n")

for paragraph in paragraphs:

    paragraph = paragraph.strip()

    if paragraph:

        chunks.append(paragraph)


print("Number of chunks:", len(chunks))


# ==================================================
# 7. GENERATE DOCUMENT EMBEDDINGS
# ==================================================

embeddings = []

print("\nGenerating embeddings...")

for i, chunk in enumerate(chunks):

    embedding = create_document_embedding(chunk)

    embeddings.append(embedding)

    print("Embedding created for Chunk", i + 1)


print("\nEmbeddings generated successfully!")

print(
    "Embedding size:",
    len(embeddings[0])
)


# ==================================================
# 8. CONNECT TO CHROMADB
# ==================================================

chroma_client = chromadb.PersistentClient(
    path="./chroma_db_gemini"
)

print("\nChromaDB connected!")


# ==================================================
# 9. CREATE COLLECTION
# ==================================================

collection = chroma_client.get_or_create_collection(

    name="gemini_documents",

    metadata={
        "hnsw:space": "cosine"
    }
)

print("ChromaDB collection created!")


# ==================================================
# 10. STORE DATA IN CHROMADB
# ==================================================

collection.upsert(

    ids=[
        f"chunk_{i}"
        for i in range(len(chunks))
    ],

    documents=chunks,

    embeddings=embeddings
)


print("\nData stored in ChromaDB!")

print(
    "Number of stored chunks:",
    collection.count()
)


# ==================================================
# 11. SIMILARITY SEARCH
# ==================================================

results = []


while True:

    question = input(
        "\nEnter your question "
        "(type exit to stop): "
    )


    # Stop program

    if question.lower() == "exit":

        break


    # ==================================================
    # 12. CREATE QUERY EMBEDDING
    # ==================================================

    query_embedding = create_query_embedding(
        question
    )


    # ==================================================
    # 13. SEARCH CHROMADB
    # ==================================================

    search_results = collection.query(

        query_embeddings=[
            query_embedding
        ],

        n_results=3,

        include=[
            "documents",
            "distances"
        ]
    )


    # ==================================================
    # 14. GET RESULTS
    # ==================================================

    documents = search_results["documents"][0]

    distances = search_results["distances"][0]

    ids = search_results["ids"][0]


    # ==================================================
    # 15. DISPLAY RESULTS
    # ==================================================

    print("\n" + "=" * 60)

    print("CHROMADB SIMILARITY SEARCH RESULTS")

    print("=" * 60)


    for i in range(len(documents)):

        similarity = 1 - distances[i]


        print("\nResult", i + 1)

        print("-" * 60)

        print("Chunk ID:", ids[i])

        print(
            "Similarity:",
            round(similarity, 4)
        )

        print("Information:")

        print(documents[i])


        # Save result

        results.append(
            (
                question,
                ids[i],
                similarity
            )
        )


# ==================================================
# 16. FINAL RESULTS
# ==================================================

print("\n" + "=" * 60)

print("FINAL RESULTS")

print("=" * 60)


for question, chunk, similarity in results:

    print("\nQuestion:", question)

    print(
        "Retrieved Chunk:",
        chunk
    )

    print(
        "Similarity:",
        round(similarity, 4)
    )


print("\nProgram completed.")