import frappe
from googleplaces import GooglePlaces, types, lang
import requests

YOUR_API_KEY = 'AIzaSyBiuhjZr_TPUdxRK3V_QDqEZUY2bkcU3vQ'
LANGUAGE = "ca"

@frappe.whitelist()
def autocomplete_adress(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address':address , "language": LANGUAGE, "key": YOUR_API_KEY}

    r=requests.get(url, params=params)

    return r.json()['results']

