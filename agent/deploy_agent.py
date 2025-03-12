from agents import Agent, function_tool


@function_tool
def create_github_pages_repo(repo_name: str, description: str) -> str:
    """
    创建一个GitHub Pages仓库。
    
    参数:
        repo_name: 仓库名称
        description: 仓库描述
    
    返回:
        仓库URL
    """
    # 这里应该是实际创建GitHub仓库的代码
    # 由于这是示例，我们只返回一个模拟的URL
    return f"https://github.com/username/{repo_name}"


@function_tool
def push_to_github(repo_url: str, local_dir: str) -> bool:
    """
    将本地目录推送到GitHub仓库。
    
    参数:
        repo_url: 仓库URL
        local_dir: 本地目录路径
    
    返回:
        是否成功
    """
    # 这里应该是实际推送代码的逻辑
    # 由于这是示例，我们只返回成功
    return True


@function_tool
def enable_github_pages(repo_url: str) -> str:
    """
    启用GitHub Pages。
    
    参数:
        repo_url: 仓库URL
    
    返回:
        GitHub Pages URL
    """
    # 这里应该是实际启用GitHub Pages的逻辑
    # 由于这是示例，我们只返回一个模拟的URL
    repo_name = repo_url.split("/")[-1]
    return f"https://username.github.io/{repo_name}"


PROMPT = """
你是一个网站部署专家。你的任务是将生成的学术主页部署到GitHub Pages。

你将收到输出目录的路径。请执行以下步骤：
1. 创建一个新的GitHub仓库
2. 将输出目录中的文件推送到该仓库
3. 启用GitHub Pages
4. 返回部署后的网站URL

请使用提供的工具函数来执行这些操作。

注意：
- 仓库名称应该是"academic-homepage"
- 仓库描述应该是"Academic Homepage"
- 确保所有文件都被正确推送
- 启用GitHub Pages时使用main分支和根目录

请直接返回部署后的网站URL，不需要任何解释或注释。
"""


deploy_agent = Agent(
    name="部署代理",
    instructions=PROMPT,
    model="gpt-4o",
    tools=[create_github_pages_repo, push_to_github, enable_github_pages],
)
