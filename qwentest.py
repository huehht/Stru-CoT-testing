import os
from getpass import getpass
from langchain_community.llms import Tongyi
from langchain_core.prompts import PromptTemplate

api_key = getpass()
# api_key=os.getenv("DASHSCOPE_API_KEY")
print(api_key)
os.environ["DASHSCOPE_API_KEY"]=api_key
llm = Tongyi(model="qwen-max-latest")
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)
chain = prompt | llm
question = "你是谁？"
chain.invoke({"question": question})
