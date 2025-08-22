from dotenv import load_dotenv
from application.file_reader import FileReader
from application.db import ChromaDB
from application.rag import CurriculumRAG

load_dotenv(override=True)

reader = FileReader("data/me.pdf");
#TODO: Melhorar o retorno para conter metadados
curriculum_text = reader.read_pdf();

rag = CurriculumRAG(curriculum_text)
db = ChromaDB()

chunks = rag.text_splitter()
print(f"Chunks: {chunks}")
db.save(chunks)