import os
from dotenv import load_dotenv

load_dotenv()

USER_ID = int(os.environ.get("USER_ID")) # set user_id to send messages to him.
