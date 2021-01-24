"""
Embedding a playlist
<iframe src="https://open.spotify.com/embed/album/1DFixLWuPkv3KT3TnV35m3" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>

Song Test
https://open.spotify.com/track/05SUJyDZaEJaqwBr6UsKRH?si=Mr6NduYZR4GkFbW4fM8NOg

AUTH TOKEN: BQDwwcEF-2dsmCETTqRmZETsd_s4I4E9xnKnQXceBq2zJ28xvyZg_JAMiOFgwhNkeLZBLKVRWdYlOuHWb64x0Fw_3-YbyKJwWiVlakle9IinMSPXUWLOqMbePRfFjPtBEU4FGUVmi7X0hpK4wvHc91YFng0-FX4

https://api.spotify.com/v1/search?q=Digitalism&type=track%2Cartist&limit=10&offset=5

"""

# QUERY_START = "https://api.spotify.com/v1/search?q="
# QUERY_TYPE = "&type="
# QUERY_LIMIT = "&limit="
# QUERY_OFFSET = "&offset=5"

BEARER = "Bearer "
AUTH_TOKEN = "BQBO_smalYzCJmWdjbzaX9PzUUh2oHpGZD7SemK4rs04mJiJ5Hv3N7TsS3BhNfg921xwt1M4eiCfAY9jG6dZ7cAavwlcGZl0hJKm__LgqjzgIw6Xh6iorfGdRB8b14b5_2p5U2i0LDTd_VGNvyi4VoEtvdoj2oo"

import urllib3

def get_spotify_json(artist_str,):
    """
    Returns a JSON containing page information for a specific Wiki file.
    Needs a string with the artist's name.
    """
    url = QUERY_STR_PRE_ARTIST + make_spaces_ascii(artist_str) + QUERY_STR_POST_ARTIST
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

def main():
    # """
    # market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_genres=house&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50
    # """
    # http = urllib3.PoolManager()
    # data = '{"market": "US", "seed_artists": "4NHQUGzhtTLFvgF5SZesLK", "seed_genres": "house", "tracks": "0c6xIDDpzE81m2q797ordA", "min_energy": "0.4", "min_popularity": "50"}'
    # url = 'https://api.spotify.com/v1/recommendations?'
    # req = http.request(url, data, {'Content-Type': 'application/json', 'Authorization': BEARER + AUTH_TOKEN})
    # f = http.urlopen(req)
    # for x in f:
    #     print(x)
    # f.close()


    http = urllib3.PoolManager()
    req = http.request(
            'GET',
            'https://api.spotify.com/v1/recommendations?',
            headers = {
                'Authorization': BEARER + AUTH_TOKEN
            },
            fields = { 'market': 'US',
                       'seed_artists': '4NHQUGzhtTLFvgF5SZesLK',
                       'seed_genres': 'house',
                       'tracks': '0c6xIDDpzE81m2q797ordA',
                       'min_energy': '0.4',
                       'min_popularity': '50',
                       'authorization': AUTH_TOKEN
            }
    )
    print(req.data)


if __name__ == "__main__":
    main()