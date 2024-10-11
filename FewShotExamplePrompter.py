from langchain import PromptTemplate, FewShotPromptTemplate

class FewShotExamplePrompter:
    def __init__(self, examples, example_formatter_template, prefix, suffix, example_separator):
        # 初始化few-shot examples和格式化模板
        self.examples = examples
        self.example_formatter_template = example_formatter_template
        self.prefix = prefix
        self.suffix = suffix
        self.example_separator = example_separator
        
        # 创建用于格式化例子的prompt模板
        self.example_prompt = PromptTemplate(
            input_variables=["descriptions", "input", "output","data_structure","result"],
            template=example_formatter_template
        )
        
        # 创建FewShotPromptTemplate对象
        self.few_shot_prompt = FewShotPromptTemplate(
            examples=self.examples,
            example_prompt=self.example_prompt,
            prefix=self.prefix,
            suffix=self.suffix,
            input_variables=["descriptions", "input", "output","data_structure"],
            example_separator=self.example_separator
        )
    
    def generate_prompt(self, input_value="", output_value="", ds=""):
        # 使用few-shot例子和指定的输入值生成格式化后的prompt
        return self.few_shot_prompt.format(input=input_value, output=output_value, data_structure=ds)