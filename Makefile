# 可配置变量
PYTHON := python3.12
PIP := pip3

# 虚拟环境
VENV := .venv
ACTIVATE := . $(VENV)/bin/activate

.PHONY: install run

install:
	@echo "📦 创建虚拟环境..."
	python3.12 -m venv $(VENV)
	@echo "📦 安装生产依赖..."
	$(ACTIVATE) && pip install -U pip uv -i https://mirrors.cernet.edu.cn/pypi/web/simple
	$(ACTIVATE) && uv pip install -r requirements.txt -i https://mirrors.cernet.edu.cn/pypi/web/simple
	@echo "📦 安装开发依赖..."
	@echo "✅ 依赖安装完成，请活环境：source $(VENV)/bin/activate"


run:
	@echo "🚀 启动服务..."
	$(ACTIVATE) && uv run python ./github_trending_scraper.py
	$(ACTIVATE) && uv run python ./main.py

deploy:
	@echo "🚀 部署服务..."
	pnpm run deploy
