from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "写一段代码以完成这个函数,不要有其他文字，并使用中文回答问题"),
    ("user", "{input}")
])
print(prompt)
chain = prompt | llm 
out=chain.invoke({"input":"实现了飞行的起飞控制"})
print(out)