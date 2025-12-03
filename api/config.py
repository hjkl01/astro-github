import os

from loguru import logger
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

log_file_path = os.path.join(BASE_DIR, "logs/stdout.log")
err_log_file_path = os.path.join(BASE_DIR, "logs/error.log")

logger.add(
    log_file_path,
    format="{process} {thread} {time:YYYY.MM.DD HH.mm.ss} {level}.{file}.{name}.{module}.{line} {message}",
    rotation="100 MB",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=True,
    level="INFO",
)
logger.add(
    err_log_file_path,
    format="{time:YYYY.MM.DD HH.mm.ss} {level}.{file}.{name}.{module}.{line} {message}",
    rotation="100 MB",
    level="ERROR",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

load_dotenv()

QWEN_KEY = os.getenv("QWEN_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:14b")
