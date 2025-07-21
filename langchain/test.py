import os
from dotenv import load_dotenv
load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# print(DEEPSEEK_API_KEY)

# from openai import OpenAI
# client = OpenAI(api_key=DEEPSEEK_API_KEY,base_url="https://api.deepseek.com")
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {
#       "role": "system",
#       "content": "You are a helpful assistant."
#     },
#     {
#       "role": "user",
#       "content": "What is the meaning of life?"
#     }
#   ]
# )
# print(response.choices[0].message.content)

# from langchain.chat_models import init_chat_model
#
# model = init_chat_model(model="deepseek-reasoner", model_provider="deepseek")
# question = "大模型有哪些基础概念？"
# result = model.invoke(question)
# print(result.content)



# import os
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url="https://dashscope.aliyun.com/compatible-model/v1")
# completions = client.chat.completions.create(
#   model="qwen-plus",
#   messages=[
#     {
#       "role": "system",
#       "content": "You are a helpful assistant."
#     },
#     {
#       "role": "user",
#       "content": "你是谁?"
#     }
#   ]
# )
# print(completions.model_dump_json())


#使用ollama
# from langchain_ollama import ChatOllama
# model=ChatOllama(model="gemma3")
# question="你是谁?介绍下你自己"
# result=model.invoke(question)
# print(result.content)