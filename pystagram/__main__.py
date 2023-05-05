"""
Author: Justin Chen
Date: 5.7.2020

API for downloading Instagram videos
"""
import requests
import urllib
import os
import re


class Instagram(object):
    """
    inputs:
    url (str) URL to video e.g. https://www.instagram.com/p/BSVHktjDn5m/
    """

    def __init__(self, url: str):
        self.url = self.format(url)

    """
    inputs:
    url (str) URL to video

    outputs:
    url (str) Formatted video url
    """

    def format(self, url: str) -> str:
        if url.startswith("www"):
            url = url.replace("www", "https://www")

        # remove queries
        return re.sub(r"\?(.*)", "", url)

    """
    Downloads Instagram video

    inputs:
    dst      (str, optional) Save destination. Defaults to current working directory.
    filename (str, optional) Save filename
    """

    def download(self, dst: str = "", filename: str = ""):
        try:
            resp = requests.get(os.path.join(self.url, "?__a=1"))
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
            shortcode_media = resp.json()["graphql"]["shortcode_media"]
            is_edge_media = "edge_sidecar_to_children" in shortcode_media.keys()

            time_stamp = shortcode_media["taken_at_timestamp"]

            if filename is None or len(filename) == 0:
                filename = time_stamp

            if not is_edge_media:
                if not shortcode_media["is_video"]:
                    return

                video_url = shortcode_media["video_url"]
                self.retrieve(video_url, dst, filename)
            else:
                edges = shortcode_media["edge_sidecar_to_children"]["edges"]
                dst_dir = os.path.join(dst, filename)

                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

                for i, e in enumerate(edges):
                    node = e["node"]

                    if not node["is_video"]:
                        continue

                    self.retrieve(
                        node["video_url"], dst_dir, f"{i}-{node['shortcode']}"
                    )
        except ValueError as e:
            raise Exception(e)

    """
    Download video

    inputs:
    video_url (str) Video url to download
    dst       (str) Directory to save to
    filename  (str) Save file name
    """

    def retrieve(self, video_url: str, dst: str, filename: str):
        if len(dst) == 0:
            dst = os.getcwd()

        save_path = os.path.join(dst, f"{filename}.mp4")

        if not os.path.exists(save_path):
            try:
                urllib.request.urlretrieve(video_url, save_path)
            except urllib.error.ContentTooShortError as e:
                raise Exception(e)
            except urllib.error.HTTPError as e:
                raise Exception(e)
            except urllib.error.URLError as e:
                raise Exception(e)
