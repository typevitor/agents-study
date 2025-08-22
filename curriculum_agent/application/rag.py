from langchain.text_splitter import RecursiveCharacterTextSplitter

class CurriculumRAG:

    def __init__(self, text: str):
        self.text = text
    
    def text_splitter(self) -> list:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50,
            length_function=len,
            is_separator_regex=False,
        )
        texts = text_splitter.create_documents([self.text])
        return texts