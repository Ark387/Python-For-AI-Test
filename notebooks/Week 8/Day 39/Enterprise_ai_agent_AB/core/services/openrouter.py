from openai import OpenAI
from dotenv import load_dotenv

import os


load_dotenv()

# llm_client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPEN_ROUTER_KEY"),
# )

llm_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_KEY"),
)

# MODEL = "nvidia/nemotron-3.5-lightning:free"       # chat model (free, NVIDIA)
MODEL = "openrouter/auto"
EMBEDDING_MODEL = "baai/bge-m3"


