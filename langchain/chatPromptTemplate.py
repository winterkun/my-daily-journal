from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langchain.output_parsers.boolean import BooleanOutputParser
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 初始化模型
model = init_chat_model(model="deepseek-chat", model_provider="deepseek")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "这是用户的输入的问题: {topic}，请用yes或no回答。"),
])

# 创建布尔输出解析器
output_parser = BooleanOutputParser()

# 创建链
bool_qa_chain = prompt_template | model | output_parser

# 提问
question = "请问1+1=3吗？"
result = bool_qa_chain.invoke({"topic": question})

print(result)