import os
import warnings
import sys

from langchain_community.document_loaders import BSHTMLLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv

# This loads environment variables from a .env file
load_dotenv()

chatgpt_token = os.getenv('CHATGPT_TOKEN')
# export ChatGPT API key
os.environ["OPENAI_API_KEY"] = chatgpt_token

# temporarily remove 'deprecated' warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

loader = BSHTMLLoader("data/koleo_ukr.html")
index = VectorstoreIndexCreator().from_loaders([loader])
chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-4-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []
while True:
    query = input("Prompt: ")

    if query in ['quit', 'q', 'exit']:
        # todo: save chat history to persist directory
        sys.exit()

    result = chain({"question": query, "chat_history": chat_history})
    print("> ", result['answer'])

    chat_history.append((query, result['answer']))
    query = None
