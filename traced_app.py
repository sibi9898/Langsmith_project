from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
prompt = ["give me a list of 5 fruits.", "What is the capital of France?", "What are the benefits of meditation?"]
model = ChatOpenAI(
    model_name="gpt-4o-mini")

for p in prompt:
    print(model.invoke(p).content)