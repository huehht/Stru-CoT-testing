from human_eval.data import write_jsonl, read_problems

problems = read_problems()

def generate_one_completion(prompt_input):
    import os
    # from getpass import getpass
    from langchain_community.llms import Tongyi
    from langchain_core.prompts import PromptTemplate

    # api_key = getpass()
    api_key=os.getenv("DASHSCOPE_API_KEY")
    # print(api_key)
    os.environ["DASHSCOPE_API_KEY"]=api_key
    llm = Tongyi(model="qwen-max-latest")
    template = """Please complete the code: {question}"""
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    question = prompt_input
    result=chain.invoke({"question": question})
    print(result)
    return result

num_samples_per_task = 200
samples = [
    dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)