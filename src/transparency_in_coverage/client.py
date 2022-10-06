import requests
import json

from requests.exceptions import ConnectionError
from requests.models import Response
from urllib.request import urlopen
from urllib.error import HTTPError


class TransCovClient:

    def get_coverage_links(self)-> dict:
        response =  self._get_files_links()
        if response.status_code != 200:
            return {"success": False, "status_code": response.status_code}
        result = response.json()
        result["success"] = True
        return result
    
    def get_json_file_from_link(self, link:str) -> dict:
        try:
            response = urlopen(link)
        except HTTPError as e:
            return {"success": False, "error": e}

        try:
            data_json = json.loads(response.read())
        except UnicodeDecodeError:
            return {"success": False, "error": "decode error"}

        return {"success": True, "data": data_json}


    def _get_files_links(self)-> Response:
        try:
            return requests.get("https://transparency-in-coverage.uhc.com/api/v1/uhc/blobs/")
        except ConnectionError:
            response = Response()
            response.error_type = "connection error"
            response.status_code = 500
            response._content = b'{ "error" : "connection error" }'
            return response
