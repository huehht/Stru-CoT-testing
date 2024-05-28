from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from FewShotExamplePrompter import FewShotExamplePrompter
llm = Ollama(model="llama3")
output_parser = StrOutputParser()

# 定义几个few-shot examples
examples = [
    {"descriptions": "这是一个用于计算圆面积的函数","input": "圆","output": "圆面积","data_structure":"1","result":"2"},
    {"descriptions": "这是一个用于计算长方形面积的函数","input": "长方形","output": "长方形面积","data_structure":"1","result":"2"},
    {"descriptions": "这是一个用于计算三角形面积的函数","input": "三角形","output": "三角形面积","data_structure":"1","result":2}
]

# 定义格式化模板和前后缀
with open("Stru-CoT-testing/example.txt", "r", encoding="utf-8") as f:
    example_formatter_pretemplate = f.read()
# example_formatter_pretemplate=""
example_formatter_template = example_formatter_pretemplate.join("函数说明:{descriptions}\n函数输入：{input}\n函数输出：{output}\n类数据结构：{data_structure}\n生成的代码为：{result}")
prefix = "写一段代码以完成这个C++类中的函数，不要有其他文字，并使用中文回答问题，以下为所需生成函数的输入输出和类数据结构以及函数生成的示例："
suffix = "函数说明:{descriptions}\n函数输入：{input}\n函数输出：{output}\n类数据结构：{data_structure}，为其生成代码"
example_separator = "\n"

# 实例化FewShotExamplePrompter类
prompter = FewShotExamplePrompter(
    examples=examples,
    example_formatter_template=example_formatter_template,
    prefix=prefix,
    suffix=suffix,
    example_separator=example_separator
)

# 生成包含few-shot examples的prompt
prompt = prompter.generate_prompt(description_value="飞机")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "写一段代码以完成这个函数,不要有其他文字，并使用中文回答问题"),
#     ("user", "{input}")
# ])
print(prompt)
# chain = prompt | llm 
# out=chain.invoke({"input":"实现了飞行的起飞控制"})
# print(out)