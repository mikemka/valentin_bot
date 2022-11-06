import ast
import dotenv
import os
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

DOTENV_PATH = BASE_DIR / '.env'

if DOTENV_PATH.exists():
    dotenv.load_dotenv(DOTENV_PATH)

DEBUG = ast.literal_eval(os.getenv('DEBUG'))

TOKEN = os.getenv('TOKEN')

if DEBUG:
    TOKEN = os.getenv('DEBUG_TOKEN')
