import requests


class GoogleSearch:

    def __init__(self, api_key, engine_id):
        self.api_key = api_key
        self.engine_id = engine_id

    def raw_search(self, query: str, num_results: int = 10) -> list:
        """
        function performs a Google search

        Args:
            query: string to search
            num_results: desired number of results, defaults to 10

        Returns:
            list of json
        """
        # calculate number of pages searched, google returns 10 results per page
        # each page requires a separate api call
        pages = num_results // 10

        # set up variable for result pages
        data_list = []

        # iterate through pages
        for page in range(1, pages + 1):
            start = (page - 1) * 10 + 1
            try:
                response = requests.get(
                    url='https://content.googleapis.com/customsearch/v1',
                    params={
                        'cx': self.engine_id,
                        'q': query,
                        'key': self.api_key,
                        'start': start
                    }
                )
                response.raise_for_status()

                data_list.append(response.json())

            except requests.exceptions.HTTPError as err:
                print(err)

        return data_list

    def parsed_search(self, query: str) -> tuple[list, list]:
        """
        function parses the json file for page titles and urls
        Args:
            query: search query

        Returns:
            tuple of page titles and urls
        """
        # iterate over the search results of the corresponding page.
        # google returns 10 results per result page
        _titles = []
        _links = []

        for data in self.raw_search(query):
            search_items = data.get('items')
            for search_item in search_items:
                pagemap = search_item.get('pagemap', {})
                meta_tags = pagemap.get('metatags')[0]
                _titles.append(meta_tags.get('og:title'))
                _links.append(search_item.get('link'))
        return _titles, _links

