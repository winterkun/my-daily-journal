# 导入所需的库
import os
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv(override=True)

# 初始化语言模型
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if DEEPSEEK_API_KEY is None:
    raise ValueError("DEEPSEEK_API_KEY 环境变量未设置，请检查 .env 文件")

# 正确传递 model 参数
model = init_chat_model(model="deepseek-chat", openai_api_key=DEEPSEEK_API_KEY)

# 创建一个用于生成新闻内容的 PromptTemplate
news_gen_prompt = PromptTemplate.from_template("请根据以下新闻撰写一段简短的新闻内容（100字以内）：\n\n标题： {topic}")

# 创建 news_chain，用于根据新闻标题生成新闻内容
news_chain = news_gen_prompt | model

# 定义响应模式
schemas = [
    ResponseSchema(
        name="time",
        type="string",
        description="事件发生的时间"
    ),
    ResponseSchema(
        name="location",
        type="string",
        description="事件发生的地点"
    ),
    ResponseSchema(
        name="event",
        type="string",
        description="发生的具体事件"
    )
]

# 创建结构化输出解析器
parser = StructuredOutputParser.from_response_schemas(schemas)

# 创建一个用于生成新闻总结的 PromptTemplate
summary_prompt = PromptTemplate(
    template="请根据以下新闻内容，生成一个总结。\n\n{news}\n\n{format_instructions}",
    input_variables=["news", "format_instructions"]
)

# 创建 summary_chain，用于根据生成的新闻内容生成总结
summary_chain = summary_prompt.partial(
    format_instructions=parser.get_format_instructions()) | news_chain | parser

# 将 news_chain 和 summary_chain 组合成一个完整的链
full_chain = news_chain | summary_chain

# 调用 full_chain 并传入新闻标题，获取生成的新闻总结并打印
result = full_chain.invoke({"topic": "苹果公司在加州发布新款AI芯片"})
print(result)
