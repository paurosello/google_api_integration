import frappe
from googleplaces import GooglePlaces, types, lang
import requests

LANGUAGE = "ca"

@frappe.whitelist()
def autocomplete_adress(address):
    API_KEY = frappe.get_doc("Google API Settings").api_key

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address':address , "language": LANGUAGE, "key": API_KEY}

    r=requests.get(url, params=params)

    return r.json()['results']

