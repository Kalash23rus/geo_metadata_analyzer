import json
import requests
import time
from tqdm import tqdm

def get_geo_metadata(geo_id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term={geo_id}&retmode=json"
    response = requests.get(url)
    data = response.json()

    if data.get("esearchresult", {}).get("idlist"):
        geo_uid = data["esearchresult"]["idlist"][0]
        summary_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gds&id={geo_uid}&retmode=json"
        summary_response = requests.get(summary_url)
        summary_data = summary_response.json()
        metadata = summary_data["result"][geo_uid]
        return metadata
    else:
        return None