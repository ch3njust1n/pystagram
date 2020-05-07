import requests
import urllib
import os

class Instagram(object):
    '''
    inputs:
    url (str) URL to video e.g. https://www.instagram.com/p/BSVHktjDn5m/
    '''
    def __init__(self, url):
        self.url = url
        self.title = ''

    '''
    Downloads Instagram video

    inputs:
    dest     (str, optional) Save destination
    filename (str, optional) Save filename
    '''
    def download(self, dest='/home', filename=''):
        try:
            resp = requests.get(os.path.join(self.url, '?__a=1'))
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception(e)
        except requests.exceptions.ConnectionError as e:
            raise Exception(e)
        except requests.exceptions.Timeout as e:
            raise Exception(e)
        except requests.exceptions.InvalidURL as e:
            raise Exception(e)
        except requests.exceptions.RequestException as e:
            raise Exception(e)

        try:
            shortcode_media = resp.json()['graphql']['shortcode_media']
            video_url = shortcode_media['video_url']
            time_stamp = shortcode_media['taken_at_timestamp']
        except ValueError as e:
            raise Exception(e)

        self.title = time_stamp if len(filename) == 0 else filename

        save_path = os.path.join(dest, f'{self.title}.mp4')

        if not os.path.exists(save_path):
            try:
                urllib.request.urlretrieve(video_url, save_path)
            except  urllib.error.ContentTooShortError as e:
                raise Exception(e)
            except urllib.error.HTTPError as e:
                raise Exception(e)
            except urllib.error.URLError as e:
                raise Exception(e)
