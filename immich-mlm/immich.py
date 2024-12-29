import logging
import json
import requests
import urllib.parse


class Immich:

    def _init__(self, urlbase, apikey):
        self.urlbase = urlbase
        self.apikey = apikey
        self.tags = {}
        self.processed = {}
    
    def _request(self, uri, method, payload, content="json"):
        url = f"{self.urlbase}{uri}"

        match method:
            case "GET":
                headers = {
                    'Accept': 'application/json',
                    "x-api-key": self.apikey
                }
            case "POST":
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "x-api-key": self.apikey
                }
            case "PUT":
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "x-api-key": self.apikey
                }
            case _:
                headers = {
                    'Accept': 'application/json',
                    "x-api-key": self.apikey
                }
        r = requests.request(method, url, headers=headers, data=payload)

        if content == "json":
            data = r.json()
            logging.debug(json.dumps(data, indent=3))
        elif content == "file":
            data = r.content
        else:
            data = r.content
        return data

    def get_paths(self):
        uri = "/view/folder/unique-paths"
        method = "GET"
        payload = {}
        data = self._request(uri, method, payload)
        return data
    
    def get_assetsbypath(self, path):
        pathenc = urllib.parse.quote_plus(path)
        uri = f"/view/folder?path={pathenc}"
        method = "GET"
        payload = {}
        data = self._request(uri, method, payload)
        return data

    def get_asset(self, asset_id):
        uri = f"/assets/{asset_id}"
        method = "GET"
        payload = {}
        data = self._request(uri, method, payload)
        return data
    
    def get_tags(self):
        uri = "/tags"
        method = "GET"
        payload = {}
        data = self._request(uri, method, payload)
        return data
    
    def tag_assets(self, tag_id, asset_ids):
        uri = f"/tags/{tag_id}/assets"
        method = "PUT"
        payload = {
            "ids": asset_ids    # List of asset ids
        }
        data = self._request(uri, method, payload)
        return data
    
    def download_asset(self, asset_id, asset_type):
        uri = f"/assets/{asset_id}/{asset_type}"
        method = "GET"
        payload = {}
        data = self._request(uri, method, payload, content="file")
        return data

    def get_config(self):
        uri = "/system-config"
        method = "GET"
        payload = {}
        data = self._request(uri, method, payload)
        return data

    def save_config(self, cfgfile):
        c = self.get_config()
        with open(cfgfile, 'w') as fp:
            json.dump(c, fp, indent=3)

    def load_tags(self):
        self.tags = self.get_tags()
        