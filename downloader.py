from dotenv import load_dotenv
import os

load_dotenv()

# Select site to download from
SITE = "SQLBI"
SITE_USERNAME = os.getenv(f"{SITE}_username")
SITE_PASSWORD = os.getenv(f"{SITE}_password")
