import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), os.getenv("ENVIRONMENT_FILE"))
load_dotenv(dotenv_path=dotenv_path, override=True)

APP_HOST: str = os.environ.get("HOST")
APP_PORT: int = int(os.environ.get("PORT"))
APP_DEBUG: bool = bool(os.environ.get("DEBUG"))
DEV_TOOLS_PROPS_CHECK: bool = bool(os.environ.get("DEV_TOOLS_PROPS_CHECK"))
