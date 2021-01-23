# https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=Freddie%20Mercury&exintro=1

"""
WIKI-RELATED FUNCTIONS
"""

import requests

QUERY_STR_PRE_ARTIST = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="
QUERY_STR_POST_ARTIST = "&exintro=1"


def get_info(artist_str):
    """
    :param artist_str: string with artist's name on it
    :returns: json containing short blurb about artist
    """

    result_json = ""
    return result_json


def find_spaces(artist_str):
    return


def main():
    test_session = requests.Session()
    test_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=Freddie%20Mercury&exintro=1"
    test_params = {
        "action": "query",
        "format": "json",
        "prop": "extract",
        "titles": "Freddie%20Mercury",
        "exintro": "1"
    }

    test_req = test_session.get(url=test_url, params=test_params)
    data = test_req.json()

    print(data)


if __name__ == "__main__":
    main()
