URL Information Extractor (RAG-based)

This project is a Retrieval-Augmented Generation (RAG)-based application that extracts and processes webpage data to provide accurate answers to user queries. It uses LangChain along with vector search to enhance information retrieval and response generation.

🚀 Features

RAG Implementation: Combines retrieval from a knowledge base and generation via LLM.

FAISS Vector Search: Stores and retrieves webpage content efficiently.

MapReduce Technique: Optimized retrieval for large documents.

Multi-URL Support: Processes multiple sources for better contextual answers.

Source Citation: Provides URLs as references for generated answers.

🛠️ Tech Stack

LangChain (for pipeline construction)

FAISS (for vector-based retrieval)

DeepSeek-R1 LLM (for response generation)

UnstructuredURLLoader (for loading webpage content)

RecursiveCharacterTextSplitter (for text chunking)

🔍 How It Works

1️⃣ Webpage Content Extraction: Loads raw text from URLs.2️⃣ Chunking & Vectorization: Splits text into smaller segments and converts them into vector embeddings.3️⃣ Storage & Retrieval: Stores embeddings in FAISS and retrieves relevant chunks based on user queries.4️⃣ Response Generation: Uses retrieved data to generate an answer via LLM.

🎥 Demo

https://www.linkedin.com/posts/siddhanth-garg-7b13b0232_langchain-rag-retrievalaugmentedgeneration-activity-7296937240935510016-yJlH?utm_source=share&utm_medium=member_desktop&rcm=ACoAADoUQ3UB3OwnD75rRLhBQTig7lKmWt2Ejtc

📜 License

This project is open-source and available under the MIT License.

For suggestions or collaborations, feel free to connect with me! 🚀
