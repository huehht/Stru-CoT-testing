from langchain import PromptTemplate, FewShotPromptTemplate

# 定义几个few-shot examples，这些例子将帮助模型理解任务
examples = [
    {"input": "三角形", "output": "多边形"},
    {"input": "自行车", "output": "交通工具"},
    {"input": "火箭", "output": "太空交通工具"}
]

# 创建一个用于格式化例子的prompt模板
example_formatter_template = """
输入：{input}
输出：{output}
"""

# 使用上面的例子格式化模板创建一个PromptTemplate
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_formatter_template
)

# 创建一个FewShotPromptTemplate对象
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,  # 我们之前定义的例子
    example_prompt=example_prompt,  # 用于格式化例子的prompt模板
    prefix="给定以下输入输出对，找出模式并给出新输入的输出：",
    suffix="\n输入：{input}\n输出：",
    input_variables=["input"],  # 整体prompt模板的输入变量
    example_separator="\n"  # 例子之间的分隔符
)

# 使用few-shot例子格式化prompt模板
prompt_with_examples = few_shot_prompt.format(input="飞机")

print(prompt_with_examples)