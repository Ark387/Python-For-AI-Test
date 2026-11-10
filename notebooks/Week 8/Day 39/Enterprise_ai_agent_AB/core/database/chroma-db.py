
import chromadb
from chromadb.config import Settings




chroma_client = chromadb.PersistentClient(
    path="./chroma_db",                                   # own folder, not the notebook folder
    settings=Settings(anonymized_telemetry=False),
)

collection = chroma_client.get_or_create_collection(name="restaurant_vector_db")