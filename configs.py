import datetime
import json

from dotenv import load_dotenv


def root_path():
    import os
    return os.path.dirname(os.path.abspath(__file__))


def get_var(var_name: str):
    load_dotenv()
    import os
    return os.getenv(var_name)


def get_headers():
    return {
        "x-rapidapi-key": get_var("API_TOKEN")
    }


def actual_season():
    return datetime.datetime.now().year
