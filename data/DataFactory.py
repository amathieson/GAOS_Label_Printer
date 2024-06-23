import http.client
import json
import urllib.parse
from typing import Literal

from data.LabelData import LabelData

_ROOT_SERVER = "https://gaos.genav.ch/"
_API_CRED_EMAIL = '__gaos_gear_printer@genav.ch'
_API_CRED_PASSWORD = 'QfN?g^8r-URG=GCY'
_API_SERVER = "gaos.genav.ch"


class DataFactory:
    _ACCESS_TOKEN: str = ""

    def __init__(self):
        conn = http.client.HTTPSConnection(_API_SERVER, 443)
        payload = 'email=' + urllib.parse.quote(_API_CRED_EMAIL) + '&password=' + urllib.parse.quote(_API_CRED_PASSWORD)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/gear/api/?authenticate", payload, headers)
        res = conn.getresponse()
        data = res.read()
        # Parse the response
        dta = json.loads(data.decode("utf-8"))
        if dta['token'] is not None:
            print("Successfully authenticated as '%s'" % dta['technician']['name'])
            self._ACCESS_TOKEN = dta['token']

    def fetch_asset(self, asset_id: str) -> LabelData:
        conn = http.client.HTTPSConnection(_API_SERVER, 443)
        conn.request("GET", "/gear/api/?getItemData&items%5B%5D=" + asset_id + "&token=" + self._ACCESS_TOKEN)
        res = conn.getresponse()
        data = res.read()
        # Parse the response
        dta = json.loads(data.decode("utf-8"))
        return LabelData(AssetID=asset_id, AssetTags=','.join(dta[0]['data']['tags']), AssetName=dta[0]['data']['name'],
                         ArrowDirection=None, LocationName=dta[0]['data']['location_name'],
                         LocationID=dta[0]['data']['locationID'])

    def fetch_location(self, location_id: str, direction: Literal["NORTH", "EAST", "SOUTH", "WEST"] or None)\
            -> LabelData:
        conn = http.client.HTTPSConnection(_API_SERVER, 443)
        conn.request("GET", "/gear/api/?getLocationData&location=" + location_id + "&token=" +
                     self._ACCESS_TOKEN)
        res = conn.getresponse()
        data = res.read()
        # Parse the response
        dta = json.loads(data.decode("utf-8"))
        return LabelData(AssetID=dta[0]['gearID'], AssetTags='', AssetName='',
                         ArrowDirection=direction, LocationName=dta[0]['location_name'],
                         LocationID=dta[0]['location_ID'])
