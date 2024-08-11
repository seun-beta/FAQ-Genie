<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/4syLkpP.jpeg" alt="Project logo"></a>
</p>

<h3 align="center">Supernova RAG API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/seun-beta/faq-genie.svg)](https://github.com/seun-beta/faq-genie/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/seun-beta/faq-genie.svg)](https://github.com/seun-beta/faq-genie/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">Supernova RAG API is a powerful Retrieval-Augmented Generation system designed to deliver precise answers from Supernova Limited's extensive employee handbook using FastAPI, MongoDB, and OpenAI's GPT model.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [File Structure](#file_structure)
- [TODO](#todo)
- [Contributing](#contributing)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

**Supernova RAG API** provides an efficient way to query Supernova Limited's employee handbook, utilizing MongoDB's vector search capabilities and OpenAI's GPT model to augment and refine the answers. This ensures that users receive accurate and contextually relevant responses to their queries.

## 🏁 Getting Started <a name = "getting_started"></a>

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following software installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- An OpenAI API Key (Sign up at [OpenAI](https://beta.openai.com/signup/))

### Installing

1. **Clone the repository:**

   ```bash
   git clone https://github.com/seun-beta/faq-genie.git
   cd faq-genie
   ```

2. **Create a `.env` file in the root directory:**

   ```env
   MONGODB_URI=mongodb://localhost:27017/
   DB_NAME=supernova_rag
   COLLECTION_NAME=employee_handbook
   OPENAI_API_KEY=your_openai_api_key
   LOG_LEVEL=INFO
   ```

3. **Build and start the Docker containers:**

   ```bash
   docker-compose up --build
   ```

4. **Access the application:**

   The application will be running at `http://localhost:8000`.

## 🎈 Usage <a name="usage"></a>

Once the application is running, you can:

- **Query the RAG system**: Use the `/rag` endpoint to submit a query, and receive a response augmented by OpenAI's GPT model.

   Example:
   ```bash
   curl "http://localhost:8000/rag/?query=What%20is%20the%20mission%20of%20Supernova%20Limited?"
   ```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [MongoDB](https://www.mongodb.com/) - Database with vector search capabilities
- [Docker](https://www.docker.com/) - Containerization
- [OpenAI GPT](https://openai.com/) - AI Model

## 🗂️ File Structure <a name = "file_structure"></a>

```
.
├── app
│   ├── __init__.py            # Initialize FastAPI app
│   ├── main.py                # FastAPI application setup
│   └── rag_service.py         # Service to handle RAG logic and OpenAI integration
├── config
│   └── settings.py            # Configuration settings
├── data
│   └── handbook.json          # Sample data for the employee handbook
├── embeddings
│   ├── __init__.py            # Initialize embeddings package
│   └── openai_embedder.py     # OpenAI embedding generation
├── db
│   ├── __init__.py            # Initialize database package
│   └── mongo_db.py            # MongoDB operations including vector search
├── rag
│   ├── __init__.py            # Initialize RAG package
│   └── rag_system.py          # Core RAG system logic
├── scripts
│   ├── populate_db.py         # Script to populate MongoDB with handbook data
│   └── query_rag.py           # Script to query the RAG system
├── tests
│   ├── __init__.py            # Initialize tests package
│   ├── test_db.py             # Unit tests for MongoDB operations
│   ├── test_embedder.py       # Unit tests for embedding generation
│   └── test_rag_system.py     # Unit tests for the RAG system
├── utils
│   ├── logger.py              # Logging utility
│   └── error_handling.py      # Error handling utility
├── Dockerfile                 # Dockerfile for FastAPI app
├── docker-compose.yml         # Docker Compose file
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
└── README.md                  # Project documentation
```

## 🤝 Contributing <a name = "contributing"></a>

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/seun-beta/faq-genie/issues).

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

## ✍️ Authors <a name = "authors"></a>

- [@seun-beta](https://github.com/seun-beta) - Idea & Initial work

See also the list of [contributors](https://github.com/seun-beta/faq-genie/contributors) who participated in this project.


