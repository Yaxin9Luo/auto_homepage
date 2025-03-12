from enum import Enum
from typing import List

from pydantic import BaseModel

from agents import Agent


class TaskType(str, Enum):
    """任务类型枚举"""
    WEB_CODE = "网页代码生成"
    ACADEMIC_CONTENT = "学术内容整理"
    TEXT_POLISH = "文本润色"
    UI_BEAUTIFY = "UI美化"
    SEO_OPTIMIZE = "SEO优化"
    CODE_REVIEW = "代码审查"
    DEPLOY = "网站部署"


class TriageOutput(BaseModel):
    """分流代理的输出类型"""
    tasks: List[TaskType]
    """需要执行的任务列表"""


PROMPT = """
你是一个学术主页生成系统的分流代理。你的任务是分析用户的需求，确定需要执行哪些任务。

可能的任务类型包括：
1. 网页代码生成 - 生成HTML/CSS/JS代码
2. 学术内容整理 - 整理学术简历、成果列表等
3. 文本润色 - 润色文本内容
4. UI美化 - 美化页面外观
5. SEO优化 - 优化搜索引擎可见性
6. 代码审查 - 检查代码质量和安全性
7. 网站部署 - 部署到GitHub Pages或Netlify

你将收到用户的信息，包括个人资料、学术成果、偏好等。请根据这些信息，确定需要执行哪些任务。

注意：
- 网页代码生成和学术内容整理是必须的任务
- 代码审查也是必须的任务
- 其他任务根据用户的需求和偏好来决定
"""


triage_agent = Agent(
    name="分流代理",
    instructions=PROMPT,
    model="o3-mini",
    output_type=TriageOutput,
)
