# Academic Homepage Automated Generation System | [中文版](README.md)

This is a multi-agent system project for automatically generating academic personal homepages based on user input. The system uses OpenAI's large language models and agent framework, with multiple expert agents collaborating to generate, optimize, and deploy academic homepages.

## Architecture

System workflow:

1. User inputs personal information and requirements
2. `triage_agent` analyzes user requirements and decides which expert agents to call
3. Expert agents perform their respective tasks:
   - `web_code_agent`: Generates webpage code
   - `academic_content_agent`: Organizes academic content
   - `text_polish_agent`: Polishes text
   - `ui_beautify_agent`: Beautifies interface
   - `seo_agent`: Optimizes SEO
   - `code_review_agent`: Reviews code
   - `deploy_agent`: Deploys website
4. Finally generates a complete academic homepage

## System Requirements

- Python 3.12+ (Recommended)
- OpenAI API key (needs to be set in environment variables as `OPENAI_API_KEY`, e.g., export OPENAI_API_KEY=sk-...)
- Necessary dependency packages:
  - openai-agents
  - rich
  - pydantic

## Installation Guide

1. Clone the repository:

```bash
git clone https://github.com/Yaxin9Luo/auto_homepage.git
cd auto_homepage
```

2. Create and activate conda environment:

```bash
conda create -n auto_homepage python=3.12
conda activate auto_homepage
```

3. Install dependencies:

```bash
# Install rich library
conda install -c conda-forge rich

# Install openai-agents library
python -m pip install openai-agents

# Install other dependencies
pip install pydantic
```

4. Set OpenAI API key:

```bash
# Linux/macOS
export OPENAI_API_KEY=your_api_key_here

# Windows
set OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Activate conda environment:

```bash
conda activate auto_homepage
```

2. Run the system:

```bash
python main.py
```

3. Follow the prompts to input your academic information:
   - Basic information (name, title, institution, email)
   - Research areas
   - Educational background
   - Published papers
   - Project experience
   - Personal profile
   - Website style preference (minimalist/modern/traditional)
   - Language preference (Chinese/English/bilingual)

4. The system will automatically generate an academic homepage and save it to the `output` directory.

## Deployment Guide

### Local Preview

You can use Python's built-in HTTP server to preview the generated academic homepage locally:

```bash
# Enter output directory
cd output

# Start HTTP server
python -m http.server
```

Then visit http://localhost:8000 in your browser to view your academic homepage.

### Deploy to GitHub Pages

1. Create a new GitHub repository:

```bash
# Create a new directory
mkdir -p academic-homepage

# Copy generated files
cp -r output/* academic-homepage/

# Enter new directory
cd academic-homepage

# Initialize Git repository
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub:
   - Log in to your GitHub account
   - Click the "+" icon in the top right corner, select "New repository"
   - Enter "academic-homepage" as the repository name
   - Keep the repository public
   - Do not initialize the repository (do not add README, .gitignore, or license)
   - Click "Create repository"

3. Push the local repository to GitHub (replace `YOUR_USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/academic-homepage.git
git branch -M main
git push -u origin main
```

4. Enable GitHub Pages:
   - On the GitHub repository page, click "Settings"
   - Scroll to the "Pages" section
   - In the "Source" dropdown menu, select the "main" branch and "/(root)" directory
   - Click "Save"

5. After a few minutes, your website will be available at:
   `https://YOUR_USERNAME.github.io/academic-homepage`

### Deploy to Netlify

1. Register a Netlify account (if you don't have one yet): https://app.netlify.com/signup
2. After logging in, click "New site from Git"
3. Select "GitHub" as your Git provider
4. Authorize Netlify to access your GitHub repositories
5. Select the "academic-homepage" repository you just created
6. Keep the default settings in the deployment settings
7. Click "Deploy site"

After a few minutes, Netlify will provide a random URL for your website. You can customize this URL in Netlify's site settings.

## Features

1. Automatically generates academic-style personal homepages
2. Supports multiple languages (Chinese and English)
3. Automatically organizes academic achievements and research interests
4. Optimizes SEO to improve search engine visibility
5. One-click deployment to GitHub Pages or Netlify
6. Responsive design, adapts to different devices
7. Structured data markup to improve search engine understanding

## FAQ

1. **Q: Why is my API call failing?**  
   A: Please ensure you have correctly set the OPENAI_API_KEY environment variable, and that the API key is valid and has sufficient quota.

2. **Q: How do I modify the generated homepage?**  
   A: You can directly edit the index.html file in the output directory, or rerun the program and provide updated information.

3. **Q: How do I add custom CSS styles?**  
   A: You can edit the `<style>` section in the index.html file, or add an external CSS file.

## To-Do Checklist ✅

- [ ] Add more theme templates
  - [ ] Academic minimalist style
  - [ ] Modern tech style
  - [ ] Traditional academic style
- [ ] Add automatic update functionality
  - [ ] Automatic paper retrieval
  - [ ] Citation data updates
- [ ] Optimize generated code quality
  - [ ] Improve code readability
  - [ ] Optimize performance
- [ ] Add more customization options
  - [ ] Color theme customization
  - [ ] Layout adjustment options
  - [ ] Font selection

## Project Progress 📊

- [x] Complete basic architecture design
- [x] Implement multi-agent collaboration system
- [x] Support GitHub Pages deployment
- [x] Support Netlify deployment
- [ ] Complete internationalization support
- [ ] Implement automated testing

## Contribution Guidelines

Contributions of code, issue reports, or improvement suggestions are welcome! Please participate in project development through GitHub Issues or Pull Requests.

## Open Source

This project is completely open source. 