import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

os.environ["GROQ_API_KEY"] = "api_key"

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

template = """
You are a healthcare assistant.

Provide safe general health advice.
Do not diagnose diseases.
Encourage consulting doctors for serious issues.

Question: {question}
"""

prompt = PromptTemplate.from_template(template)

chain = prompt | llm


def ask_health_question(question):
    response = chain.invoke({"question": question})
    return response.content
