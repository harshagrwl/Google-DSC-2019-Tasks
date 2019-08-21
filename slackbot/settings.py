import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


SECRET_KEY = os.getenv("xoxp-718653270114-723720180593-730656138004-b42a3db0bf57886c3ba99372ecb96765")
GCS_API_KEY = os.getenv("AIzaSyDtY1j0Bezk8BXw_9SKAXWYG6EyAoDryI8")
GCS_ENGINE_ID = os.getenv("004427544878426260376:axdgrmc-h0m")