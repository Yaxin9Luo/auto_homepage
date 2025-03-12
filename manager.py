from __future__ import annotations

import asyncio
import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List

from rich.console import Console

from agents import Agent, Runner, custom_span, gen_trace_id, trace

from .agents.academic_content_agent import academic_content_agent
from .agents.code_review_agent import code_review_agent
from .agents.deploy_agent import deploy_agent
from .agents.seo_agent import seo_agent
from .agents.text_polish_agent import text_polish_agent
from .agents.triage_agent import TaskType, triage_agent
from .agents.ui_beautify_agent import ui_beautify_agent
from .agents.web_code_agent import web_code_agent
from .printer import Printer


class HomepageManager:
    """学术主页生成系统的核心管理类"""
    
    def __init__(self):
        self.console = Console()
        self.printer = Printer(self.console)
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
    
    async def run(self, user_data: Dict[str, Any]) -> None:
        """运行学术主页生成流程"""
        trace_id = gen_trace_id()
        with trace("学术主页生成", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"追踪ID: https://platform.openai.com/traces/{trace_id}",
                is_done=True,
                hide_checkmark=True,
            )
            
            self.printer.update_item(
                "starting",
                "开始生成学术主页...",
                is_done=True,
                hide_checkmark=True,
            )
            
            # 保存用户数据到输出目录
            user_data_path = self.output_dir / "user_data.json"
            with open(user_data_path, "w", encoding="utf-8") as f:
                json.dump(user_data, f, ensure_ascii=False, indent=2)
            
            # 分析用户需求，确定任务
            tasks = await self._analyze_requirements(user_data)
            
            # 生成学术内容
            academic_content = await self._generate_academic_content(user_data)
            
            # 生成网页代码
            html_content = await self._generate_web_code(user_data, academic_content, tasks)
            
            # 如果需要，润色文本
            if TaskType.TEXT_POLISH in tasks:
                html_content = await self._polish_text(html_content, user_data["language_preference"])
            
            # 如果需要，美化UI
            if TaskType.UI_BEAUTIFY in tasks:
                html_content = await self._beautify_ui(html_content, user_data["style_preference"])
            
            # 如果需要，优化SEO
            if TaskType.SEO_OPTIMIZE in tasks:
                html_content = await self._optimize_seo(html_content, user_data)
            
            # 代码审查
            html_content = await self._review_code(html_content)
            
            # 保存生成的HTML
            html_path = self.output_dir / "index.html"
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            # 如果需要，部署网站
            if TaskType.DEPLOY in tasks:
                deploy_url = await self._deploy_website()
                self.printer.update_item(
                    "deploy",
                    f"网站已部署: {deploy_url}",
                    is_done=True,
                )
            
            self.printer.update_item(
                "complete",
                f"学术主页生成完成! 文件保存在: {html_path}",
                is_done=True,
            )
            
            self.printer.end()
    
    async def _analyze_requirements(self, user_data: Dict[str, Any]) -> List[TaskType]:
        """分析用户需求，确定需要执行的任务"""
        self.printer.update_item("analyzing", "分析用户需求...")
        
        result = await Runner.run(
            triage_agent,
            json.dumps(user_data, ensure_ascii=False),
        )
        
        # 获取TriageOutput对象中的tasks字段
        triage_output = result.final_output
        tasks = triage_output.tasks
        
        task_names = [task.value for task in tasks]  # 使用value而不是name
        self.printer.update_item(
            "analyzing",
            f"需要执行的任务: {', '.join(task_names)}",
            is_done=True,
        )
        
        return tasks
    
    async def _generate_academic_content(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """生成学术内容"""
        self.printer.update_item("content", "生成学术内容...")
        
        result = await Runner.run(
            academic_content_agent,
            json.dumps(user_data, ensure_ascii=False),
        )
        
        # 将AcademicContentOutput对象转换为字典
        academic_content = result.final_output.model_dump()
        
        self.printer.update_item(
            "content",
            "学术内容生成完成",
            is_done=True,
        )
        
        return academic_content
    
    async def _generate_web_code(
        self, user_data: Dict[str, Any], academic_content: Dict[str, Any], tasks: List[TaskType]
    ) -> str:
        """生成网页代码"""
        self.printer.update_item("web_code", "生成网页代码...")
        
        input_data = {
            "user_data": user_data,
            "academic_content": academic_content,
            "tasks": [task.value for task in tasks]
        }
        
        result = await Runner.run(
            web_code_agent,
            json.dumps(input_data, ensure_ascii=False),
        )
        
        html_content = result.final_output
        
        self.printer.update_item(
            "web_code",
            "网页代码生成完成",
            is_done=True,
        )
        
        return html_content
    
    async def _polish_text(self, html_content: str, language_preference: str) -> str:
        """润色文本"""
        self.printer.update_item("polish", "润色文本...")
        
        input_data = {
            "html_content": html_content,
            "language_preference": language_preference
        }
        
        result = await Runner.run(
            text_polish_agent,
            json.dumps(input_data, ensure_ascii=False),
        )
        
        polished_html = result.final_output
        
        self.printer.update_item(
            "polish",
            "文本润色完成",
            is_done=True,
        )
        
        return polished_html
    
    async def _beautify_ui(self, html_content: str, style_preference: str) -> str:
        """美化UI"""
        self.printer.update_item("beautify", "美化UI...")
        
        input_data = {
            "html_content": html_content,
            "style_preference": style_preference
        }
        
        result = await Runner.run(
            ui_beautify_agent,
            json.dumps(input_data, ensure_ascii=False),
        )
        
        beautified_html = result.final_output
        
        self.printer.update_item(
            "beautify",
            "UI美化完成",
            is_done=True,
        )
        
        return beautified_html
    
    async def _optimize_seo(self, html_content: str, user_data: Dict[str, Any]) -> str:
        """优化SEO"""
        self.printer.update_item("seo", "优化SEO...")
        
        input_data = {
            "html_content": html_content,
            "user_data": user_data
        }
        
        result = await Runner.run(
            seo_agent,
            json.dumps(input_data, ensure_ascii=False),
        )
        
        seo_optimized_html = result.final_output
        
        self.printer.update_item(
            "seo",
            "SEO优化完成",
            is_done=True,
        )
        
        return seo_optimized_html
    
    async def _review_code(self, html_content: str) -> str:
        """代码审查"""
        self.printer.update_item("review", "代码审查...")
        
        result = await Runner.run(
            code_review_agent,
            html_content,
        )
        
        reviewed_html = result.final_output
        
        self.printer.update_item(
            "review",
            "代码审查完成",
            is_done=True,
        )
        
        return reviewed_html
    
    async def _deploy_website(self) -> str:
        """部署网站"""
        self.printer.update_item("deploy", "部署网站...")
        
        result = await Runner.run(
            deploy_agent,
            str(self.output_dir),
        )
        
        deploy_url = result.final_output
        
        return deploy_url
