import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

print(os.getenv("DATABASE_FILENAME"))
DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "twitter.db"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "sqlite", DATABASE_FILENAME)
