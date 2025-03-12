import asyncio
import json
import os
from pathlib import Path

from manager import HomepageManager


async def get_user_input():
    """获取用户输入的学术信息"""
    print("欢迎使用学术主页自动化生成系统！")
    print("请输入您的学术信息：")
    
    user_data = {}
    
    # 检查是否存在保存的用户数据
    data_file = Path("user_data.json")
    if data_file.exists():
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                user_data = json.load(f)
            print("已加载保存的用户数据。")
            modify = input("是否需要修改数据？(y/n): ").lower()
            if modify != 'y':
                return user_data
        except Exception as e:
            print(f"加载数据失败: {e}")
    
    # 基本信息
    user_data["name"] = input("姓名: ") or user_data.get("name", "")
    user_data["title"] = input("职称/头衔: ") or user_data.get("title", "")
    user_data["affiliation"] = input("所属机构: ") or user_data.get("affiliation", "")
    user_data["email"] = input("邮箱: ") or user_data.get("email", "")
    
    # 研究领域
    research_interests = input("研究领域(用逗号分隔): ") or user_data.get("research_interests", "")
    user_data["research_interests"] = [i.strip() for i in research_interests.split(",") if i.strip()]
    
    # 教育背景
    education = []
    if "education" in user_data:
        modify_edu = input("是否修改教育背景？(y/n): ").lower()
        if modify_edu != 'y':
            education = user_data["education"]
    
    if not education:
        print("请输入教育背景（输入空行结束）：")
        while True:
            degree = input("学位: ")
            if not degree:
                break
            institution = input("学校: ")
            year = input("年份: ")
            education.append({"degree": degree, "institution": institution, "year": year})
    
    user_data["education"] = education
    
    # 发表论文
    publications = []
    if "publications" in user_data:
        modify_pub = input("是否修改发表论文？(y/n): ").lower()
        if modify_pub != 'y':
            publications = user_data["publications"]
    
    if not publications:
        print("请输入发表论文（输入空行结束）：")
        while True:
            title = input("论文标题: ")
            if not title:
                break
            authors = input("作者(用逗号分隔): ")
            venue = input("发表期刊/会议: ")
            year = input("年份: ")
            url = input("链接(可选): ")
            publications.append({
                "title": title,
                "authors": [a.strip() for a in authors.split(",") if a.strip()],
                "venue": venue,
                "year": year,
                "url": url
            })
    
    user_data["publications"] = publications
    
    # 项目经历
    projects = []
    if "projects" in user_data:
        modify_proj = input("是否修改项目经历？(y/n): ").lower()
        if modify_proj != 'y':
            projects = user_data["projects"]
    
    if not projects:
        print("请输入项目经历（输入空行结束）：")
        while True:
            name = input("项目名称: ")
            if not name:
                break
            description = input("项目描述: ")
            year = input("年份: ")
            url = input("链接(可选): ")
            projects.append({
                "name": name,
                "description": description,
                "year": year,
                "url": url
            })
    
    user_data["projects"] = projects
    
    # 个人简介
    user_data["bio"] = input("个人简介: ") or user_data.get("bio", "")
    
    # 网站风格偏好
    user_data["style_preference"] = input("网站风格偏好(简约/现代/传统): ") or user_data.get("style_preference", "简约")
    
    # 语言偏好
    user_data["language_preference"] = input("语言偏好(中文/英文/双语): ") or user_data.get("language_preference", "中文")
    
    # 保存用户数据
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(user_data, f, ensure_ascii=False, indent=2)
    
    return user_data


async def main():
    user_data = await get_user_input()
    
    # 创建输出目录
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 运行主页生成器
    manager = HomepageManager()
    await manager.run(user_data)
    
    print("\n学术主页生成完成！请查看 output 目录。")


if __name__ == "__main__":
    asyncio.run(main())
