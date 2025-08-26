# Curriculum Agent

An intelligent AI agent that answers questions about a person's curriculum vitae (CV) using Retrieval-Augmented Generation (RAG) technology. The agent can engage in professional conversations about career experience, education, skills, and projects as if representing the CV owner.

## Overview

The Curriculum Agent is designed to act as a professional representative, answering questions about career history, academic background, courses, skills, and projects based on a provided CV. It uses RAG to retrieve relevant information from the curriculum and provides accurate, professional responses suitable for interactions with potential employers.

## Features

- **RAG-powered responses**: Uses ChromaDB for vector storage and similarity search
- **Professional interaction**: Maintains a professional tone suitable for employer conversations
- **Quality assurance**: Built-in evaluation system to ensure response quality
- **PDF processing**: Extracts and processes curriculum data from PDF files
- **Interactive chat interface**: Gradio-based web interface for easy interaction
- **Tool integration**: Extensible tool system for additional functionality

## Architecture

The system consists of several key components:

### Core Components

- **[`Agent`](curriculum_agent/base_agents/agent.py)**: Main agent that handles chat interactions and RAG queries
- **[`Evaluator`](curriculum_agent/base_agents/evaluator.py)**: Quality assurance agent that evaluates responses
- **[`Chat`](curriculum_agent/application/chat.py)**: Chat controller that manages conversation flow
- **[`CurriculumRAG`](curriculum_agent/application/rag.py)**: RAG implementation for text chunking and processing
- **[`ChromaDB`](curriculum_agent/application/db.py)**: Vector database for storing and retrieving curriculum chunks
- **[`FileReader`](curriculum_agent/application/file_reader.py)**: PDF processing utility
- **[`OpenAIProvider`](curriculum_agent/application/openai_provider.py)**: OpenAI API integration

### Data Flow

1. **PDF Processing**: [`FileReader`](curriculum_agent/application/file_reader.py) extracts text from CV PDF
2. **Text Chunking**: [`CurriculumRAG`](curriculum_agent/application/rag.py) splits text into manageable chunks
3. **Vector Storage**: [`ChromaDB`](curriculum_agent/application/db.py) stores chunks as embeddings
4. **Query Processing**: User questions trigger similarity search in vector database
5. **Response Generation**: [`Agent`](curriculum_agent/base_agents/agent.py) generates responses using retrieved context
6. **Quality Check**: [`Evaluator`](curriculum_agent/base_agents/evaluator.py) validates response quality

## Installation

1. **Prerequisites**:
   ```bash
   python >= 3.12
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment setup**:
   Create a `.env` file with:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Setup Your Curriculum

1. **Place your CV PDF** in the `data/` directory as `me.pdf`
2. **Create a summary file** at `data/summary.txt` with a brief professional summary

### Initialize the RAG System

Run the RAG setup to process your curriculum:

```bash
python curriculum_agent/rag.py
```

This will:
- Extract text from your PDF
- Create text chunks
- Store embeddings in ChromaDB

### Start the Chat Interface

Launch the interactive chat interface:

```bash
python curriculum_agent/main.py
```

This opens a Gradio web interface where you can interact with your curriculum agent.

## Configuration

### Agent Configuration

The agent can be configured in [`curriculum_agent/base_agents/agent.py`](curriculum_agent/base_agents/agent.py):

- **Name**: Set the person's name the agent represents
- **Summary**: Professional summary for context
- **RAG parameters**: Adjust similarity search parameters (k=3 by default)

### Database Configuration

ChromaDB settings in [`curriculum_agent/application/db.py`](curriculum_agent/application/db.py):

- **Storage path**: `./db/` (configurable)
- **Embedding model**: `text-embedding-3-small`
- **Collection name**: `curriculum`

### Text Processing

RAG configuration in [`curriculum_agent/application/rag.py`](curriculum_agent/application/rag.py):

- **Chunk size**: 300 characters
- **Chunk overlap**: 50 characters
- **Splitter**: RecursiveCharacterTextSplitter

## Quality Assurance

The system includes a built-in evaluation mechanism:

- **Response validation**: Each response is evaluated for appropriateness
- **Feedback loop**: Failed responses are regenerated with feedback
- **Professional tone**: Ensures responses maintain professional standards

## File Structure

```
curriculum_agent/
├── main.py                     # Entry point and Gradio interface
├── rag.py                      # RAG system initialization
├── application/
│   ├── chat.py                 # Chat controller
│   ├── openai_provider.py      # OpenAI API integration
│   ├── db.py                   # ChromaDB vector database
│   ├── rag.py                  # RAG implementation
│   ├── file_reader.py          # PDF processing
│   └── api.py                  # Tool system
├── base_agents/
│   ├── agent.py                # Main curriculum agent
│   └── evaluator.py            # Response evaluation agent
├── data/
│   ├── me.pdf                  # Your curriculum PDF
│   └── summary.txt             # Professional summary
└── db/                         # ChromaDB storage (auto-created)
```

## Example Interactions

**Q**: "What programming languages do you know?"
**A**: "Based on my curriculum, I have experience with [languages found in CV]..."

**Q**: "Tell me about your latest project"
**A**: "My most recent project involved [project details from CV]..."

**Q**: "What is your educational background?"
**A**: "I completed [education details from CV]..."

## License

This project is for educational and personal use. Ensure compliance with OpenAI's usage policies when deploying.