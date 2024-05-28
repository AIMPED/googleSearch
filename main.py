from dotenv import load_dotenv
from classes import GoogleSearch
import os


_ = load_dotenv()
API_KEY = os.environ.get('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.environ.get('GOOGLE_ENGINE_ID')

search_client = GoogleSearch(
    api_key=API_KEY,
    engine_id=SEARCH_ENGINE_ID
)


if __name__ == '__main__':
    print(
        search_client.parsed_search(
            query="aimped site:github.com"
            )
    )

    print(
        search_client.raw_search(
            query="aimped site:github.com"
            )
    )

