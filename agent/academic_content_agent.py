from typing import Dict, List, Optional

from pydantic import BaseModel

from agents import Agent


class Publication(BaseModel):
    """发表论文模型"""
    title: str
    authors: List[str]
    venue: str
    year: str
    url: Optional[str] = None
    citation: Optional[str] = None
    abstract: Optional[str] = None
    keywords: Optional[List[str]] = None


class Project(BaseModel):
    """项目经历模型"""
    name: str
    description: str
    year: str
    url: Optional[str] = None
    technologies: Optional[List[str]] = None
    outcomes: Optional[str] = None


class Education(BaseModel):
    """教育背景模型"""
    degree: str
    institution: str
    year: str
    description: Optional[str] = None


class AcademicContentOutput(BaseModel):
    """学术内容代理的输出类型"""
    bio_short: str
    """简短的个人简介（1-2句话）"""
    
    bio_long: str
    """详细的个人简介（1-2段）"""
    
    research_interests_desc: str
    """研究兴趣描述"""
    
    publications_formatted: List[Publication]
    """格式化的发表论文列表"""
    
    projects_formatted: List[Project]
    """格式化的项目经历列表"""
    
    education_formatted: List[Education]
    """格式化的教育背景列表"""
    
    skills: List[str]
    """技能列表"""
    
    keywords: List[str]
    """关键词列表，用于SEO"""


PROMPT = """
你是一个学术内容整理专家。你的任务是整理和优化用户提供的学术信息，使其适合在学术主页上展示。

你将收到用户的原始信息，包括个人资料、教育背景、发表论文、项目经历等。请根据这些信息，生成格式化的学术内容。

具体要求：
1. 生成简短的个人简介（1-2句话）和详细的个人简介（1-2段）
2. 整理研究兴趣，生成连贯的描述
3. 格式化发表论文列表，添加缺失的信息（如引用格式、摘要等）
4. 格式化项目经历列表，添加缺失的信息（如使用的技术、成果等）
5. 格式化教育背景列表，添加描述
6. 从用户信息中提取技能列表
7. 生成关键词列表，用于SEO优化

请确保内容专业、准确、简洁，适合学术主页展示。
"""


academic_content_agent = Agent(
    name="学术内容整理代理",
    instructions=PROMPT,
    model="o3-mini",
    output_type=AcademicContentOutput,
)
