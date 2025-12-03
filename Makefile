# 可配置变量
PYTHON := python3.12
PIP := pip3

# 虚拟环境
VENV := .venv
ACTIVATE := . $(VENV)/bin/activate

.PHONY: install run build deploy

install:
	@echo "📦 安装开发依赖..."
	uv sync
	@echo "✅ 依赖安装完成，激活环境：source $(VENV)/bin/activate"

crawl:
	@echo "🚀 抓取trending..."
	# $(ACTIVATE) && uv run python ./github_trending_scraper.py
	$(ACTIVATE) && uv run python main.py crawl

gene:
	@echo "🚀 启动解析..."
	$(ACTIVATE) && uv run python ./main.py

run: crawl gene
	@echo "🚀 启动服务..."
	# $(ACTIVATE) && uv run python ./main.py cate

clean-cache:
	@echo "🚀 清理缓存..."
	rm -rf .astro && rm -rf  node_modules/.astro

build: clean-cache
	@echo "🚀 构建服务..."
	pnpm run build

deploy:
	@echo "🚀 部署服务..."
	pnpm run deploy
