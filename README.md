# 学术主页自动化生成系统

这是一个多代理系统的学术主页自动化生成项目，可以根据用户输入自动生成和优化学术个人主页。系统使用OpenAI的大语言模型和代理框架，通过多个专家代理协作完成学术主页的生成、优化和部署。

## 架构

系统流程：

1. 用户输入个人信息和需求
2. `triage_agent` 分析用户需求，决定调用哪些专家代理
3. 专家代理执行各自的任务：
   - `web_code_agent`: 生成网页代码
   - `academic_content_agent`: 整理学术内容
   - `text_polish_agent`: 润色文本
   - `ui_beautify_agent`: 美化界面
   - `seo_agent`: 优化SEO
   - `code_review_agent`: 审查代码
   - `deploy_agent`: 部署网站
4. 最终生成完整的学术主页

## 系统要求

- Python 3.12+ (Recommend)
- OpenAI API 密钥（需要在环境变量中设置 `OPENAI_API_KEY`,eg, export OPENAI_API_KEY=sk-...）
- 安装了必要的依赖包：
  - openai-agents
  - rich
  - pydantic

## 安装指南

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/academic-homepage-generator.git
cd academic-homepage-generator
```

2. 创建并激活conda环境：

```bash
conda create -n personal_page python=3.12
conda activate personal_page
```

3. 安装依赖：

```bash
# 安装rich库
conda install -c conda-forge rich

# 安装openai-agents库
python -m pip install openai-agents

# 安装其他依赖
pip install pydantic
```

4. 设置OpenAI API密钥：

```bash
# Linux/macOS
export OPENAI_API_KEY=your_api_key_here

# Windows
set OPENAI_API_KEY=your_api_key_here
```

## 使用方法

1. 激活conda环境：

```bash
conda activate personal_page
```

2. 运行系统：

```bash
python -m academic_homepage_generator.main
```

3. 按照提示输入您的学术信息：
   - 基本信息（姓名、职称、机构、邮箱）
   - 研究领域
   - 教育背景
   - 发表论文
   - 项目经历
   - 个人简介
   - 网站风格偏好（简约/现代/传统）
   - 语言偏好（中文/英文/双语）

4. 系统会自动生成学术主页，并保存到 `output` 目录中。

## 部署指南

### 本地预览

您可以使用Python的内置HTTP服务器在本地预览生成的学术主页：

```bash
# 进入output目录
cd output

# 启动HTTP服务器
python -m http.server
```

然后在浏览器中访问 http://localhost:8000 即可查看您的学术主页。

### 部署到GitHub Pages

1. 创建一个新的GitHub仓库：

```bash
# 创建一个新目录
mkdir -p academic-homepage

# 复制生成的文件
cp -r output/* academic-homepage/

# 进入新目录
cd academic-homepage

# 初始化Git仓库
git init
git add .
git commit -m "Initial commit"
```

2. 在GitHub上创建一个新仓库：
   - 登录您的GitHub账户
   - 点击右上角的"+"图标，选择"New repository"
   - 仓库名称输入"academic-homepage"
   - 保持仓库为公开（Public）
   - 不要初始化仓库（不要添加README、.gitignore或license）
   - 点击"Create repository"

3. 将本地仓库推送到GitHub（替换`YOUR_USERNAME`为您的GitHub用户名）：

```bash
git remote add origin https://github.com/YOUR_USERNAME/academic-homepage.git
git branch -M main
git push -u origin main
```

4. 启用GitHub Pages：
   - 在GitHub仓库页面，点击"Settings"
   - 滚动到"Pages"部分
   - 在"Source"下拉菜单中，选择"main"分支和"/(root)"目录
   - 点击"Save"

5. 几分钟后，您的网站将在以下URL上可用：
   `https://YOUR_USERNAME.github.io/academic-homepage`

### 部署到Netlify

1. 注册Netlify账户（如果您还没有）：https://app.netlify.com/signup
2. 登录后，点击"New site from Git"
3. 选择"GitHub"作为您的Git提供商
4. 授权Netlify访问您的GitHub仓库
5. 选择您刚刚创建的"academic-homepage"仓库
6. 在部署设置中，保持默认设置不变
7. 点击"Deploy site"

几分钟后，Netlify将为您的网站提供一个随机的URL。您可以在Netlify的站点设置中自定义这个URL。

## 功能特点

1. 自动生成符合学术风格的个人主页
2. 支持多语言（中文和英文）
3. 自动整理学术成果和研究兴趣
4. 优化SEO，提高搜索引擎可见性
5. 一键部署到GitHub Pages或Netlify
6. 响应式设计，适配不同设备
7. 结构化数据标记，提高搜索引擎理解

## 常见问题

1. **Q: 为什么我的API调用失败？**  
   A: 请确保您已正确设置OPENAI_API_KEY环境变量，并且API密钥有效且有足够的额度。

2. **Q: 如何修改已生成的主页？**  
   A: 您可以直接编辑output目录中的index.html文件，或者重新运行程序并提供更新的信息。

3. **Q: 如何添加自定义CSS样式？**  
   A: 您可以编辑index.html文件中的`<style>`部分，或者添加外部CSS文件。

## 建议改进

1. 添加更多模板和主题
2. 支持更多部署平台
3. 添加更多自定义选项
4. 集成学术数据库API，自动获取论文信息
5. 添加图片上传功能
6. 实现多语言切换功能
7. 添加博客和出版物页面

## 贡献指南

欢迎贡献代码、报告问题或提出改进建议！请通过GitHub Issues或Pull Requests参与项目开发。

## 许可证

本项目采用MIT许可证。详情请参阅LICENSE文件。
